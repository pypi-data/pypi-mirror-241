# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 10:04:53 2023

@author: romain.coulon, jialin.hu
"""

import numpy as np
import tdcrpy.TDCRPy as td
import scipy.optimize as opt

def eff(TD, TAB, TBC, TAC, Rad, pmf_1, kB, V, mode2, N=10000, L=1, maxiter=20):
    """
    Caclulation of the efficiency of a TDCR system based on the model TDCRPy.

    Parameters
    ----------
    TD : float
        triple-to-double coincidence ratio. Not consider if mode2="asym". Not consider if mode2="asym".
    TAB : float
        triple-to-double coincidence ratio (coincidences between channel A and B). Not consider if mode2="sym".
    TBC : float
        triple-to-double coincidence ratio (coincidences between channel B and C). Not consider if mode2="sym".
    TAC : float
        triple-to-double coincidence ratio (coincidences between channel A and C). Not consider if mode2="sym".
    Rad : string
        List of radionuclides.
    pmf_1 : string
        list of probability of each radionuclide..
    kB : float
        Birks constant in cm/keV.
    V : float
        volume of the scintillator in ml.
    mode2 : string
        "sym" for symetrical model, "asym" for symetrical model.
    N : interger, optional
        number of Monte-Carlo trials. The default is 1000.
    L : float, optional
        free parameter(s) as initial guess. The default is 1.
    maxiter : interger, optional
        maximum number of iterations of the optimization procedures

    Returns
    -------
    L0 : float
        global free parameter.
    L : tuple
        free parameters (relevant for the asymetric model).
    eff_S : float
        counting efficiency of single events.
    u_eff_S : float
        standard uncertainty of eff_S.
    eff_D : float
        counting efficiency of double coincidences.
    u_eff_D : float
        standard uncertainty of eff_D.
    eff_T : float
        counting efficiency of triple coincidences.
    u_eff_T : float
        standard uncertainty of eff_T.

    """
    # Estimation of the free parameter that minimize the residuals
    # r=opt.minimize_scalar(td.TDCRPy, args=(TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "res", "sym"), method='bounded', bounds=[0, 10000],options={'xatol': 1e-4, 'disp': True, 'maxiter':20})
    r=opt.minimize_scalar(td.TDCRPy, args=(TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "res", "sym"), method='bounded', bounds = (0.5, 2), options={'disp': True, 'maxiter':20})
    # r=opt.minimize_scalar(td.TDCRPy, args=(TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "res", "sym"), method='golden', options={'disp': True, 'maxiter':maxiter})
    L=r.x
    print(r)
    
    if mode2 == "asym":
        L=(L, L, L)           # Free paramete in keV-1
        r=opt.minimize(td.TDCRPy, L, args=(TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "res", "asym"), method='nelder-mead',options={'xatol': 1e-5, 'disp': True, 'maxiter':maxiter})
        L=r.x
        print(r)
        out=td.TDCRPy(L,TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "eff", "asym")
    else:
        out=td.TDCRPy(L,TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "eff", "sym")
        
    L0 = np.mean(L)
    if mode2 == "sym":
        L=(L, L, L)
    eff_S = out[0]
    u_eff_S = out[1]
    eff_D = out[2]
    u_eff_D = out[3]
    eff_T = out[4]
    u_eff_T = out[5]
    
    return L0, L, eff_S, u_eff_S, eff_D, u_eff_D, eff_T, u_eff_T
    
def effCurves(L, TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V):
    effD = []; ueffD = []; tdcr = []; uTdcr = []
    for l in L:
        out=td.TDCRPy(l, TD, TAB, TBC, TAC, Rad, pmf_1, N, kB, V, "eff", "sym", Display=False, barp=True, uncData=False)  
        effD.append(out[2])
        ueffD.append(out[3])
        tdcr.append(out[4]/out[2])
        uTdcr.append(1/out[2]*np.sqrt(out[5]**2+out[4]**2*out[3]**2/out[2]**2))
    return effD, ueffD, tdcr, uTdcr

# L = 1
# TD = 0.977667386529166
# TAB = 0.992232838598821
# TBC = 0.992343419459002
# TAC = 0.99275350064608

# # out = td.TDCRPy(L, TD, TAB, TBC, TAC, "Co-60","1", 1000, 1e-5, 10, "res", "sym",barp=True)
# # out = opt.minimize_scalar(td.TDCRPy, args=(TD, TAB, TBC, TAC, "Co-60","1", 100, 1e-5, 10, "res", "sym"), method='golden', options={'disp': True, 'maxiter':20})
# # out = opt.minimize_scalar(td.TDCRPy, args=(TD, TAB, TBC, TAC, "Co-60","1", 100, 1e-5, 10, "res", "sym"), method='bounded', bounds = (0.5, 2), options={'disp': True, 'maxiter':20})
# out = eff(TD,TAB,TBC,TAC,"Co-60","1",1e-5,10,"sym",N=1000, L=3, maxiter=20)

# print(out)