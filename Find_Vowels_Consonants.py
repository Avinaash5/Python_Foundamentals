n = input()
n_no_spaces = n.replace(" ","") # here I am removing spaces
n_lower = n_no_spaces.lower() # then converting into lowercase
len_n=len(n_lower) # finding the length of the string
vowels = ("a,e,i,o,u")
vowel_count = 0
for char in n_lower:
    if char in vowels:
        vowel_count=vowel_count+1
print(vowel_count)
print(len_n-vowel_count)
