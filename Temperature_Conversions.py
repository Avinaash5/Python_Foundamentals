n=input()
float_n=float(n[:-1])
last_character=n[-1:]
K=0.00
if last_character=="C":
    round_of_C=round(float_n,2)
    F=  (float_n*1.8)+32.0
    round_of_F=round(F,2)
    K=273.0+(float_n)
    round_of_K=round(K,2)
    print(str(round_of_C)+"C")
    print(str(round_of_F)+"F")
    print(str(round_of_K)+"K")
elif last_character=="F":
    round_of_F=round(float_n,2)
    C=(float_n-32.00)*(5/9)
    round_of_C=round(C,2)
    K=273.0+float(C)
    round_of_K=round(K,2)
    print(str(round_of_C)+"C")
    print(str(round_of_F)+"F")
    print(str(round_of_K)+"K")
elif last_character=="K":
    round_of_K=round(float_n,2)
    C=float_n-273.0
    round_of_C=round(C,2)
    F=  (C*1.8)+32.0
    round_of_F=round(F,2)
    print(str(round_of_C)+"C")
    print(str(round_of_F)+"F")
    print(str(round_of_K)+"K")
