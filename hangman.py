#imports
import random

#greeting
lost = 0
won = 0
while True:
    print("H A N G M A N")
    choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    if choice == "exit":
        break

    if choice == "results":
        print(f"You won: {won} times")
        print(f"You lost: {lost} times")

    if choice == "play":

        # create a list of words
        list_of_words = ["python", "swift", "java", "javascript"]

        #choose random word from list_of_words, enter input
        word = random.choice(list_of_words)
        covered_word = "-"*(len(word))
        original_word = word

        #looping the game
        life_counter = 8
        wrong_letters = []
        attempts = []
        print()

        while life_counter > 0:
            already_guessed = False
            print(covered_word)
            guessed_letter = input("Input a letter:")

            if (len(guessed_letter) == 1) and (guessed_letter in attempts) and (guessed_letter in "abcdefghijklmnopqrstuvwxyz"):
                print("You've already guessed this letter.")
                already_guessed = True

            attempts.append(guessed_letter)

            for j in range(len(word)):

                if already_guessed == True:
                    break

                if len(guessed_letter) != 1:
                    print("Please, input a single letter.")
                    break

                if guessed_letter.islower() == False:
                    print("Please, enter a lowercase letter from the English alphabet.")
                    break

                if guessed_letter == word[j]:
                    covered_word = covered_word[:j] + guessed_letter + covered_word[j+1:]

                    if covered_word == original_word:
                        print(original_word)
                        print(f"You guessed the word {original_word}!\nYou survived!")
                        life_counter = 0
                        won += 1
                        break

                elif guessed_letter not in word:
                    if guessed_letter not in wrong_letters and guessed_letter not in covered_word:
                        wrong_letters.append(guessed_letter)

                    elif guessed_letter in wrong_letters:
                        print("That letter doesn't appear in the word.")
                        life_counter -= 1
                        break

                if guessed_letter == word[j]:
                    word = word[:j] + "-" + word[j+1:]

        if life_counter == 0 and covered_word != original_word:
            print("You lost!")
            lost += 1
