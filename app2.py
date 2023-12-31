def getNumber(number):
    count=0
    sum=0
    while number>0:
        count+=1
        sum+=number%10
        number//=10
    return  f'count:{count},sum:{sum}'

print(getNumber(int(input('Enter a number:'))))
print(getNumber(int(input('Enter a number:'))))