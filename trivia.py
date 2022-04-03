from classQuiz import Quiz

questions=["1.What is capital city of is Israel ?\n(a) Tel aviv \n(b) Jerusalem \n(c) Lod \n(d) Rishon Lezion \n\n Enter your answer :",
           "2.What is the color of the sun ?\n(a) orange \n(b) black \n(c) yellow \n(d) white \n\n Enter your answer :",
           "3.Who is the founder of Tech Career ? \n(a) Takele Mekonen \n(b) Usher Elias \n(c) Israel Mangisto \n(d) Asaf Avraham \n\n Enter your answer :",
           "4.How many days are there in a year ? " ]

questions_answers=[
    Quiz(questions[0],"b"),
    Quiz(questions[1],"c"),
    Quiz(questions[2],"b")
]

## פונקציה שבודקת אם התשובה נכונה ומחשבת את הניקוד

def scoresSum(questions_answers):
    score=0
    counter=0
    for i in questions_answers:
        print("###########################")
        answer= input(i.question)
        counter+=1
        if counter == 2 :
            print("Total score round 1: ",score)
            counter=0
            print(counter)

        if answer == i.answer:
            score+=200
            print(" Correct answer ! :)")
        else:
            print("_______________________")
            print(" Worng answer :( \n The correct answer is : ", i.answer)

    # print("you got " ,score,"scores")

scoresSum(questions_answers)