###############################################################################
# Rapid equilibrium
###############################################################################


def equilibrium(S, P, keq):
    Total = S + P
    S = Total / (1 + keq)
    P = keq * Total / (1 + keq)
    return S, P
