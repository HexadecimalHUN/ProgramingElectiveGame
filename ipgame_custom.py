from sys import argv
import random
from string import hexdigits
from ipaddress import IPv4Address
import re


def random_ip(seed):
    random.seed(seed)
    return str(IPv4Address(random.getrandbits(32)))


print ("Please calculate the subnet of the following ip:")
game_ip = (random_ip(seed=random))  # type: str
print(game_ip)

# dividing the ip
assert game_ip.count(".") == 3
ip_parts = game_ip.split(".")
ip_parts = [int(part) for part in ip_parts]
first, second, third, fourth = ip_parts

if first <= 128:    # Type A Address
    print("The IP is A type")
    cus_subn_mask = random.randrange(9, 32, 1)
    print (cus_subn_mask)
    upc = cus_subn_mask - 8
    if upc < 9:
        lst_num_sec = [int(i) for i in list('{0:08b}'.format(second))]
        print(upc)
        print(lst_num_sec)

    elif upc < 17:
        upc2 = 17-8
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]
        print (upc2)
        print(lst_num_third)

    elif upc < 25:
        upc3 = 25-16
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
        print (upc3)
        print (lst_num_fourth)


elif first <= 192:  # Type B Address
    print("The IP is B type")
    cus_subn_mask = random.randrange(17, 32, 1)
    print (cus_subn_mask)

    upc=cus_subn_mask-16

    if upc < 9:
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]
        print(upc)
        print (lst_num_third)

    elif upc < 17:
        upc2= 17-8
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
        print (upc2)
        print (lst_num_fourth)
elif first <= 255:  # Type C Address
    print("The IP is C type")
    cus_subn_mask = random.randrange(25, 32, 1)
    print (cus_subn_mask)
    lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
    upc=cus_subn_mask-24
    print (upc)
    print (lst_num_fourth)