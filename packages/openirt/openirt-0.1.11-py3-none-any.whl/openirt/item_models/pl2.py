from model import Model
import numpy as np


class PL2(Model):
    """
    2-parameter logistic model (a/b form).
    p(theta) = 1 / (1 + exp(-a(theta - b))
    """

    def __init__(self):
        super().__init__(
            PL2.pl2_p,
            num_params=2,
            multi=True,
            prov_params=[1,  0],
            loc_param=1,
            param_bounds=((-10, 10), (-4, 4)),
            loc_param_asc=True,
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
        
        exp = -params[0] * (ability - params[1])
        return 1 / (1 + np.exp(exp))
        
