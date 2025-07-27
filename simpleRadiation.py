"""Sefan-Boltzmann Law of Radiation"""

# useful for simplified radiation heat transfer

e = int(input("enter e: "))
sigma = 5.67*10**-8 # W/(m^2*K^4))
A = int(input("enter A (m^2): "))
T1 = int(input("enter T1 (C): "))
T2 = int(input("enter T2 (C): "))

Q = e * sigma * A * (T2**4 - T1**4)

print(Q)