"""Thermal Resistance Network Solver"""


"""
NOTES
-----
>> This code helps calculate total thermal resistances.

"""


def condR(L,k,A):
    R = L / (k*A)
    return R

def convR(h,A):
    R = 1 / (h*A)
    return R

def radR(e,A,T1,T2):
    sigma = 5.67*10**-8 # W/(m^2*K^4))
    R = 1 / (e * sigma * A * (T2+T1) * (T2**2 +T1**2))
    return R


resistances = []
temp_parallel_group = []

while True:
    print("Choose an Option:")
    print("1. Add parallel")
    print("2. Add next series")
    print("3. Done")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        n = int(input("Enter number of parallel paths: "))
        for i in range(n):
            temp_parallel_group.append(float(input(f"enter parallel resistance {i+1}: ")))
        resistances.append(1/sum(1/(temp_parallel_group[i]) for i in range(len(temp_parallel_group))))
        temp_parallel_group.clear()

    elif choice == "2":
        R = float(input("Enter resistance (C/W): "))
        resistances.append(R)

    elif choice == "3":
        Rtot = sum(resistances)
        break

print(Rtot)