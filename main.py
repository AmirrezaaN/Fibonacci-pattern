number1 = 1
number2 = 1
number = 0
pattern_number = int(input("[INPUT] How many numbers of the Fibonacci pattern do you want :"))

print("0,1,1",end=",")
for i in range(pattern_number-3):
    number=number1+number2
    print(number,end=",")
    number1=number2
    number2=number

