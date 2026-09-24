first_num=int(input("Enter the first number:\n"))
sec_num=int(input("Enter the second number:\n"))
sum=first_num*sec_num
print(f"{first_num} * {sec_num} = {sum}")
if(sum>0):
    print("The result is positive.")
elif(sum<0):
    print("The result is negative.")
elif(sum==0):
    print("The result is positive and negative.")