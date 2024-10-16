from scipy.optimize import differential_evolution

def global_object(x):
    return x [0] ** 2 + x[1] ** 2 

result = differential_evolution(global_object , [(-2 ,2) , (-2,2)] ) 
print("Global Optimization Solution:", result.x)
print("Global Minimal Value:", result.fun)
