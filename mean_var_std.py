import numpy as np
def calculate(L):
    if len(L)==9:
        l=np.array(L).reshape((3,3))
        m={'mean':[list(l.mean(axis=0)),list(l.mean(axis=1)),l.mean()],'variance':[list(l.var(axis=0)),list(l.var(axis=1)),l.var()],'standard deviation':[list(l.std(axis=0)),list(l.std(axis=1)),l.std()],'max':[list(l.max(axis=0)),list(l.max(axis=1)),l.max()],'min':[list(l.min(axis=0)),list(l.min(axis=1)),l.min()],'sum':[list(l.sum(axis=0)),list(l.sum(axis=1)),l.sum()]}
        return m
    elif len(L)<9:
        raise ValueError( "List must contain nine numbers." )
