from Crypto.Util.number import inverse, long_to_bytes #pip import pycryptodome
from factordb.factordb import FactorDB # pip import factordb-python

c = 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n = 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e = 65537  

# get p and q from factordb.com using N manually
#p = 
#q = 

# Calculate p and q using primefac
def get_factor(n):
    f = FactorDB(n)
    f.connect()
    return f.get_factor_list()

p, q = get_factor(n)

phi = ( p - 1 ) * ( q - 1 )

d = inverse( e, phi )

m = pow(c, d, n)
print( long_to_bytes(m) ) # long_to_bytes translates the solution to ascii for us
