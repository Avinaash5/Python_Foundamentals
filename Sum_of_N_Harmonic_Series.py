#Sum of harmonic series
n=int(input())
total=1
for i in range(2,n+1):
    harmonic_series = 1/i
    total =total+harmonic_series
total=round(total,2)
print(float(total))
