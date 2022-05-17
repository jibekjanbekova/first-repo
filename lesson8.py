
'''
ls = [12, 35454, 6566, 767, 7778, 8, 77, 7, 754545, 454, 54, 33, 2, 232, 12, 45, 99, 765]
print(ls.index(min(ls)))
'''
'''
ls=['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']
a=ls.count('good')

b=ls.count('bad')

if a==2 or a == 1:
	print('Опубликовать')
elif a>2:
	print('Я чувствую серию!')
else:
	print('Fail')
'''
'''
a='мир'
print(a[::-1])
b='слово'
print(b[::-1])
'''
'''
a=int(input('god'))
def vek(a):
	if a%100+0:
		d=int(a/100)
	else:
		d=int(a/100)+1
	return(str(d))+'vek'
print(vek(a))
'''
'''
matches=["3:1", "2:2", "0:1", "3:0", "0:0", "0:1", "4:2", "2:1", "1:1", "0:2"]
point=0
for i in matches:
	if i[0]>i[2]:
		points += 3
	elif i[0]==i[2]:
		points += 1
print(points)

'''
n=int(input('цена телефона:'))
k=int(input('сумма которую хотите откладывать каждый день:'))
money=0
days=0
while n !=money:
	money +=k
	days+=1
if money == n:
	print(f'Маше потребовалась {days} дней чтобы купить телефон')
