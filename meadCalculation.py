# These librairie provide the different calcul that can be useful for Mead production

def calculate_honey(V:float, Cv:float, Cm:float):
    #M = V * (24.5 * Cv + Cm)
    return V * (24.5 * Cv + Cm)

def calculate_alcool_brix(Bi:float, Bf:float):
    #ABV = (Bi - Bf) * 0.59
    return (Bi - Bf) * 0.59

def calculate_alcool_density(df:float, di:float):
    #ABV = (di - df) * 131.25
    return (di - df) * 131.25
