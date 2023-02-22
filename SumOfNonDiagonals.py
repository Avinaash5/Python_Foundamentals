def get_matrix(m):
    matrix=[]
    for i in range(m):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix

def get_total_sum_for_odd_m(matrix,m):
    total_sum=0
    for i in range(m):
        if((i==0)or (i==(m-1))):
            row_sum=sum(matrix[i][1:(m-1)])
            total_sum+=row_sum
        elif(i==(m//2)):
            row_sum=(sum(matrix[i])-matrix[i][i])
            total_sum+=row_sum
        else:
            j=m-(i+1)
            row_sum=(sum(matrix[i])-matrix[i][i]-matrix[i][j])
            total_sum+=row_sum
    return total_sum

def get_total_sum_for_even_m(matrix,m):
    total_sum=0
    k=int(m/2)
    for i in range(m):
        if((i==0)or (i==(m-1))):
            row_sum=sum(matrix[i][1:(m-1)])
            total_sum+=row_sum
        elif(i==(m//2) and (i!=k) and(i!=(k-1))):
            row_sum=(sum(matrix[i])-matrix[i][i])
            total_sum+=row_sum
        elif((i==k) or(i==(k-1))):
            if (i==k):
                row_sum=(sum(matrix[i])-matrix[i][i]-matrix[i][i-1])
            elif(i==(k-1)):
                row_sum=(sum(matrix[i])-matrix[i][i]-matrix[i][i+1])
            total_sum+=row_sum
        else:
            j=m-(i+1)
            row_sum=(sum(matrix[i])-matrix[i][i]-matrix[i][j])
            total_sum+=row_sum
    return total_sum

def get_sum_non_diagonals(matrix,m):
    if(m%2==1):
        total_sum=get_total_sum_for_odd_m(matrix,m)
    else:
        total_sum=get_total_sum_for_even_m(matrix,m)
    return total_sum
    

def main():
    m=int(input())
    matrix=get_matrix(m)
    result=get_sum_non_diagonals(matrix,m)
    print(result)

main()
