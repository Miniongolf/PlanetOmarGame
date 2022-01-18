from random import choice, shuffle
from colorama import Fore

QandA = [["What country is Ottawa in?", "Canada", ["Canada", "USA", "France"]],
["What is the chemical equation of water?", "H2O", ["NaCl", "H2O", "Fl"]],
["What letter comes after A?", "B", ["D", "F", "B"]],
["What is 999^0?", "1", ["1", "999999999", "93638562847"]]]

locationQuiz = [["Where do Muslims live?", "All around the world", ["All around the world", "Only in Asia", "Only in the Middle East"]],
["How many gods do Muslims worship", "One", ["One", "Two", "Five"]]]

foodQuiz = [["What food category can Muslims eat?", "Halal", ["Halal", "Kosher", "Vegan"]],
["What type of meat can Muslims not eat due to religious reasons?", "Pork", ["Pork", "Chicken", "Lamb"]],
["Why do Muslims only eat Halal food", "To follow their God's rules", ["To follow their God's rules", "It tastes better", "For fun"]]]

clothingQuiz = [["What is one type of traditional clothing female Muslims wear?", "Hijab", ["Hijab", "Turban", "Blazer"]], ["What is one type of traditional clothing male Muslims wear?", "Ghutra", ["Ghutra", "Hijab", "Cap"]],
["Why do Muslim women wear headscarves?", "To respect their religion",["To respect their religion", "For fun", "It looks pretty"]]]

festivalsQuiz = [["During what festival do Muslims need to fast after sunrise to sunset?", "Ramadan", ["Ramadan", "Eid-ul-Fitr", "Al Hijra"]]]

def quiz(Quiz, points, last=False):
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
                print("Invalid answer. Please enter a letter from a-c.")
        elif response.isnumeric():
            response = int(response) - 1
            if response < 3:
                response = question[2][response].lower()
            else:
                print("Invalid answer. Please enter letter from a-c")

        if response == Quiz[Qnum][1].lower():
            print(f"{Fore.LIGHTGREEN_EX}Correct!{Fore.RESET}")
            Qnums.remove(Qnum)
            points += 6
        else:
            print(f"{Fore.LIGHTRED_EX}Incorrect…{Fore.RESET}")
            points -= 1

    if last == False:
        print("Congratulations! You completed the quiz. Now press Enter to go to the next maze.")
        input()
    return points
