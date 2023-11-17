import numpy as np
from item_models import PL1, PL2, PL3
from scipy.stats import norm
import scipy.integrate as integrate
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from graded_model import GradedModel


# we assume there is some sort of location param.
# For graded models we must also assume icc is increasing, so we place bounds
class GradedMMLE:
    def __init__(
        self,
        graded_model,
        responses,
        response_count,
        ability_distr = None,
    ) -> None:
        # loc_param asc is a list of booleans, corresponding to each item. The boolean is 'True' if a higher location
        # corresponds to a more difficult item.
        # subj now refers to groups of subjects
        self.responses = responses
        self.num_subjects, self.num_items = responses.shape
        self.graded_model = graded_model
        self.response_count = response_count
        
        if ability_distr is None:
            self.ability_distr = lambda ability: norm.pdf(ability)
        else:
            self.ability_distr = ability_distr
        self.prov_params = graded_model.get_prov_params()

    # P(U_l) = \int P(U_l|\theta) \pi(\theta) d\theta
    def marginal_prob_of_resp(self, params, resp):
        integrand = lambda ability: self.graded_model.condit_prob_of_subj_resp_vect(
            params, resp, ability
        ) * self.ability_distr(ability)
        result, _ = integrate.quad(integrand, -7, 7, epsabs=1e-3, epsrel=1e-3)
        return result

    # L = \sum_{l=1}^{L} r_l \log{P(U_l)}
    def log_likelihood(self, params):
        marg_p = np.array(
            [self.marginal_prob_of_resp(params, resp) for resp in self.responses]
        )
        if np.any(marg_p <= 0):
            return -np.inf
        return np.sum(self.response_count * np.log(marg_p))

    def maximize_log_lik_loc(self, params, item, param_type_idx, boundary_idx):
        initial_guess = params[item][param_type_idx][boundary_idx]

        def obj_func(x):
            params[item][param_type_idx][boundary_idx] = x
            return -self.log_likelihood(params)

        result = minimize(
            obj_func,
            initial_guess,
            bounds=[self.graded_model.loc_param_bounds(params, item, param_type_idx, boundary_idx)],
            tol=1e-3,
        )
        return result.x[0], -result.fun

    def maximize_log_lik(self, params, item, param_type_idx):
        initial_guess = params[item][param_type_idx][0]

        def obj_func(x):
            params[item][param_type_idx] = x
            return -self.log_likelihood(params)

        result = minimize(
            obj_func,
            initial_guess,
            bounds=[self.graded_model.models[item].param_bounds[param_type_idx]],
            tol=1e-3,
        )
        return result.x[0], -result.fun

    def em_mmle(self, eps=0.5):
        params = self.prov_params.copy()
        prev_log_L = -np.inf
        log_L = self.log_likelihood(params)
        print(params)
        while abs(log_L - prev_log_L) > eps:
            print(params)
            print(f"prev log L: {prev_log_L}")
            print(f"log L: {log_L}")
            prev_log_L = log_L
            for i in range(len(params)):
                model = self.graded_model.models[i]
                # item_params are all parameters for item i
                for param_type_idx in range(model.num_params):
                    # param_type are the same type of parameters for i, e.g. all the betas
                    if param_type_idx == model.loc_param:
                        # optimize all location params separately
                        for k in range(self.graded_model.categories[i] - 1):
                            print(
                                f"maximizing item {i}, {param_type_idx}th parameter, where k={k}"
                            )
                            new_param, log_L = self.maximize_log_lik_loc(
                                params, i, param_type_idx, k
                            )
                    else:
                        print(
                            f"maximizing item {i}, {param_type_idx}th parameter, (all k)"
                        )
                        new_param, log_L = self.maximize_log_lik(
                            params, i, param_type_idx
                        )
        return params

    # \bar(\theta_l) = \frac{\int \theta P(U_l|\theta) \pi(\theta) d\theta}{P(U_l)}
    def estimate_ability_post_mean(self, params, subj):
        integrand = (
            lambda ability: self.graded_model.condit_prob_of_subj_resp_vect(
                params, self.responses[subj], ability
            )
            * self.ability_distr(ability)
            * ability
        )
        numer, _ = integrate.quad(integrand, -7, 7, epsabs=1e-3, epsrel=1e-3)
        denom = self.marginal_prob_of_resp(params, self.responses[subj])
        return numer / denom
    
    def estimate_abilities_post_mean(self, params):
        return np.array([self.estimate_ability_post_mean(params, group) for group in range(self.num_subjects)])
