import random

score=0
questions = {}
passed = False

print ("Hello to the Math game! \nHere you will get 10 math problems to solve. \nSolve at least 8 to proceed")
for i in range(10):
    int_a = random.randint(10, 20)
    int_b = random.randint(1, 9)
    operators = ['+','-','*','//']
    operator_value = random.choice(operators)
    question = str(int_a)+" "+operator_value+" "+str(int_b)
    answer = str(eval(question))
    question+=": "
    questions.update({question:answer})

for q in questions.keys():
    user_answer=input(q)
    if questions.get(q)==user_answer:
        print("Correct!")
        score+=1
    else:
        print("You're Wrong!")
print("You have "+str(score)+" points!")

if score < 8:
    print ("You lose!")
else:
    passed = True
    print ("You won!")

    
