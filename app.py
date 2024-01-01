def getNumber(number):
    count=0
    while number>0:
        count+=1
        number//=10
    return  count

print(getNumber(int(input('Enter a number:'))))
print('Dastur ishladi....')

print('urraaaaa')



def calc(a,b):
    return a+b

print(calc(5,7))
