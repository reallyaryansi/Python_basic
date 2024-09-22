import random
import string

def encode(code):

    if len(code) >= 3:
        rd = "".join(random.choices(string.ascii_letters, k=3))

        encoded = rd + code[1:] + code[0] + rd
        print (f"The encoded code is{encoded} ")


    else:
        encoded = code[::-1]
        print(f"The encoded code is{encoded}")



# decoding secret code
def decoded(code):
    if (len(code) >= 3):
        decodehf = code[3:-3]
        decode = decodehf[-1] + decodehf[:-1]
        print(f"The decoded code is {decode}")
    else:
        decode = code[::-1]
        print(f"The decoded code is{ decode}")


# main part of the code

try:
    x = int(input(" Enter 1 for encode and 2 for decode : "))
    if x == 1:
        code = input("Enter a code to encode : ")
        encode(code)
    elif x == 2:
        code = input("Enter a code to decode: ")
        decoded(code)
    else:
        print("wrong answer print between 1 to 4 : ")

except ValueError:
    print(" invalid input! plz Enter a number ")






