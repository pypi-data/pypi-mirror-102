import limix
import numpy as np
import multiprocessing
from functools import partial
from statsmodels.sandbox.stats.multicomp import multipletests

from scipy.stats import itemfreq

from .glm import glm_LRT

def show_progress(RV=None):
    return RV

def qtl_scan(y, GT, depth, M=None, interact=None, method='limix', nproc=1, 
             min_AF=0.05, **kwargs):
    n_gene = y.shape[1]
    n_sample = y.shape[0]
    
    pval_GT = np.array([None] * y.shape[1], float)
    fdr_GT  = np.array([None] * y.shape[1], float)
    coef_GT = np.array([None] * y.shape[1], float)
    coef_GT_se = np.array([None] * y.shape[1], float)
    
    pval_inter = np.array([None] * y.shape[1], float)
    fdr_inter  = np.array([None] * y.shape[1], float)
    coef_inter = np.array([None] * y.shape[1], float)
    coef_inter_se = np.array([None] * y.shape[1], float)
    
    ## define function with kwargs
    if method == 'statsmodels' or method == 'NB':
        func_use = partial(qtl_statsmodels, **kwargs)
    else:
        func_use = partial(qtl_limix, **kwargs)
        
    ## run GLM with single or multiple processes
    if nproc == 1:
        for i in range(y.shape[1]): # SNP-gene pair
            if np.max(itemfreq(GT[:, i])[:, 1]) > ((1 - min_AF) * n_sample):
                continue
                
            pval_GT[i], pval_inter[i], _qtl1, _qtl2 = func_use(
                y[:, i], GT[:, i], depth, M, interact)
            
            if method != "limix":
                continue
            
            coef_GT[i] = np.array(_qtl1.effsizes['h2']['effsize'])[-1]
            coef_GT_se[i] = np.array(_qtl1.effsizes['h2']['effsize_se'])[-1]
            coef_inter[i] = np.array(_qtl2.effsizes['h2']['effsize'])[-1]
            coef_inter_se[i] = np.array(_qtl2.effsizes['h2']['effsize_se'])[-1]
    else:
        pool = multiprocessing.Pool(processes=nproc)
        result = []
        idx_kept = []
        for i in range(y.shape[1]): # SNP-gene pair
            if np.max(itemfreq(GT[:, i])[:, 1]) > ((1 - min_AF) * n_sample):
                continue
                
            idx_kept.append(i)
            result.append(pool.apply_async(
                func_use, (y[:, i], GT[:, i], depth, M, interact),
                callback=show_progress
            ))
        
        pool.close()
        pool.join()
        result = [res.get() for res in result]
        
        for ii in range(len(idx_kept)):
            _idx = idx_kept[ii]
            pval_GT[_idx], pval_inter[_idx], _qtl1, _qtl2 = result[ii]
            
            if method != "limix":
                continue
            
            coef_GT[_idx] = np.array(_qtl1.effsizes['h2']['effsize'])[-1]
            coef_GT_se[_idx] = np.array(_qtl1.effsizes['h2']['effsize_se'])[-1]
            coef_inter[_idx] = np.array(_qtl2.effsizes['h2']['effsize'])[-1]
            coef_inter_se[_idx] = np.array(_qtl2.effsizes['h2']['effsize_se'])[-1]
            
    
    ## Multiple testing correction
    _idx = pval_GT >= 0
    print("%d out %d tests valid for FDR correction" %(sum(_idx), len(_idx)))
    if sum(_idx) > 1:
        fdr_GT[_idx] = multipletests(pval_GT[_idx], method='fdr_bh')[1]
        fdr_inter[_idx] = multipletests(pval_inter[_idx], method='fdr_bh')[1]

    ## Return results
    RV = {}
    RV['pval_GT'] = pval_GT
    RV['fdr_GT']  = fdr_GT
    RV['pval_inter'] = pval_inter
    RV['fdr_inter']  = fdr_inter
    
    RV['coef_GT']  = coef_GT
    RV['coef_GT_se']  = coef_GT_se
    RV['coef_inter']  = coef_inter
    RV['coef_inter_se']  = coef_inter_se
    
    return RV


def qtl_NB(y, GT, depth, M=None, interact=None, **kwargs):
    print("Please use `qtl_statsmodels` in future.")
    return qtl_statsmodels(y, GT, depth, M=None, interact=None, **kwargs)


def qtl_statsmodels(y, GT, depth, M=None, interact=None, **kwargs):
    """
    default: family=sm.families.NegativeBinomial()
    """
    if M is not None:
        M1 = np.append(np.log(depth + 1).reshape(-1, 1), M, axis=1)
    else:
        M1 = np.log(depth + 1).reshape(-1, 1)
    
    # if M is not None:
    #     M1 = np.append(depth.reshape(-1, 1), M, axis=1)
    # else:
    #     M1 = depth.reshape(-1, 1)

    try:
        nb_res1 = glm_LRT(y, GT, M=M1, **kwargs)
        pval_GT = nb_res1.p_LRT
    except:
        pval_GT, nb_res1 = None, None
        
    # Test for interaction
    pval_inter, nb_res2 = None, None
    if interact is not None:
        M2 = np.append(GT.reshape(-1, 1), M1, axis=1)
        try:
            nb_res2 = glm_LRT(y, GT * interact, M=M2, **kwargs)
            pval_inter = nb_res2.p_LRT
        except:
            pass
    
    return pval_GT, pval_inter, nb_res1, nb_res2


