import numpy as np
from scipy import constants, special

result_addition = np.add(5, 3)
result_exponential = np.exp(2)

result_bessal = special.jn(2, 3)

print("Addition:", result_addition)
print("Exponential:", result_exponential)
print("Bessel function result:", result_bessal)
