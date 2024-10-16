# import numpy as np
# from scipy.stats import ttest_ind

# # Generate two random normal distributions
# v1 = np.random.normal(size=100)
# v2 = np.random.normal(size=100)

# # Perform two-sample t-test
# res = ttest_ind(v1, v2)

# # Print the result
# print(res)


# 2 : kstest example
# import numpy as np
# from scipy.stats import kstest

# # Generate two random normal distributions
# v1 = np.random.normal(size=100)
# v2 = np.random.normal(size=100)


# res = kstest(v1, v2)


# print(res)

# 3 :  describe example  
import numpy as np
from scipy.stats import describe

# Generate two random normal distributions
v1 = np.random.normal(size=100)

res = describe(v1)
print(res)
