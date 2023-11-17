from model import Model
import numpy as np


class PL2(Model):
    """
    2-parameter logistic model (slope/intercept form).
    p(theta) = 1 / (1 + exp(-(zeta + lambda*theta))
    """

    def __init__(self):
        super().__init__(
            PL2.pl2_p,
            num_params=2,
            multi=True,
            prov_params=[0, 1],
            loc_param=0,
            param_bounds=((-10, 10), (0, 5)),
            loc_param_asc=False,
        )

    @staticmethod
    def pl2_p(ability: np.ndarray, params: np.ndarray) -> np.ndarray:
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
        items = np.array(params).shape[1]
        num_abilities = 1
        if np.array(ability).shape != ():
            num_abilities = np.array(ability).shape[0]
        ability = np.tile(np.array([ability]).transpose(), (1, items))

        params = np.tile(params, num_abilities).reshape((2, num_abilities, items))
        return 1 / (1 + np.exp(-params[0] - (params[1] * ability)))

    @staticmethod
    def convert_param_form(self, params):
        """
        Convert item parameters from one form to another. (Slope/intercept to
        alpha/beta, and vice versa)

        Args:
            params: A list or numpy array representing the item parameters.

        Returns:
            A numpy array representing the converted item parameters.
        """
        return np.array([-params[0] / params[1], 1 / params[1]])
