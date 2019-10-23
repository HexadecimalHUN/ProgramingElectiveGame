from sys import argv
import random
from string import hexdigits
from ipaddress import IPv4Address



def random_ip(seed):
    random.seed(seed)
    return str(IPv4Address(random.getrandbits(32)))


print ("Please calculate the subnet of the following ip:")

# IP Random generation
game_ip = (random_ip(seed=random))  # type: str
print(game_ip)

# Dividing the IP into four 8 bit sections
assert game_ip.count(".") == 3
ip_parts = game_ip.split(".")
ip_parts = [int(part) for part in ip_parts]
first, second, third, fourth = ip_parts



if first < 128:    # Type A Address
    # Generating a custom subnet mask
    cus_subn_mask = random.randrange(9, 32, 1)
    print (cus_subn_mask, "is the custom subnet mask")

    #Adding -8 all the time, because we doesn't wana to deal with the first 8 bit of the IP
    upc = cus_subn_mask - 8

    #If the subnet mask is 8 or less character long belongs to here
    if upc < 9:
        # Casting binear from the IP-s important section
        lst_num_sec = [int(j) for j in list('{0:08b}'.format(second))]

        # Making a fake unary format from the Custom subnet mask
        unar_num=upc*"1"
        ' '.join(format(ord(x), 'b') for x in unar_num)

        #Filling up a list from the custom subnet mask in fake 8 bit binary
        kgt = int(float(unar_num))
        a = int(unar_num,2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

        #Now doing some neat segragation
        #Fillig up a list in reverse from the fake binary list
        def seg1and0(arr,n):
            count = 0
            for i in range(0, n):
                if (arr[i]==1):
                    count = count +1
            for i in range(0,count):
                arr[i] = 1
            for i in range(count, n):
                arr[i]= 0
            return arr

        #Using the function in the field
        n=len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)


        # The actual comparison part
        if unar_num_lst_rev[0] == 0:
            lst_num_sec[0] = 0
        if unar_num_lst_rev[1] == 0:
            lst_num_sec[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_sec[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_sec[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_sec[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_sec[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_sec[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_sec[7] = 1

        #Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_sec)

        #Generating a decimal number from the binary
        masked_ip_dec = int(masked_ip_bin, 2) 


        print("So guys we did it, the ip is the following:", first, masked_ip_dec, "0","0")


    elif upc < 17:
        # Adding -8 all the time, because we doesn't wana to deal with the first and the second 8 bit of the IP
        upc2 = upc-8

        # Casting binear from the IP-s important section
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]

        # Making a fake unary format from the Custom subnet mask
        unar_num = upc2 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)

        # Filling up a list from the custom subnet mask in fake 8 bit binary
        kgt = int(float(unar_num))
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

        # Now doing some neat segragation
        # Filling up a list in reverse from the fake binary list
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count ):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0
            return arr


        #Using the function in the field
        n = len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)


        # The actual comparison part
        if unar_num_lst_rev[0] == 0:
            lst_num_third[0] = 0
        if unar_num_lst_rev[1] ==0:
            lst_num_third[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_third[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_third[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_third[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_third[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_third[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_third[7] = 0

        # Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_third)

        # Generating a decimal number from the binary
        masked_ip_dec = int(masked_ip_bin, 2) -1

        print("So guys we did it, the ip is the following:", first,second,masked_ip_dec,"0")

    elif upc < 25:

        # Adding -8 all the time, because we doesn't wana to deal with the first and the second and the third 8 bit of the IP
        upc3 = upc-16

        # Casting binear from the IP-s important section
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]

        # Making a fake unary format from the Custom subnet mask
        unar_num = upc3 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        kgt = int(float(unar_num))

        # Filling up a list from the custom subnet mask in fake 8 bit binary
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]

        # Now doing some neat segragation
        # Filling up a list in reverse from the fake binary list
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0
            return arr

        #Using the function in the field
        n = len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)


        # The actual comparison part
        if unar_num_lst_rev[0] == 0:
            lst_num_fourth[0] = 0
        if unar_num_lst_rev[1] == 0:
            lst_num_fourth[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_fourth[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_fourth[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_fourth[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_fourth[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_fourth[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_fourth[7] = 0

        #Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

        masked_ip_dec = int(masked_ip_bin, 2)

        print("So guys we did it, the ip is the following:", first,second,third, masked_ip_dec)

elif first < 192:  # Type B Address

    # Generating a custom subnet mask
    cus_subn_mask = random.randrange(17, 32, 1)
    print (cus_subn_mask, "is the custom subnet mask")

    # Adding -16 all the time, because we doesn't wana to deal with the first 16 bit of the IP
    upc = cus_subn_mask-16

    if upc < 9:
        # Casting binear from the IP-s important section
        lst_num_third = [int(i) for i in list('{0:08b}'.format(third))]

        # Making a fake unary format from the Custom subnet mask
        unar_num = upc * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        kgt = int(float(unar_num))

        # Filling up a list from the custom subnet mask in fake 8 bit binary
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]


        #Now doing some neat segragation
        #Fillig up a list in reverse from the fake binary list
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count ):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0
            return arr


        #Using the function in the field
        n = len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)


        # The actual comparison part

        if unar_num_lst_rev[0] == 0:
            lst_num_third[0] = 0
        if unar_num_lst_rev[1] == 0:
            lst_num_third[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_third[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_third[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_third[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_third[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_third[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_third[7] = 0

        #Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_third)

        # Generating a decimal number from the binary
        masked_ip_dec = int(masked_ip_bin, 2) -1

        print("So guys we did it, the ip is the following:", first,second, masked_ip_dec,"0")


    elif upc < 17:

        # Adding -8 all the time, because we doesn't wana to deal with the first 8 bit of the IP
        upc2= upc-8

        # Casting binear from the IP-s important section
        lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]

        # Making a fake unary format from the Custom subnet mask
        unar_num = upc2 * "1"
        ' '.join(format(ord(x), 'b') for x in unar_num)
        kgt = int(float(unar_num))

        # Filling up a list from the custom subnet mask in fake 8 bit binary
        a = int(unar_num, 2)
        unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]



        #Now doing some neat segragation
        #Fillig up a list in reverse from the fake binary list
        def seg1and0(arr, n):
            count = 0
            for i in range(0, n):
                if (arr[i] == 1):
                    count = count + 1
            for i in range(0, count):
                arr[i] = 1
            for i in range(count, n):
                arr[i] = 0
            return arr



        #Using the function in the field
        n = len(unar_num_lst)
        unar_num_lst_rev = seg1and0(unar_num_lst, n)


        # The actual comparison part
        if unar_num_lst_rev[0] == 0:
            lst_num_fourth[0] = 0
        if unar_num_lst_rev[1] == 0:
            lst_num_fourth[1] = 0
        if unar_num_lst_rev[2] == 0:
            lst_num_fourth[2] = 0
        if unar_num_lst_rev[3] == 0:
            lst_num_fourth[3] = 0
        if unar_num_lst_rev[4] == 0:
            lst_num_fourth[4] = 0
        if unar_num_lst_rev[5] == 0:
            lst_num_fourth[5] = 0
        if unar_num_lst_rev[6] == 0:
            lst_num_fourth[6] = 0
        if unar_num_lst_rev[7] == 0:
            lst_num_fourth[7] = 0

        #Generating a binear number from the list
        masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

        # Generating a decimal number from the binary
        masked_ip_dec = int(masked_ip_bin, 2)

        print("So guys we did it, the ip is the following:", first,second,third, masked_ip_dec)



elif first < 256:  # Type C Address

    # Generating Custom subnet
    cus_subn_mask = random.randrange(25, 32, 1)
    print (cus_subn_mask, "is the custom subnet mask")

    # Casting binear from the IP-s important section
    lst_num_fourth = [int(i) for i in list('{0:08b}'.format(fourth))]
    # Adding -24, because we doesn't wana to deal with the first 24 bit of the IP
    upc=cus_subn_mask-24

    # Making a fake unary format from the Custom subnet mask
    unar_num = upc * "1"
    ' '.join(format(ord(x), 'b') for x in unar_num)
    kgt = int(float(unar_num))

    # Filling up a list from the custom subnet mask in fake 8 bit binary
    a = int(unar_num, 2)
    unar_num_lst = [int(i) for i in list('{0:08b}'.format(a))]


    # Now doing some neat segragation
    # Fillig up a list in reverse from the fake binary list
    def seg1and0(arr, n):
        count = 0
        for i in range(0, n):
            if(arr[i] == 1):
                count = count + 1
        for i in range(0, count ):
            arr[i] = 1
        for i in range(count, n):
            arr[i] = 0
        return arr

    #Using the function in the field
    n = len(unar_num_lst)
    unar_num_lst_rev = seg1and0(unar_num_lst, n)

    # The actual comparison part
    if unar_num_lst_rev[0] == 0:
        lst_num_fourth[0] = 0
    if unar_num_lst_rev[1] == 0:
        lst_num_fourth[1] = 0
    if unar_num_lst_rev[2] == 0:
        lst_num_fourth[2] = 0
    if unar_num_lst_rev[3] == 0:
        lst_num_fourth[3] = 0
    if unar_num_lst_rev[4] == 0:
        lst_num_fourth[4] = 0
    if unar_num_lst_rev[5] == 0:
        lst_num_fourth[5] = 0
    if unar_num_lst_rev[6] == 0:
        lst_num_fourth[6] = 0
    if unar_num_lst_rev[7] == 0:
        lst_num_fourth[7] = 0

    #Generating a binear number from the list
    masked_ip_bin = ''.join(str(e) for e in lst_num_fourth)

    # Generating a decimal number from the binary
    masked_ip_dec = int(masked_ip_bin, 2)

    print("So guys we did it, the ip is the following:", first,second,third, masked_ip_dec)
