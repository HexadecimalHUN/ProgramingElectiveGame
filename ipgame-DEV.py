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

if first <= 128:
    print("The IP is A type")
    # default netmask for type A is 255.0.0.0 -> Just the first section gona be modified
    masked_ip = 255, second, third, fourth
    print(masked_ip)
elif first <= 192:
    print("The IP is B type")
    # default netmask for type B is 255.255.0.0 -> First and second section gona be modified
    masked_ip = 255, 255, third, fourth
    print(masked_ip)
elif first <= 255:
    print("The IP is C type")
    # default netmask for type C is 255.255.255.0 -> First second and third section gona be modified
    masked_ip = 255, 255, 255, fourth
    print(masked_ip)
