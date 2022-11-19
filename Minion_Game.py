def minion_game(string):
    vowels=list('AEIOU')
    player1=0
    player2=0
    for char in range(len(string)):
        if string[char] in vowels:
            player2+= len(string) - char
        else:
            player1 += len(string) - char
    if player1>player2:
        print("player1 ",player1)
    elif player2>player1:
        print("player2 ",player2)
    else:
      print("Draw")
      
if __name__ == '__main__':
    s = input()
    minion_game(s)
