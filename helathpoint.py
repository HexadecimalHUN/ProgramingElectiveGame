dem = int(input())
hp = 3
def hp_calc_first(dem, hp):
    hp = hp - dem
    return hp


result = hp_calc_first(dem, hp)
print(result)

dem = int(input())
def hp_calc_later(dem, result):
    result= result - dem
    return result

result=hp_calc_later(dem,result)
print(result)

dem = int(input())
result= hp_calc_later(dem,result)
print(result)