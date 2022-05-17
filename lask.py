'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a=input("язык  программирования:")
for i in languages:
	if a==i:
		print('this languages is in list' )
'''
'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
a=input('перебрать:')
for i in  languages:
	print(i)
	if a==i:
		break

'''
'''
a=7
for i in range(5):
	print(a*a)

'''
'''
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(len(languages)):
	print(i,languages[i])
'''
'''
for i in range(11):
	print(i, end='')
for i in range (10,1,-1):
	print(i, end='
'''

'''
names=['Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан']
for i in range(len(names)):
	if i % 2!=0:
		print(names[i])
'''
a=input()
if len(a)==3:
		print('это трехзначное число')
else:
		print('он не трехзначное число')
if a>=0 and a%2==0:
	print('он положителный')
else:
		print('не положительное')

 


