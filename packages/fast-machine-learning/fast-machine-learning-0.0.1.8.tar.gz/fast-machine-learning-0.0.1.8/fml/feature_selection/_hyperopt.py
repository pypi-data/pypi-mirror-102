
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
if __name__ == "__main__":
    from fml.validates import validate_switch
else:
    from ..validates import validate_switch
import numpy as np

def single_hyperopt(X, Y, algo, flen, loo=10):
    
    featurespace = {}
    for fl in range(flen):
        featurespace.update({str(fl): hp.randint(str(fl), X.shape[1])})
    
    trials = Trials()
    
    def f(params):
        print(params)
        result = validate_switch(loo, algo, X[:, np.array(list(params.values()))], Y)
        if len(set(Y)) > 8:
            loss = result["rmse"]
        else:
            loss = 1 / result["accuracy_score"] + 0.0000001
        return {'loss': loss, 'status': STATUS_OK}

    best = fmin(fn=f, space=featurespace, algo=tpe.suggest, max_evals=100, trials=trials)

    return best, f(best)["loss"]


if __name__ == "__main__":
    from sklearn.datasets import load_boston
    import xgboost; algo = xgboost.XGBRegressor
    dataset = load_boston()
    X = dataset.data
    Y = dataset.target
    
    best, loss = single_hyperopt(X, Y, algo, 5, 10)