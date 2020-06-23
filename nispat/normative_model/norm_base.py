from six import with_metaclass
from abc import ABCMeta, abstractmethod
import pickle

class NormBase(with_metaclass(ABCMeta)):
    """ Base class for normative model back-end.

        All normative modelling approaches must define the following methods::

            NormativeModel.estimate()
            NormativeModel.predict()
    """

    def __init__(self, x=None):
        pass

    @abstractmethod
    def estimate(self, X, y):
        """ Estimate the normative model """

    @abstractmethod
    def predict(self, Xs, X, y):
        """ Make predictions for new data """

    @property
    @abstractmethod
    def n_params(self):
        """ Report the number of parameters required by the model """
    
    def save(self, save_path):
        try:
            with open(save_path, 'wb') as handle:
                pickle.dump(self, handle, -1)
            return True
        except Exception as err:
            print('Error:', err)
            raise
    
    def load(self, load_path):
        try:
            with open(load_path, 'rb') as handle:
                nm = pickle.load(handle)
            return nm
        except Exception as err:
            print('Error:', err)
            raise
