"""Fourier's Law of Thermal Conductivity"""

# useful for validating the conduction through simple geometry

k = int(input("enter k (W/mC): "))
A = int(input("enter A (m^2): "))
L = int(input("enter L (m): "))
T1 = int(input("enter T1 (C): "))
T2 = int(input("enter T2 (C): "))

Q = k * A * ((T2-T1))/L

print(Q)