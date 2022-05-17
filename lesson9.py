
'''
file=open('directories.txt','w')

file.write(aku.py            hello.py   ' lask.py'    snap          Музыка
 ay.ji             janyl.py    lask.py      Видео         Общедоступные
 ay.ji.py          jaynyl.py   lesson8.py   Документы    'Рабочий стол'
 ay.ji.save        jibek.py    lesson9.py   Загрузки      Шаблоны
 directories.txt   jika.py     py           Изображения
jibek@jibek-H)
file.close()
 

f=open('directories.txt','r')
a=f.read()
print(a)
f.close()
 
'''

'''
name=input('username: ')
password=input('pasword:')
f=open('user.txt','w')
a=f.write(f'username:{name}\npassword:{password}')
'''
'''
f=open('user.txt','r')
a=f.read()
if 'w' in a:
	print('да, в тексте есть w')
else:
	print('нет, в тексте нет w')
print(a)
f.close()
'''

#t = []
#b=open('python.txt', 'w')
#a=b.write('''Python is a widely used high-level programming language for general-purpose
#programming, created by Guido van Rossum and first released in 1991. An interpreted
#language, Python has a design philosophy that emphasizes code readability (notably
#using w90hitespace indentation to delimit code blocks rather than curly brackets or
#keywords), and a syntax that allows programmers to express concepts in fewer lines of
#code than might be used in languages such as C++ or Java.''')
'''
b.close()
a=open('python.txt','r')
f=a.read()
for i in f.split():
	if 't'in i:
		t.append(i)
print(t)
a.close()
'''


c=open('database.txt','w')
f=c.write('Aidai:041205')
c.close()
login=input('логин для регистратции')
password=input('ведите пароль')
password=input('ведите пароль для проверки')
d=f.read()
for i in d.split(':'):
	if i==login:
		print('такой логин уже существует')


