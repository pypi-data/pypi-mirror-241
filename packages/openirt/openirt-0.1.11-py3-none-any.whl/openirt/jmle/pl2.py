import numpy as np
from item_models import Model, PL2, PL3


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

    Parameters
    ----------
        params : np.ndarray
            Item parameters. Each column is a different item, each row is
            a different parameter.
        results : np.ndarray
            Results. Each row is a different individual, each column is a
            different item.
        end : float
            Convergence threshold.
        eps : float
            Threshold for detecting a near-singular matrix.
        eps2 : float
            Threshold for detecting small values of P*Q.

    Returns
    -------
        int
            Estimated ability.
    """
    params = np.array(params)
    results = np.array(results)
    
    est = init
    log_lik = model.log_likelihood(np.array([est]), params, results)
    prev_log_lik = log_lik + 2 * end
    
    iteration = 0
    while np.abs(log_lik - prev_log_lik) > end and iteration < max_iterations:
        P = PL2.pl2_p(est, params)[0]
        Q = 1 - P
        
        W = P * Q
        if np.any(np.abs(W) < eps):
            W += eps

        denom = -np.sum(params[0] ** 2 * W)

        num = np.sum(params[0] * W * ((results - P) / W))
        
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

# def estimate_ability_max_lik(
#     model: Model,
#     params: np.ndarray,
#     results: np.ndarray,
#     init=0,
#     bounds=(-10, 10),
#     end=1e-5,
#     eps=1e-10,
#     max_iterations=100,
# ) -> np.ndarray:
#     """
#     Estimate abilities using the maximum likelihood method.
#     See Model.estimate_ability_max_lik and PL2.estimate_ability_max_lik.
#     """
#     return pl3_estimate_ability_max_lik(
#         PL3(),
#         [params[0], params[1], np.zeros(len(params[0]))], results, 
#         init, bounds, end, eps, max_iterations
#     )


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
            Instance of PL2 model.
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
    params_temp = np.array([[est[0]], [est[1]]])    
    
    log_lik = model.log_likelihood(ability, params_temp, np.array([result]))
    prev_log_lik = log_lik + 2 * end
    
    iteration = 0
    while np.abs(log_lik - prev_log_lik) > end and iteration < max_iterations:    
        P = PL2.pl2_p(ability, params_temp).T[0]
        W = P * (1 - P)
        lamb11 = -np.sum((ability - est[1]) ** 2 * W)
        lamb12 = est[0] * np.sum((ability - est[1]) * W)
        lamb22 = -np.sum(est[0] ** 2 * W)
        L = np.array([[lamb11, lamb12], [lamb12, lamb22]])
        if abs(np.linalg.det(L)) < eps:
            L += np.identity(2) * eps
        L_inv = np.linalg.inv(L)

        L1 = np.sum((result - P) * (ability - est[1]))
        L2 = np.sum((P - result) * est[0])
        obs_mat = np.array([L1, L2])

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
                
        params_temp = np.array([[est[0]], [est[1]]])
        log_lik = model.log_likelihood(ability, params_temp, np.array([result]))
        
        if out_of_bounds:
            break
        iteration += 1
        
    return est, log_lik
