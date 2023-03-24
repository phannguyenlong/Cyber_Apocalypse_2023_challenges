from sage.all_cmdline import *
cipher_arr = [(25, 25, 11, 28, 11), (27, 21, 22, 13, 14), (6, 0, 22, 11, 25), (20, 19, 7, 8, 17), (21, 0, 17, 11, 11)]
key_arr = [(17, 22, 7, 2, 15), (21, 6, 20, 18, 1), (27, 3, 6, 26, 0), (7, 27, 6, 19, 19), (12, 9, 11, 25, 23)]

# 72 84 66 123 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 63 125

list_prime = [17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
list_ascii = [72,84,66,123,49,50,51,52,53,54,55,56,57,48,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,95,113,114,115,116,117,118,119,120,121,122,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,64,33,125]
message = [(4, 16, 15, 4, 12), (12, 12, 12, 12, 12), (12, 12, 12, 12, 12), (12, 12, 12, 12, 12), (12, 12, 12, 12, 6)]

test = [(3,4,3),(3,3,3)]

def find(res):
    for x in range(0, 5):
        for y in range(0, 5):
            index = 0
            temp = ""
            for i in range(0, len(list_ascii)):
                if (list_ascii[i] % prime == res[x][y]):
                    # print(str(list_ascii[i]) + ":" + str(res[x][y]))
                    if (string[index] == "" and index !=0):
                        string[index] = string[index-1]
                    string[0] += str(list_ascii[i]) + " "
                    index += 1
                    temp += chr(list_ascii[i]) + " : "
                    if (index >= 1):
                        temp += chr(list_ascii[i]) + " : "
            print(temp)
        print("====================")

    for i in range(0, len(string)):
        print(string[i])

for t in range(0, len(list_prime)):
    prime = list_prime[t]
    cipher = matrix(GF(prime), 5,5, cipher_arr)
    key = matrix(GF(prime), 5,5, key_arr)
    # message = matrix(GF(prime), 5,5, message)

    res = matrix(GF(23),5,5)
    try:
        res = cipher * key.inverse()
    except:
        continue
    
    if ((72 % prime == res[0][0]) and (84 % prime == res[0][1]) and (66 % prime == res[0][2])):
        print(res)
        res = list(res)
        print(res)
        print("Prime: " + str(prime))
        find(res)
    string = ["","","","",""]