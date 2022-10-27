Capital_letters=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Small_letters=list('abcdefghijklmnopqrstuvwxyz')
sentence=input()
new_sentence=""
for char in sentence:
    if (char == " "):
        new_sentence+=" "
    elif (char in Capital_letters):
        index=Capital_letters.index(char)
        if index==0:
            index=27-1
            new_char=Capital_letters[index-1]
            new_sentence+=new_char
        else:
            index=index
            new_char=Capital_letters[index-1]
            new_sentence+=new_char
    elif (char in Small_letters):
        index=Small_letters.index(char)
        if index==0:
            index=27-1
            new_char=Small_letters[index-1]
            new_sentence+=new_char
        else:
            index=index
            new_char=Small_letters[index-1]
            new_sentence+=new_char
print(new_sentence)
