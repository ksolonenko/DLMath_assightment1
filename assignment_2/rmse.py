import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    # TODO: Implement RMSE Calculation here...
    rmse = np.sqrt(
        ((tar-pred)**2).mean()
        )
    return rmse