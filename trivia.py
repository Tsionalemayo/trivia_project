from classQuiz import Quiz

questions=["1.Who is the founder of Tech Career ?\n(a) Takele Mekonen \n(b) Usher Elias \n(c) Israel Mangisto \n(d) Asaf Avraham \n\n Enter your answer :",
           "2.What is capital city of Israel ?\n(a) Tel aviv \n(b) Jerusalem \n(c) Lod \n(d) Rishon Lezion \n\n Enter your answer :",
           "3.What is the color of the sun ?\n(a) orange \n(b) black \n(c) yellow \n(d) white \n\n Enter your answer :",
           "4.How many days are there in a year ?\n(a) 365 \n(b) 405 \n(c) 356 \n(d) 325 \n\n Enter your answer :",
            "5.What the highest building on the planet? ?\n(a) Burj Khalifa \n(b) Shanghai Tower \n(c) Abraj Al-Bait Clock Tower \n(d) empire state \n\n Enter your answer :",
            "6.which place is the deepest place on the planet ?\n(a) Dead Sea \n(b) Mariana Trench \n(c) Mount Everest \n(d) Lake-Lake Baikal \n\n Enter your answer :",
            "7.how long can human live without food ?\n(a) 8 to 21 days \n(b) 53 days \n(c) 7 days \n(d) 3 days \n\n Enter your answer :",
            "8.NASA’s most famous space telescope? ?\n(a) Humble Space Telescope \n(b) Galaxy Satellite Telescope \n(c) Muble Satellite Telescope \n(d) Hubble Space Telescope \n\n Enter your answer :",
            "9.How many colors are there in the rainbow? ?\n(a) 5 \n(b) 6 \n(c) 7 \n(d) 10 \n\n Enter your answer :",
            "10. Bonus Question!!!\nWhich country borders 14 nations and crosses 8 time zones? ?\n(a) israel \n(b) Germany \n(c) Russia \n(d) China \n\n Enter your answer :",
            ]



questions_answers=[
    Quiz(questions[0],"b"),
    Quiz(questions[1],"b"),
    Quiz(questions[2],"c"),
    Quiz(questions[3],"a"),
    Quiz(questions[4],"a"),
    Quiz(questions[5],"b"),
    Quiz(questions[6],"a"),
    Quiz(questions[7],"d"),
    Quiz(questions[8],"c"),
    Quiz(questions[9],"c")
]

## פונקציה שבודקת אם התשובה נכונה ומחשבת את הניקוד

def scoresSum(questions_answers):
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


#### שאלת בונוס (שאלה 10) יתווספו עוד 1000 נקודות ##
        if answer == i.answer and bonus == 10:
            score += 1000
    print("################################")
    print("Game over ! you got ",score,"score")
    print("you answered" ,correctanswer,"/10")
    print("################################")


scoresSum(questions_answers)

##fix later the 1000 bonus points allways added to the score.

