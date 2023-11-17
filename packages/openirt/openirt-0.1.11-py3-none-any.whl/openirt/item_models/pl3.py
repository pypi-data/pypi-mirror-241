from model import Model
import numpy as np


class PL3(Model):
    """
    3-parameter logistic model ((a,b,c) form).
    p(theta) = c + (1-c) * (1 / (1 + exp(-a - b*theta))
    """

    def __init__(self):
        super().__init__(
            PL3.pl3_p,
            num_params=3,
            multi=True,
            prov_params=[1, 0, 0.01],
            loc_param=1,
            param_bounds=((-10, 10), (-4, 4), (1e-3, 0.3)),
            loc_param_asc=True,
        )

    @staticmethod
    def pl3_p(ability: np.ndarray, params: np.ndarray) -> np.ndarray:
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
        items = np.array(params).shape[1]
        num_abilities = 1
        if np.array(ability).shape != ():
            num_abilities = np.array(ability).shape[0]
        ability = np.tile(np.array([ability]).transpose(), (1, items))

        params = np.tile(params, num_abilities).reshape((3, num_abilities, items))
        return params[2] + (1 - params[2]) / (
            1 + np.exp(-params[0] * (ability - params[1]))
        )

    @staticmethod
    def pl2_p(ability: np.ndarray, params: np.ndarray) -> np.ndarray:
        """
        Calculate the probability of a correct response using the 2-parameter logistic model.
        This uses (a,b) form, unlike PL2.pl2_p().

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

        params = np.tile(params, num_abilities).reshape((3, num_abilities, items))
        return 1 / (1 + np.exp(-params[0] * (ability - params[1])))
