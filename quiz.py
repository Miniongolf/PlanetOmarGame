from random import choice, shuffle
from colorama import Fore


# Quiz = [[Question, Answer, [Option 1, Option 2, Option 3]],
# [Question, Answer, [Option 1, Option 2, Option 3]],
# [Question, Answer, [Option 1, Option 2, Option 3]]]

QandA = [["What country is Ottawa in?", "Canada", ["Canada", "USA", "France"]],
["What is the chemical equation of water?", "H2O", ["NaCl", "H2O", "Fl"]],
["What letter comes after A?", "B", ["D", "F", "B"]],
["What is 999^0?", "1", ["1", "999999999", "93638562847"]]]

clothingQuiz = [["What is one type of traditional clothing female Muslims wear?", "Hijab", ["Hijab", "Thobe", "Ghutra"]],
["What is one type of traditional clothing male Muslims wear?", "Ghutra", ["Ghutra", "Burqa", "Abaya"]],
["Why do Muslim women wear headscarves?", "There are varying reasons from person to person",["Maintain modesty", "Be more connected to the religion", "There are varying reasons from person to person"]]]

festivalsQuiz = [["During what festival do Muslims need to fast after sunrise to sunset?", "Ramadan", ["Ramadan", "Eid-ul-Fitr", "Al Hijra"]]]

def quiz(Quiz):
    letters = "abcdefghijklmnopqrstuvwxyz"

    Qnums = list(range(len(Quiz)))
    while len(Qnums) > 0:
        Qnum = choice(Qnums)
        question = Quiz[Qnum]
        print(question[0])
        shuffle(question[2])
        print(f"a) {question[2][0]}\nb) {question[2][1]}\nc) {question[2][2]}")
        response = input().lower()
        if response in letters:
            if letters.find(response) < 3:
                response = question[2][letters.find(response)].lower()
            else:
                print("Invalid answer. Please enter a number from 1-3 or a letter from a-c.")
        elif response.isnumeric():
            response = int(response) - 1
            if response < 3:
                response = question[2][response].lower()
            else:
                print("Invalid answer. Please enter a number from 1-3 or a letter from a-c")

        if response == Quiz[Qnum][1].lower():
            print(f"{Fore.LIGHTGREEN_EX}Correct!{Fore.RESET}")
            Qnums.remove(Qnum)
        else:
            print(f"{Fore.LIGHTRED_EX}Incorrect…{Fore.RESET}")

    print("Congratulations! You completed the quiz.")
