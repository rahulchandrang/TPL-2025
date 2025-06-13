def set_random_seed(seed):
    import random
    import numpy as np
    import torch

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def log_metrics(metrics, log_file='metrics.log'):
    with open(log_file, 'a') as f:
        for key, value in metrics.items():
            f.write(f"{key}: {value}\n")