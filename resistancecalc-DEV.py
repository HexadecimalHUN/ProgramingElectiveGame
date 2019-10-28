import random

resistor1 = random.randrange(1, 10, 1)
print("Resistor 1 =", resistor1)
resistor2 = random.randrange(1, 10, 1)
print("Resistor 2 =", resistor2)
resistor3 = random.randrange(1, 10, 1)
print("Resistor 3 =", resistor3)
end_result = 1
def resistor(resist_sum,resistor1, resistor2, resistor3):

    if resist_sum == resistor1 + resistor2 + resistor3:
        end_result = resist_sum
        return end_result
    else:
        exit(print("You failed"))
resist_sum= int(input())
end_result = resistor(resist_sum,resistor1, resistor2, resistor3)
if end_result == resistor(resist_sum,resistor1, resistor2, resistor3):
    print("You rock")
print(end_result)

voltage = random.randrange(20,100,1)
print("Now you have to calculate the Current rounded up or down as you learnt in high school, I now gave you the voltage: ", voltage)

guess_current = int(input())
val1=1

def current(guess_current,voltage, end_result):
    current_num = voltage // end_result
    if current_num == guess_current:
        return val1
    else:
        exit(print("you failed"))

val1 = current(guess_current,voltage, end_result)

val1 = (print("You rock again"))
