import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class Model:
    """
    Class for item response theory models, e.g. Pl1.
    """

    def __init__(
        self,
        p: callable,
        num_params: int,
        multi: bool = False,
        prov_params: list = None,
        loc_param: int = None,
        param_bounds: list = None,
        loc_param_asc: bool = True,
    ) -> None:
        """
        Initialize model.

        Parameters
        ----------
            p : callable
                Function that calculates the probability of a correct response
                given the ability and item parameters. For example,
                see pl1_p in pl1.py.
            num_params : int
                Number of item parameters. For example the PL3 models uses 3
                parameters: a, b, and c.
            multi : bool, optional
                True if p accepts an array of parameters, false if it accepts a
                single ability and parameters for a single item. Defaults to
                False.
            prov_params : list, optional
                Provisional item parameters, used when EM algorithm is
                initiated. Defaults to None.
            loc_param : int, optional
                Index of location parameter. For example, for the PL3 model
                with item parameters (a,b,c),
                b is the location parameter, so loc_param=1. Defaults to None.
            param_bounds : list, optional
                Minimum and maximum values for each item, for example
                [(0,1), (-5, 5)] for some model with num_params=2.
                Defaults to None.
            loc_param_asc : bool, optional
                True if a higher value for the location parameter results in an
                overall smaller probability of success. Defaults to True.
        """
        if multi:
            self.p = p
        else:
            self.p = lambda abilities, params: np.array(
                [[p(ability, param) for param in params.T] for ability in abilities]
            )
        self.num_params = num_params
        self.prov_params = prov_params
        self.loc_param = loc_param
        self.param_bounds = param_bounds
        self.loc_param_asc = loc_param_asc

    def plot_icc(
        self,
        params: np.ndarray,
    ):
        """
        Plot item characteristic curve for each item.

        Parameters
        ----------
            params : np.ndarray
                Item parameters. Each column is a different item, each row is a
                different parameter.
        """
        ability = np.linspace(-7, 7, 100)
        for i in range(params.shape[1]):
            plt.plot(
                ability,
                self.p(ability, params[:, i].reshape(params.shape[0], 1)),
                label=f"Question{i+1}",
            )
        plt.legend()
        if matplotlib.get_backend().lower() != 'agg':
            plt.show()

    def simulated_responses(
        self,
        abilities: np.ndarray,
        params: np.ndarray,
    ) -> np.ndarray:
        """Randomly generate responses given abilities and item parameters.

        Parameters
        ----------
            abilities (np.ndarray): Array of abilities.
            params (np.ndarray): Item parameters. Each column is a different item, each row is a different parameter.

        Returns
        -------
            np.ndarray
                Array of responses. Each row is a different subject, each column is a different item.
        """
        prob = self.p(abilities, params)
        return (np.random.rand(prob.shape[0], prob.shape[1]) < prob).astype(int)

    def log_likelihood(self, abilities, params, resp, eps=1e-8):
        """Log likelihood of responses given abilities and item parameters.
        
        Parameters
        ----------
            abilities (np.ndarray): Array of abilities.
            params (np.ndarray): Item parameters. Each column is a different item, each row is a different parameter.
            resp (np.ndarray): Array of responses. Each row is a different subject, each column is a different item.
            eps (float, optional): Threshold for small probabilities.
            
        Returns
        -------
            float
                Log likelihood of responses given abilities and item parameters.
        """
        P = self.p(abilities, params).flatten()
        P[P < eps] = eps
        P[P > 1 - eps] = 1 - eps
        Q = 1 - P
        resp = resp.flatten()
        return np.sum(np.log(P) * resp + np.log(Q) * (1 - resp))
    
    
    def init_grid(self, points_per_dim=10):
        """Grid of item parameters within bounds for initial estimates."""
        lspace = [np.linspace(self.param_bounds[i][0], self.param_bounds[i][1], points_per_dim + 2)[1:-1] for i in range(self.num_params)]
        grid = np.array(np.meshgrid(*lspace)).T.reshape(points_per_dim ** self.num_params, -1)
        return grid