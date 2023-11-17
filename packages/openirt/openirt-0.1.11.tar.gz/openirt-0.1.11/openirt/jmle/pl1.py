import numpy as np
from item_models import Model, PL1, PL2
from jmle.pl2 import estimate_ability_max_lik as pl2_estimate_ability_max_lik


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
    Estimate abilities using the maximum likelihood method.
    See Model.estimate_ability_max_lik and PL2.estimate_ability_max_lik.
    """
    return pl2_estimate_ability_max_lik(
        PL2(),
        [np.ones(len(params[0])), params[0]], results, 
        init, bounds, end, eps, max_iterations
    )


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
            Instance of PL1 model.
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
    
    est = model.prov_params[0]
    
    log_lik = model.log_likelihood(ability, [[est]], np.array([result]))
    prev_log_lik = log_lik + 2 * end
    
    iteration = 0
    while abs(log_lik - prev_log_lik) > end and iteration < max_iterations:
        P = PL1.pl1_p(ability, [[est]]).transpose()[0]
        L1 = np.sum(P - result)
        L2 = -np.sum(P * (1 - P))
        if abs(L2) < eps:
            L += 1e-10
            
        prev_log_lik = log_lik
        est = est - L1 / L2
        
        # enforce bounds
        out_of_bounds = False
        if est < model.param_bounds[0][0]:
            est = model.param_bounds[0][0]
            out_of_bounds = True
        if est > model.param_bounds[0][1]:
            est = model.param_bounds[0][1]
            out_of_bounds = True
            
        log_lik = model.log_likelihood(ability, [[est]], np.array([result]))
            
        if out_of_bounds:
            break
        iteration += 1
        
    return np.array([est]), log_lik
