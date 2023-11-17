from model import Model
import numpy as np
from scipy.stats import norm
from typing import Union


class Norm(Model):
    """
    Normal ogive model.
    """

    def __init__(self):
        super().__init__(
            Norm.norm_p,
            num_params=2,
            multi=True,
            prov_params=[0, 1],
            loc_param=0,
            param_bounds=((-10, 10), (-4, 4)),
            loc_param_asc=False,
        )

    @staticmethod
    def norm_p(
        ability: np.ndarray,
        params: np.ndarray,
    ) -> np.ndarray:
        """
        Calculate the probability of a correct response given the ability and
        item parameters.

        Parameters
        ----------
            ability : np.ndarray
                Array of abilities.
            params : np.ndarray
                Item parameters. Item parameters. Each column is a different
                item, each row is a different parameter.

        Returns
        -------
            np.ndarray
                Array of probabilities. Each row is a different individual,
                each column is a different item.
        """
        ability = np.array(ability)
        params = np.array(params)
        z = np.matmul(ability[:, np.newaxis], [params[1]])
        z += np.tile(params[0], (len(ability), 1))
        return norm.cdf(z)

    @staticmethod
    def norm_density(self, ability: np.ndarray, params: np.ndarray) -> np.ndarray:
        """
        Normal density function.
        """
        ability = np.array(ability)
        params = np.array(params)
        z = np.matmul(ability[:, np.newaxis], [params[1]])
        z += np.tile(params[0], (len(ability), 1))
        return norm.pdf(z)

    @staticmethod
    def convert_param_form(self, params):
        return np.array([-params[0] / params[1], 1 / params[1]])
