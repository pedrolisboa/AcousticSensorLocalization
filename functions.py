import copy
import numpy as np

def get_error_magnitude(results, mp_pos):
    results_cp = copy.deepcopy(results)
    for scale in results:
        for method in results[scale]:
            results_cp[scale][method] = np.linalg.norm(results[scale][method] - np.transpose(mp_pos), 
                                                      ord=2, 
                                                      axis=0)
    return results_cp