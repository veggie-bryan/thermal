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

while True:
    print("Enter Resistance Type:")
    print("1. Conductive")
    print("2. Convective")
    print("3. Radiative")
    
    choice = int(input("enter 1, 2, or 3: "))

    if choice == 1:
        k = int(input("enter k (W/mC): "))
        A = int(input("enter A (m^2): "))
        L = int(input("enter L (m): "))
        R = condR(k,A,L)
        print(R)

    
    if choice == 2:
        h = int(input("enter h value (W/m^2C): "))
        A = int(input("enter A (m^2): "))
        R = convR(h,A)
        print(R)

    if choice == 3:
        e = int(input("enter e: "))
        A = int(input("enter A (m^2): "))
        T1 = int(input("enter T1 estimate(C): "))
        T2 = int(input("enter T2 estimate(C): "))
        R = radR(e,A,T1,T2)
        print(R)

