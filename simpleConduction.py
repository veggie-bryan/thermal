"""Fourier's Law of Thermal Conductivity"""

# useful for validating the conduction through simple geometry

k = input("enter k (W/mC): ")
A = input("enter A (m^2): ")
L = input("enter L (m): ")
T1 = input("enter T1 (C): ")
T2 = input("enter T2 (C): ")

Q = k * A * ((T2-T1))/L

print(Q)

