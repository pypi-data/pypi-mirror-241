import numpy as np


def estimate_ability_max_lik(
    self,
    params: np.ndarray,
    results: np.ndarray,
    end=0.00000001,
    eps=0.01,
) -> np.ndarray:
    """
    Estimate abilities using maximum likelihood estimation.
    """
    est = 0.5
    prev_est = 0
    while abs(est - prev_est) > end:
        P = self.prob(est, params)[0]
        W = (1 - P) * P
        h = self.norm_density(est, params)[0]
        prev_est = est
        denom = np.sum(params[1] ** 2 * W)
        if denom < eps or np.any(W < eps):
            break
        est = est + (np.sum(params[1] * W * ((results - P) / h)) / denom)
    return est

def estimate_item_params_max_lik(
    self,
    ability: Union[list, np.ndarray],
    result: Union[list, np.ndarray],
    sigm_orig=0,
    lamb_orig=1,
    end=0.0000001,
    eps=0.1,
) -> np.ndarray:
    """
    Estimate item parameters using maximum likelihood estimation.
    """
    ability = np.array(ability)
    result = np.array(result)
    est = [sigm_orig, lamb_orig]
    prev_est = [0, 0]
    while abs(est[0] - prev_est[0]) > end or abs(est[1] - prev_est[1]) > end:
        P = self.prob(ability, [[est[0]], [est[1]]]).transpose()[0]
        h = self.norm_density(ability, [[est[0]], [est[1]]]).transpose()[0]
        W = h**2 / (P * (1 - P))
        L11 = -np.sum(W)
        L12 = -np.sum(ability * W)
        L22 = -np.sum(ability**2 * W)
        L = np.array([[L11, L12], [L12, L22]])

        if abs(np.linalg.det(L)) < eps:
            break
        L_inv = np.linalg.inv(L)

        v = (result - P) / h
        obs_mat = np.array([np.sum(W * v), np.sum(W * v * ability)])
        prev_est = est
        est = est - np.matmul(L_inv, obs_mat)
    return est
