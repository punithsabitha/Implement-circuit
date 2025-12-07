def circuit(A,B,C):
    G1=A&B
    G2=B|C
    G3=B&C
    G4=G2&G3
    return G1|G4

A=int(input("A: "))
B=int(input("B: "))
C=int(input("C: "))

Q=circuit(A,B,C)
print("Output Q =",Q)
