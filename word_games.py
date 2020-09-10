# 3) The game of ghost is played by taking turns
#    with a partner to add a letter to an increasingly
#    long word. The first person to make a valid scrabble word
#    of length 3 or more loses.
#    You must be thinking of a valid word when you name a letter.
#    write a game that implements ghost
#    addendum: write a bot to play ghost against you.

# person inputs letter, letter is added to a word, if that word is a valid scrabble word

def get_scrabble_list():
    with open("scrabble.txt", 'r') as f:
        scrabble_list = []
        for word in f: 
            scrabble_list.append(word.strip('/n'))
    return scrabble_list

def main():
    scrabble_list = get_scrabble_list()
    game_word = ''
    count = 0
    while game_word not in scrabble_list:
        print('hello there')
        count += 1
        letter = input("Enter your letter: ")
        if len(letter)>1:
            print('nah')
            break
        game_word.join(letter)
        print(game_word)
    print("you lose")

main()