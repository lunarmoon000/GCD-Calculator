import time

sleep_rate = 0.2

def larger_or_smaller(num1 :int, num2: int):
    output = []
    if (num1 > num2):
        output.append(num1)
        output.append(num2)
    elif (num2 > num1):
        output.append(num2)
        output.append(num1)
    return output

def gcd(num1 :int, num2: int) -> int:
    if(num1 == num2):
        print(1)
        return 1
    num_array = larger_or_smaller(num1, num2)
    larger = num_array[0]
    smaller = num_array[1]

    count = 0
    gcd = 0
    
    print("gcd(", larger, ",", smaller, ")\n")
    time.sleep(sleep_rate)
    
    while True:
        curr_quotient = larger // smaller
        remainder = larger%smaller
        print(larger, "/", smaller, "=", curr_quotient, "r", remainder)
        print("-"* 25)
        time.sleep(sleep_rate)
        if(remainder > 0):
            larger = smaller
            smaller = remainder
        else:
            gcd = smaller
            print("gcd =", gcd)
            time.sleep(sleep_rate)
            return gcd
        count += 1

print("Welcome to GCD Calculator\nWhat would you like to calculate?")
num1 = 1
num2 = 1
numbers_given = False
while True:
    thing = input("input two numbers separated by a comma, -1 to exit: ")
    if(thing == "-1"):
        print("\nGoodbye!\n")
        break
    thing_array = thing.split(",")
    if(len(thing) == 1 and thing[0].isdigit()):
        print("not enough arguments! please input two numbers!")
        continue
    try:
        num1 = int(thing_array[0])
        num2 = int(thing_array[1])
        if(num1 > 0 and num2 > 0):
            numbers_given = True
        break
    except:
        print("at least one of those is not a valid number! try again!")
if numbers_given:
    gcd(num1, num2)