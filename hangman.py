import requests
import json
import sys
last_index_replaced = 0


def play_game():
    comleted_matrix = [
        [' ', '_', '_', '_', '_', '_', '_'],
        ['|', ' ', ' ', ' ', '|', ' ', ''],
        ['|', ' ', ' ', ' ', '0', ' ', ''],
        ['|', ' ', '-', '-', '|', '-', '-'],
        ['|', ' ', ' ', ' ', '|', ' ', ' '],
        ['|', ' ', ' ', '/', ' ', '\\', ' '],
        ['|', ' ', '/', ' ', ' ', ' ', '\\'],
    ]
    matrix_to_print = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ]

    def hang_the_man() -> bool:
        global last_index_replaced
        brk = False
        count = 0
        game_over = False
        for i, row in enumerate(comleted_matrix):
            for j, val in enumerate(row):
                count += 1
                if val != " ":
                    if last_index_replaced < count:
                        matrix_to_print[i][j] = val
                        last_index_replaced = count
                        brk = True
                        break

            if brk is True:
                if i == 6 and j == 6:
                    game_over = True
                break

        for i, row in enumerate(matrix_to_print):
            for j, val in enumerate(row):
                print(val, end="")
            print()

        if game_over:
            return True

        return False

    random_word = None
    is_game_over = False
    headers = {"ContentType": "application/json"}

    response = requests.get(
        "https://api.api-ninjas.com/v1/randomword?type=noun", headers=headers)

    if response.status_code == 200:
        data = json.loads(response.text)
        random_word = data.get("word")

    if not random_word:
        print("Someting went wrong. Please make sure you have working internet connection")

    random_word = random_word.lower()
    length = len(random_word)

    word_to_guess = ["_"] * length
    while 1:
        print("Please guess the word")
        for let in word_to_guess:
            print(let, end=" ")
        print()
        while 1:
            input_letter = input("Enter single letter. ")
            if len(input_letter) == 1:
                break

        if input_letter not in random_word:
            is_game_over = hang_the_man()
            if is_game_over:
                print("Game Over")
                while 1:
                    ans = input("Do you want to play again? (yes/no) ")
                    if ans == "yes":
                        global last_index_replaced
                        last_index_replaced = 0
                        play_game()
                    elif ans == "no":
                        print("Thank you for playing")
                        sys.exit()
                    else:
                        print("invalid input")

        for i, letter in enumerate(random_word):
            if letter == input_letter:
                word_to_guess[i] = letter

        if "_" not in word_to_guess:
            break

    if not is_game_over:
        print("".join(word_to_guess))
        print("Congrats you win")


play_game()
