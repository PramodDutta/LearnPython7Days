num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

# max_num = max(num1,num2,num3)
# print(max_num)

if num1 >  num2 and num1 > num3:
    print(num1)
elif num2 >num1 and num2 > num3:
    print(num2)
else:
    print(num3)