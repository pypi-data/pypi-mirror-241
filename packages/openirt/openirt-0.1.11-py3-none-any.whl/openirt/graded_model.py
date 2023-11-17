import numpy as np
from item_models import PL1, PL2, PL3
from scipy.stats import norm
import scipy.integrate as integrate
from scipy.optimize import minimize
import matplotlib.pyplot as plt


# mention: we assume there is some sort of location param.
# For graded models we must also assume icc is increasing, so we place bounds
class GradedModel:
    def __init__(
        self,
        models,
        categories,
    ) -> None:
        # loc_param asc is a list of booleans, corresponding to each item. The boolean is 'True' if a higher location
        # corresponds to a more difficult item.
        self.num_items = len(categories)
        self.categories = categories
        if type(models) != list:
            self.models = [models for _ in range(self.num_items)]
        else:    
            self.models = models

    def get_prov_params(self):
        prov_params = []
        for i, m in enumerate(self.models):
            if m.prov_params:
                prov_params.append(
                    np.tile(m.prov_params, (self.categories[i] - 1, 1)).T.astype(
                        float
                    )
                )

                # distribute location parameters (assuming bounds exist)
                lower_bound = m.param_bounds[m.loc_param][0]
                upper_bound = m.param_bounds[m.loc_param][1]
                if m.loc_param_asc:
                    prov_params[i][m.loc_param] = np.linspace(
                        lower_bound, upper_bound, self.categories[i] + 1
                    )[1:-1]
                else:
                    prov_params[i][m.loc_param] = np.linspace(
                        upper_bound, lower_bound, self.categories[i] + 1
                    )[1:-1]
            else:
                raise ValueError('"prov_params" is None')
        return prov_params

    def plot_boundaries(self, params, i):
        ability = np.linspace(-5, 5)
        for k, param in enumerate(params[i].T):
            prob = self.models[i].p(ability, param.reshape(self.models[i].num_params, 1)).reshape(-1)
            plt.plot(ability, prob, label=f"P*_{k}")
        plt.legend()
        plt.show()

    def plot_irccc(self, params, i):
        ability = np.linspace(-5, 5)
        for k in range(self.categories[i]):
            prob = [self.condit_prob_of_indiv_resp(params, k, i, ab) for ab in ability]
            plt.plot(ability, prob, label=f"P_{k}")
        plt.legend()
        plt.show()
        
    def get_expected_responses(self, params, abilities):
        ret = []
        for ability in abilities:
            ret_subj = []
            for i in range(self.num_items):
                expected_value = 0
                for resp in range(1, self.categories[i]):
                    expected_value += self.condit_prob_of_indiv_resp(params, resp, i, ability) * resp
                ret_subj.append(expected_value)
            ret.append(ret_subj)
        return np.array(ret)
     # P*_{i,k}(\theta)
    # 1 when k = -1
    # 0 when k = m-1 ?
    def boundary_prob(self, params, item, resp, ability):
        # resp is single resp
        if resp == -1:
            return 1
        if resp == self.categories[item] - 1:
            return 0
        temp_params = params[item][:, resp].reshape(self.models[item].num_params, 1)
        return self.models[item].p([ability], temp_params)[0][0]

    # P(U_{li}|\theta) = P(U_{li} = k|\theta) = P_{ik}(\theta) = P*_{i,k-1}(\theta) - P*_{ik}(\theta)
    def condit_prob_of_indiv_resp(self, params, resp, item, ability):
        # resp is single resp
        return max(
            self.boundary_prob(params, item, resp - 1, ability)
            - self.boundary_prob(params, item, resp, ability),
            1e-3,
        )

    # P(U_l|\theta) = \prod_{i=1}^n P(U_{li}|\theta)
    def condit_prob_of_subj_resp_vect(self, params, resp, ability):
        return np.prod(
            [
                self.condit_prob_of_indiv_resp(params, u, i, ability)
                for i, u in enumerate(resp)
            ]
        )
        
    def loc_param_bounds(self, params, item, param_type_idx, boundary_idx):
        # The domain of the location parameter is bounded by the adjacent location parameters
        model = self.models[item]
        tot_lower_bound = model.param_bounds[param_type_idx][0]
        tot_upper_bound = model.param_bounds[param_type_idx][1]
        if model.loc_param_asc:
            # lower bound
            if boundary_idx == 0:
                lower = tot_lower_bound
            else:
                lower = params[item][param_type_idx][boundary_idx - 1]
            # upper bound
            if boundary_idx == self.categories[item] - 2:
                upper = tot_upper_bound
            else:
                upper = params[item][param_type_idx][boundary_idx + 1]
        else:
            # lower bound
            if boundary_idx == self.categories[item] - 2:
                lower = tot_lower_bound
            else:
                lower = params[item][param_type_idx][boundary_idx + 1]
            # upper bound
            if boundary_idx == 0:
                upper = tot_upper_bound
            else:
                upper = params[item][param_type_idx][boundary_idx - 1]
        return lower, upper