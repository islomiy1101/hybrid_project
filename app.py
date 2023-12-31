def getNumber(number):
    count=0
    while number>0:
        count+=1
        number//=10
    return  count

print(getNumber(int(input('Enter a number:'))))