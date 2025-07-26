"""Newton's Law of Convection"""

"""
NOTES
-----
>> ueful for simple (estimated) convective heat transfer

>> natural convection of air ~1-10 W/m^2C

>> natural convection of water ~50-1000 W/m^2

>> refer to fluid, geometry, and heat load location for better approximations. (or the h-estimator)
"""

h = input("enter h value (W/m^2C): ")
A = input("enter A (m^2): ")
T1 = input("enter T1 (C): ")
T2 = input("enter T2 (C): ")

Q = h * A * (T2-T1)

print(Q)