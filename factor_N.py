import sys
from factordb.factordb import FactorDB
# Usage: python factor_N.py 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
#test n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
n = sys.argv[1]
def get_factor(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

p, q = get_factor(n)
print("p: %i" % p )
print("q: %i" % q )