def qtl_limix(y, GT, depth=None, M=None, interact=None, add_intercept=True,
              family='normal'):
    """
    family: normal, poisson, binomial, etc.
    """
    Ken = None if depth is None else np.diag(1.0 / depth)
    if add_intercept:
        if M is not None:
            M1 = np.append(M, np.ones((y.shape[0], 1)), axis=1)
        else:
            M1 = np.ones((y.shape[0], 1))
    else:
        M1 = None if M is None else M.copy()
    
    qtl1 = limix.qtl.scan(GT.reshape(-1, 1), y.reshape(-1, 1), 
                          family, M=M1, K=Ken, verbose=False)
    pval_GT = np.array(qtl1.stats)[0, 4]
        
    pval_inter, qtl2 = None, None
    if interact is not None:
        if M is None:
            M2 = GT.reshape(-1, 1)
        else:
            M2 = np.append(GT.reshape(-1, 1), M1, axis=1)
            
        qtl2 = limix.qtl.scan((GT * interact).reshape(-1,1), y.reshape(-1, 1), 
                              family, M=M2, K=Ken, verbose=False)
        pval_inter = np.array(qtl2.stats)[0, 4]
    
    return pval_GT, pval_inter, qtl1, qtl2


    
# def qtl_scan_limix(y, GT, depth, M=None, interact=None):
#     """
#     """
#     n_gene = y.shape[1]
#     n_sample = y.shape[0]
    
#     pval_GT = np.array([None] * y.shape[1], float)
#     fdr_GT  = np.array([None] * y.shape[1], float)
#     pval_inter = np.array([None] * y.shape[1], float)
#     fdr_inter  = np.array([None] * y.shape[1], float)
    
#     Ken = np.diag(1.0 / depth)
    
#     for i in range(y.shape[1]): # SNP-gene pair
#         if np.max(np.unique(GT[:, i], return_counts=True)[1]) > (0.95 * n_sample):            
#             continue
            
        
            
#         M1 = M.copy()
#         M2 = np.append(GT[:, i:i+1], M1, axis=1)

#         qtl = limix.qtl.scan(GT[:, i:i+1], y[:, i+1], 
#                              'normal', M=M1, K=Ken, verbose=False)
#         pval_GT[i] = np.array(qtl.stats)[:,4]

#         qtl = limix.qtl.scan((GG[:, i] * disease).reshape(-1,1), y[:, i+1], 
#                              'normal', M=M2, K=Ken, verbose=False)
#         pval_inter[i] = np.array(qtl.stats)[:,4]

#     _idx = pval_GT >= 0
#     print(sum(_idx), len(_idx), pval_GT.shape)
#     if sum(_idx) > 1:
#         fdr_GT[_idx] = multipletests(pval_GT[_idx], method='fdr_bh')[1]
#         fdr_inter[_idx] = multipletests(pval_inter[_idx], method='fdr_bh')[1]

#     return pval_GT, fdr_GT, pval_inter, fdr_inter
    

# def qtl_scan_NB(y, GT, depth, M=None, interact=None):
#     """
#     """
#     n_gene = y.shape[1]
#     n_sample = y.shape[0]
    
#     pval_GT = np.array([None] * y.shape[1], float)
#     fdr_GT  = np.array([None] * y.shape[1], float)
#     pval_inter = np.array([None] * y.shape[1], float)
#     fdr_inter  = np.array([None] * y.shape[1], float)
    
#     for i in range(y.shape[1]): # SNP-gene pair
#         if np.max(np.unique(GT[:, i], return_counts=True)[1]) > (0.95 * n_sample):            
#             continue
            
#         if M is not None:
#             M1 = np.append(np.log(depth + 1).reshape(-1, 1), M, axis=1)
#         else:
#             M1 = np.log(depth + 1).reshape(-1, 1)
#         M2 = np.append(GT[:, i:i+1], M1, axis=1)

#         try:
#             nb_res1 = glm_LRT(y[:, i], GT[:, i], M=M1)
#             nb_res2 = glm_LRT(y[:, i], GT[:, i] * interact, M=M2)
#         except:
#             continue

#         pval_GT[i] = nb_res1.p_LRT
#         pval_inter[i] = nb_res2.p_LRT

#     _idx = pval_GT >= 0
#     print(sum(_idx), len(_idx), pval_GT.shape)
#     if sum(_idx) > 1:
#         fdr_GT[_idx] = multipletests(pval_GT[_idx], method='fdr_bh')[1]
#         fdr_inter[_idx] = multipletests(pval_inter[_idx], method='fdr_bh')[1]

#     return pval_GT, fdr_GT, pval_inter, fdr_inter

