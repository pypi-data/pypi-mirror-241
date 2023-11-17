import numpy as np
from item_models import Model, PL3


def estimate_ability_max_lik(
    model: Model,
    params: np.ndarray,
    results: np.ndarray,
    init=0,
    bounds=(-10, 10),
    end=1e-5,
    eps=1e-10,
    max_iterations=100,
) -> np.ndarray:
    """
    Estimate abilities using maximum likelihood estimation.
    """    
    params = np.array(params)
    results = np.array(results)
    
    est = init
    log_lik = model.log_likelihood(np.array([est]), params, results)
    prev_log_lik = log_lik + 2 * end
    
    iteration = 0
    while np.abs(log_lik - prev_log_lik) > end and iteration < max_iterations:
        P = PL3.pl3_p(est, params)[0]
        Q = 1 - P
        
        P_2pm = PL3.pl2_p(est, params)[0]
        W = P * Q
        denom = -np.sum(params[0] ** 2 * W * (P_2pm / P) ** 2)
        num = np.sum(params[0] * W * ((results - P) / W) * (P_2pm / P))
        
        prev_log_lik = log_lik
        est = est - (num / denom)

        out_of_bounds = False
        if est < bounds[0]:
            est = bounds[0]
            out_of_bounds = True
        elif est > bounds[1]:
            est = bounds[1]
            out_of_bounds = True
        
        log_lik = model.log_likelihood(np.array([est]), params, results)
        if out_of_bounds:
            break
        iteration+=1
    return est, log_lik


def estimate_item_params_max_lik(
    model: Model,
    ability: np.ndarray,
    result: np.ndarray,
    prov_params: np.ndarray=None,
    end=1e-3,
    eps=1e-10,
    max_iterations=100,
) -> np.ndarray:
    """
    Estimate item parameters using maximum likelihood estimation.

    Parameters
    ----------
        model : Model
            Instance of PL3 model.
        ability : np.ndarray
            Array of abilities.
        result : np.ndarray
            Results. Each row is a different individual, each column is a
            different item.
        end : float
            Convergence threshold.
        eps : float
            Threshold for detecting a near-singular matrix.
        max_iterations : int
            Maximum number of iterations.

    Returns
    -------
        np.ndarray
            Array of item parameters.
    """
    if prov_params is None:
        prov_params = model.prov_params
        
    ability = np.array(ability)

    est = np.array(prov_params)
    params_temp = est.reshape((3, 1))
     
    log_lik = model.log_likelihood(ability, params_temp, np.array([result]))
    prev_log_lik = log_lik + 2 * end
    
    iteration = 0
    while np.abs(log_lik - prev_log_lik) > end and iteration < max_iterations:    
        P = PL3.pl3_p(ability, params_temp).T[0]
        if np.any(np.abs(P - est[2]) < eps) or np.any(np.abs(P) < eps):
            P = P + eps
        Q = 1 - P
        P_2pm = PL3.pl2_p(ability, params_temp).T[0]

        L11 = -np.sum((ability - est[1]) ** 2 * P * Q * (P_2pm / P) ** 2)
        L12 = np.sum(est[0] * (ability - est[1]) * P * Q * (P_2pm / P))
        L13 = -np.sum((ability - est[1]) * (Q / (1 - est[2])) * (P_2pm / P))
        L22 = -est[0] ** 2 * np.sum(P * Q * (P_2pm / P))
        L23 = np.sum(est[0] * (Q / (1 - est[2])) * (P_2pm / P))
        L33 = -np.sum((Q / (1 - est[2])) / (P - est[2]) * (P_2pm / P))
        L = np.array([[L11, L12, L13], [L12, L22, L23], [L13, L23, L33]])

        if abs(np.linalg.det(L)) < eps:
            L += np.identity(3) * 1e-10
        L_inv = np.linalg.inv(L)

        L1 = np.sum((result - P) * (ability - est[1]) * (P_2pm / P))
        L2 = -est[0] * np.sum((result - P) * (P_2pm / P))
        L3 = np.sum((result - P) / (P - est[2]) * (P_2pm / P))
        obs_mat = np.array([L1, L2, L3])
        
        prev_log_lik = log_lik
        est = est - np.matmul(L_inv, obs_mat)
        
        # enforce bounds
        out_of_bounds = False
        for par in range(model.num_params):
            if est[par] < model.param_bounds[par][0]:
                est[par] = model.param_bounds[par][0]
                out_of_bounds = True
            if est[par] > model.param_bounds[par][1]:
                est[par] = model.param_bounds[par][1]
                out_of_bounds = True
                
        params_temp = est.reshape((3, 1))
        log_lik = model.log_likelihood(ability, params_temp, np.array([result]))
        
        if out_of_bounds:
            break
        iteration += 1
    return est, log_lik
