import numpy as np
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
from splearn.linear_model import LogisticRegression
from splearn.utils.testing import SplearnTestCase, assert_array_almost_equal


class TestLogisticRegression(SplearnTestCase):

    def test_same_coefs(self):
        X, y, Z = self.make_classification(2, 10000)

        local = SklearnLogisticRegression(tol=1e-4, C=10)
        dist = LogisticRegression(tol=1e-4, C=10)

        local.fit(X, y)
        dist.fit(Z, classes=np.unique(y))

        assert_array_almost_equal(local.coef_, dist.coef_, decimal=1)
