dem = int(input())
hp = 3
#should be the first damage
def hp_calc_first(dem, hp):
    hp = hp - dem
    return hp

#usage damage
result = hp_calc_first(dem, hp)
print(result)

dem = int(input())

#after first damage

def hp_calc_later(dem, result):
    result= result - dem
    if result == 0:
      exit(print("You are dead"))
    return result

result=hp_calc_later(dem,result)
print(result)

dem = int(input())
result= hp_calc_later(dem,result)
print(result)

#heal function
heal = int(input())
def potion(heal, result):
    result=result + heal
    return result

#usage heal
result= potion(heal, result)
print(result)
