
'''
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
true=[]
false=[]
try:
	for i in values:
		true.append(set(i))
except:
	for i in values:
		false.append(i)
print('spisok true:',true)
print('spisok false:',false)
'''
'''
a=input('ведите 5 чисел с запитыми')
set={1}
for i in a.split(','):
		set.update(i)
print(set)
for i in a:
	min(i)
print(i)
'''
'''
f=['input','print','len']
b=input('выберите Python функции')
if b == 'print':
	print('принтует')
elif b=='input':
	print('ведите число или слово')
elif b=='len':
	c=len(b)	
	print('считает количество элемент',c)
else:
	print('нету токой функции') 

'''
'''
summa=int(input('сумма кредита не меньше 50 000som'))
print('ваш пранцент составляет',summa*(3.47/100))

'''
'''
c=input('буква')
print(c+5)
'''
'''
color=['red','green','blue']
print(color[3])
'''
'''

name='hello'
print(NAMe)
'''
'''
at = 10
i = 15
wo = 20
try:
    for i in range(-at, at):
        print(wo / i)
        if at > '5':
            print("at" > 5)
except TypeError:
	print('у тебя ошибка')
'''
lst = []
for i in renge(10):
lst.apend(i)

a = list(revesed(lst))
sls_obj = slice('0','8')
print(а[sls_obj])

