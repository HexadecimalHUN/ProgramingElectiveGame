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
        unar_num=upc*"1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        #print (unar_num) #testing
        kgt = int(float(unar_num))
        print(unar_num,"help me") #testing
        a = int(unar_num,2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
        print (unar_num_lst)   #testing

        #now comes the comparison and segragation
        def seg1and0(arr,n):
            count = 0
            for i in range(0, n):
                if (arr[i]==1):
                    count = count +1
            for i in range(0,count):
                arr[i] = 1
            for i in range(count, n):
                arr[i]= 0
        def print_arr(arr, n):
            for i in range(1,n):
                print (arr[i],)
        n=len(unar_num_lst)
        seg1and0(unar_num_lst, n)
        print (unar_num_lst)



    elif upc < 17:
        upc2 = upc-8
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]
        print (upc2)
        print(lst_num_third)
        unar_num = upc2 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        # print (unar_num) #testing
        kgt = int(float(unar_num))
        print(unar_num, "help me")  # testing
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
        print (unar_num_lst)  # testing


        # now comes the comparison and segragation
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count ):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0


        def print_arr(arr, n):
            for i in range(1, n):
                print (arr[i],)


        n = len(unar_num_lst)
        seg1and0(unar_num_lst, n)
        print (unar_num_lst)

    elif upc < 25:
        upc3 = upc-16
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
        print (upc3)
        print (lst_num_fourth)
        unar_num = upc3 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        # print (unar_num) #testing
        kgt = int(float(unar_num))
        print(unar_num, "help me")  # testing
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
        print (unar_num_lst)  # testing


        # now comes the comparison and segragation
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0


        def print_arr(arr, n):
            for i in range(1, n):
                print (arr[i],)


        n = len(unar_num_lst)
        seg1and0(unar_num_lst, n)
        print (unar_num_lst)

        #modification
        #we must modify the specific charcaters from the list


elif first <= 192:  # Type B Address
    print("The IP is B type")
    cus_subn_mask = random.randrange(17, 32, 1)
    print (cus_subn_mask)

    upc=cus_subn_mask-16

    if upc < 9:
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]
        print(upc)
        print (lst_num_third)
        unar_num = upc * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        # print (unar_num) #testing
        kgt = int(float(unar_num))
        print(unar_num, "help me")  # testing
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
        print (unar_num_lst)  # testing


        # now comes the comparison and segragation
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count ):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0


        def print_arr(arr, n):
            for i in range(1, n):
                print (arr[i],)


        n = len(unar_num_lst)
        seg1and0(unar_num_lst, n)
        print (unar_num_lst)

    elif upc < 17:
        upc2= upc-8
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
        print (upc2)
        print (lst_num_fourth)
        unar_num = upc2 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        # print (unar_num) #testing
        kgt = int(float(unar_num))
        print(unar_num, "help me")  # testing
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
        print (unar_num_lst)  # testing


        # now comes the comparison and segragation
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0


        def print_arr(arr, n):
            for i in range(1, n):
                print (arr[i],)


        n = len(unar_num_lst)
        seg1and0(unar_num_lst, n)
        print (unar_num_lst)


elif first <= 255:  # Type C Address
    print("The IP is C type")
    cus_subn_mask = random.randrange(25, 32, 1)
    print (cus_subn_mask)
    lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
    upc=cus_subn_mask-24
    print (upc)
    print (lst_num_fourth)
    unar_num = upc * "1"
    ' '.join(format(ord(x), 'b') for x in unar_num)
    # print (unar_num) #testing
    kgt = int(float(unar_num))
    print(unar_num, "help me")  # testing
    a = int(unar_num, 2)
    unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]
    print (unar_num_lst)  # testing


    # now comes the comparison and segragation
    def seg1and0(arr, n):
        count = 0
        for i in range(0, n):
            if (arr[i] == 1):
                count = count + 1
        for i in range(0, count ):
            arr[i] = 1
        for i in range(count, n):
            arr[i] = 0


    def print_arr(arr, n):
        for i in range(1, n):
            print (arr[i],)


    n = len(unar_num_lst)
    seg1and0(unar_num_lst, n)
    print (unar_num_lst)
