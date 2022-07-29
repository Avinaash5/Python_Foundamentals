m=3
A=[]
for i in range(m):
    n=input().split()
    A.append(n)

A_O_column=((A[0][0] =="O" and A[1][0] =="O" and A[2][0]=="O") or (A[0][1] =="O" and A[1][1] =="O" and A[2][1]=="O") or (A[0][2] =="O" and A[1][2] =="O" and A[2][2]=="O"))
A_X_column=((A[0][0] =="X" and A[1][0] =="X" and A[2][0]=="X")or (A[0][1] =="X" and A[1][1] =="X" and A[2][1]=="X") or (A[0][2] =="X" and A[1][2] =="X" and A[2][2]=="X"))
A_O_row=((A[0][0] =="O" and A[0][1] =="O" and A[0][2]=="O") or (A[1][0] =="O" and A[1][1] =="O" and A[1][2]=="O") or (A[2][0] =="O" and A[2][1] =="O" and A[2][2]=="O"))
A_X_row=((A[0][0] =="X" and A[0][1] =="X" and A[0][2]=="X") or (A[1][0] =="X" and A[1][1] =="X" and A[1][2]=="X") or (A[2][0] =="X" and A[2][1] =="X" and A[2][2]=="X"))
A_O_diagonal=((A[0][0] =="O" and A[1][1] =="O" and A[2][2]=="O") or (A[0][2] =="O" and A[1][1] =="O" and A[2][0]=="O"))
A_X_diagonal=((A[0][0] =="X" and A[1][1] =="X" and A[2][2]=="X") or (A[0][2] =="X" and A[1][1] =="X" and A[2][0]=="X"))

if A_O_column or A_O_row or A_O_diagonal:
    print("Player O Win")
elif A_X_column or A_X_row or A_X_diagonal:
    print("Player X Win")
else:
    print("Tie")
