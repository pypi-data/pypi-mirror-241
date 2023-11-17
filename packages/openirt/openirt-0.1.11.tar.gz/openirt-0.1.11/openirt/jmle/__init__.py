from pathlib import Path
import sys

if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))
from item_models import Model, PL1, PL2, PL3, Norm
import numpy as np
import jmle.pl1 as pl1
import jmle.pl2 as pl2
import jmle.pl3 as pl3


def estimate_ability_max_lik(
    model: Model, 
    params: np.ndarray, 
    results: np.ndarray,
    grid_density: int = 4,
    reg: float = 1e-2,
    bounds: tuple = (-8, 8),
    **kwargs: dict,
) -> np.ndarray:
    if isinstance(model, PL1):
        est_func = pl1.estimate_ability_max_lik
    elif isinstance(model, PL2):
        est_func = pl2.estimate_ability_max_lik
    elif isinstance(model, PL3):
        est_func = pl3.estimate_ability_max_lik
    else:
        raise NotImplementedError(
            "Cannot estimate ability using maximum liklihood estimation for given model."
        )
    # Regularization
    results = np.array(results).astype(float)
    results[results < reg] = reg
    results[results > 1 - reg] = 1 - reg
    
    # Grid
    init_grid = np.linspace(bounds[0], bounds[1], grid_density + 2)[1:-1]
    max_log_lik = -np.inf
    max_ability = None
    for ability in init_grid:
        temp_ability, temp_log_lik = est_func(model, params, results, ability, bounds, **kwargs)
        if temp_log_lik > max_log_lik:
            max_log_lik = temp_log_lik
            max_ability = temp_ability
    return max_ability


def estimate_item_params_max_lik(
    model: Model,
    ability: np.ndarray,
    result: np.ndarray,
    grid_density: int = 10,
    reg: float = 1e-2,
    **kwargs,
) -> np.ndarray:
    if isinstance(model, PL1):
        est_func = pl1.estimate_item_params_max_lik
    elif isinstance(model, PL2):
        est_func = pl2.estimate_item_params_max_lik  
    elif isinstance(model, PL3):
        est_func = pl3.estimate_item_params_max_lik
    else:
        raise NotImplementedError(
            "Cannot estimate parameters using maximum liklihood estimation for given model."
        )
    # Regularization
    result = np.array(result).astype(float)
    result[result < reg] = reg
    result[result > 1 - reg] = 1 - reg
    
    # Grid
    init_grid = model.init_grid(grid_density)
    max_log_lik = -np.inf
    max_params = None
    for params in init_grid:
        temp_params, temp_log_lik = (est_func(model, ability, result, params, **kwargs))
        if temp_log_lik > max_log_lik:
            max_log_lik = temp_log_lik
            max_params = temp_params
    return max_params

def jmle(
    model: Model,
    responses: np.ndarray,
    end: float = 0.1,
    max_iterations: int = 15,
) -> tuple:
    """
    Estimate abilities and item parameters using the EM algorithm with
    joint maximum liklihood estimation.

    Parameters
    ----------
        responses : np.ndarray
            Responses to items. Each row is a different subject, each
            column is a different item.
        end : float
            Convergence threshold.
        max_iterations : int, optional
            Maximum number of iterations. Defaults to 1000.

    Returns
    -------
        np.ndarray
            Estimated abilities
        np.ndarray
            Estimated item parameters. Each column is a different item,
            each row is a different parameter.
    """
    responses = np.array(responses)
    subjects, items = responses.shape
    
    abilities = np.sum(responses, axis=1)
    abilities = (abilities - np.mean(abilities)) / np.std(abilities)
    params = np.array(
        [
            estimate_item_params_max_lik(model, abilities, responses[:, i])
            for i in range(items)
        ]
    ).T
    
    log_lik = model.log_likelihood(abilities, params, responses)
    prev_log_log_lik = log_lik + 2 * end

    max_log_lik = -np.inf
    max_params = None
    max_abilities = None

    iteration = 0
    while abs(log_lik - prev_log_log_lik) > end and iteration < max_iterations:        
        abilities = np.array(
            [
                estimate_ability_max_lik(model, params, responses[j]) 
                for j in range(subjects)
            ]
        )
        
        # Normalize abilities
        abilities = (abilities - np.mean(abilities)) / np.std(abilities)
        
        params = np.array(
            [
                estimate_item_params_max_lik(model, abilities, responses[:, i])
                for i in range(items)
            ]
        ).T
        
        if log_lik > max_log_lik:
            max_log_lik = log_lik
            max_params = params
            max_abilities = abilities
        
        prev_log_log_lik = log_lik
        log_lik = model.log_likelihood(abilities, params, responses)
        iteration += 1
        
    return max_abilities, max_params