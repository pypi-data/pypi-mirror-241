import numpy as np
from item_models import PL2


def estimate_ability_max_lik(
    params: np.ndarray,
    results: np.ndarray,
    end=0.00000001,
    eps=0.01,
    eps2=0.000001,
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
        np.ndarray
            Array of abilities.
    """
    params = np.array(params)
    results = np.array(results)
    est = 0.5
    prev_est = 0
    while abs(est - prev_est) > end:
        P = PL2.pl2_p(est, params)[0]
        W = (1 - P) * P
        denom = np.sum(params[1] ** 2 * W)
        if abs(denom) < eps or np.any(np.abs(W) < eps2):
            print('break1')
            break
        prev_est = est
        est = est + (np.sum(params[1] * W * ((results - P) / W)) / denom)
    return est


def estimate_item_params_max_lik(
    ability: np.ndarray,
    result: np.ndarray,
    sigm_orig=-1,
    lamb_orig=1,
    end=0.00001,
    eps=0.0001,
) -> np.ndarray:
    """
    Estimate item parameters using maximum likelihood estimation.

    Parameters
    ----------
        ability : np.ndarray
            Array of abilities.
        result : np.ndarray
            Results. Each row is a different individual, each column is a
            different item.
        sigm_orig : float
            Initial value for the discrimination parameter.
        lamb_orig : float
            Initial value for the difficulty parameter.
        end : float
            Convergence threshold.
        eps : float
            Threshold for detecting a near-singular matrix.

    Returns
    -------
        np.ndarray
            Array of item parameters.
    """
    ability = np.array(ability)
    result = np.array(result)
    est = [sigm_orig, lamb_orig]
    prev_est = [0, 0]
    i = 0
    while abs(est[0] - prev_est[0]) > end or abs(est[1] - prev_est[1]) > end:
        P = PL2.pl2_p(ability, [[est[0]], [est[1]]]).transpose()[0]
        W = P * (1 - P)
        L11 = -np.sum(W)
        L12 = -np.sum(ability * W)
        L22 = -np.sum(ability**2 * W)
        L = np.array([[L11, L12], [L12, L22]])
        print(est)
        if abs(np.linalg.det(L)) < eps:
            # print(f'break2: {abs(np.linalg.det(L))}')
            # break
            L += np.identity(2) * 1e-6
        L_inv = np.linalg.inv(L)

        obs_mat = np.array([np.sum(result - P), np.sum((result - P) * ability)])
        prev_est = est
        est = est - np.matmul(L_inv, obs_mat)
        i += 1
        if i > 10000:
            break
    return est
