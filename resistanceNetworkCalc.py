"""Thermal Resistance Network Solver"""

from functions.heattransfer import * 

"""
NOTES
-----
>> Quickly build thermal resistance circuits and solve.

>> For reference, use the resistanceCalc.py to calculate indidual conductive, convective, and radiative resistances.

"""

while True:
    calculator = input("Solve Resistances (Y/N): ")
    if calculator == 'Y':
        resistance()
    elif calculator == 'N':
        break


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