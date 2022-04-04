
## פונקציה שבודקת אם התשובה נכונה ומחשבת את הניקוד

def triviaGame(questions_answers):
    score=0
    counter=0
    bonus = 0
    correctanswer = 0
    print("Welcome to Eli and Tsiona's trivia game :) ")
    for i in questions_answers:
        print("################################")
        answer= input(i.question)
        #  השאלה תחזור על עצמה כל עוד המשתמש לא בחר אחת מהאופציות!
        while answer not in ("a", "b", "c", "d"):
            print("------------------------------------")
            print("To procced to the next question.. \nYou need to select an answer from the available options : (a,b,c,d) ")
            print("------------------------------------")
            answer = input(i.question)

        counter+=1
        bonus+=1

        if answer == i.answer:
            score+=200
            correctanswer += 1
            print(" Correct answer ! :)")
        else:
            print("_______________________________")
            print(" Worng answer :( \n The correct answer is : ", i.answer)


#### לאחר כל סבב (3 שאלות) יופיע כמה נקודות יש עד כה ##
        if counter == 3:
            print("Total score : ", score)
            counter = 0

    score = calcBonus(answer,bonus,i,score)


    print("#################################")
    print("\nGame over ! \nyou got ",score,"score")
    print("Correct answers: " ,correctanswer,"/", len(questions_answers))
    print("\n################################")


#### שאלת בונוס (שאלה 10) יתווספו עוד 1000 נקודות ##
def calcBonus(answer,bonus,i,score):
    if answer == i.answer and bonus == 10:
        score += 1000
    return score




