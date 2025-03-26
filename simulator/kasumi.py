
import numpy as np

def kasumi():
    is_omote = True
    num_energy = 0
    while is_omote:
        if np.random.rand() < 0.5:
            is_omote = False
        else:
            num_energy += 1
    
    return num_energy

