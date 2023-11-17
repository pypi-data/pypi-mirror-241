from model import Model
import numpy as np
from pl2 import PL2


class PL1(Model):
    """
    1-Parameter logistic model (Rasch model).
    p(theta) = 1 / (1 + exp(-(zeta + theta))
    """

    def __init__(self):
        super().__init__(
            PL1.pl1_p,
            num_params=1,
            multi=True,
            prov_params=[0],
            loc_param=0,
            param_bounds=[(-4, 4)],
            loc_param_asc=True,
        )

    @staticmethod
    def pl1_p(ability: np.ndarray, params: np.ndarray) -> np.ndarray:
        """
        Probability of a correct response given the ability and item
        parameters.

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
        return PL2().pl2_p(ability, [np.ones(len(params[0])), params[0]])