n=int(input())
stars = "* "*(2*n)
print(stars)
#Upper part
spaces_count= 0
for i in range(1,n):
    stars = "* "*(n-i)
    spaces_count= spaces_count+2
    spaces="  "*spaces_count
    print(stars+spaces+stars)

#Lower part
spaces_count= spaces_count+2
for i in range(1,n):
    stars="* "*i
    spaces_count= spaces_count-2
    spaces="  "*spaces_count
    print(stars+spaces+stars)
    
stars = "* "*(2*n)
print(stars)
