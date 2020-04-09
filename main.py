import second  # import kodingan dari file lain (semua)
from third import secondFunction  # atau fungsi tertentu saja

import random  # contoh library yang bisa diimport
print(random.random())  # return float antara 0 - 1
print(random.randint(1, 6))  # return int antara 1 - 6
fruits = ['apple', 'banana', 'cherry']
favoriteFruit = random.choice(fruits)  # memilih item random

second.goodbye()  # jadi bisa pakai kodingan file tsb
secondFunction()  # bisa dipakai

# deklarasi variabel
price = 5
rating = 4.9
name = "Hello World"
isValid = True

# casting
testCastNumber = 3
str(testCastNumber)  # angka akan berubah jadi string

# inputs -> return typenya selalu string
your_name = input('Enter your name: ')
# maka harus dibungkus dengan int()
angka1 = int(input('Angka 1: '))
angka2 = int(input('Angka 2: '))

# scanf di python
[a, b] = input("Enter 2 numbers: ").split(' ')
print(a)
print(b)

# print format
print("angka pertama {}, angka kedua {}".format(angka1, angka2))
print("angka pertama %d, angka kedua %d" % (angka1, angka2))
print(f'Umur saya: {angka1 + angka2}')


# print karakter pertama
print(name[0])
# print karakter terakhir
print(name[-1])
# print karakter index 0 sampai 2
print(name[0:3])
# string functions
print(name.upper())
print(name.lower())
print(name.title())  # gedein huruf depan
print(name.find('W'))  # return index dari char tertentu
print(name.replace('H', 'B'))  # mengggantikan H dengan B

# split
subjects = "subject1,subject2,subject3"
subjectList = subjects.split(",")
print(subjectList)  # akan di split berdasarkan ,

# untuk join data list menjadi 1
joined = "#".join(subjectList)
print(joined)  # akan jadi subject1#subject2#subject3

# cek substring ada atau tidak, return true / false
contains = 'Hello' in name
print(f'Keberadaan hello: {contains}')

# math operators
print(f'Add: {angka1+angka2}')
print(f'Sub: {angka1-angka2}')
print(f'Mul: {angka1*angka2}')
print(f'Div Float: {angka1/angka2}')  # return float
print(f'Div Integer: {angka1//angka2}')  # return integer
print(f'Mod: {angka1%angka2}')
print(f'Exponent: {angka1**angka2}')  # pangkat

# increment & decrement (gaada angka1++)
angka1 += 1
angka2 -= 1

# if statements
angkaPertama = 300
angkaKedua = 300

if angkaPertama > angkaKedua:
    print("angka 1 lebih besar")
elif angkaPertama < angkaKedua:
    print("angka 2 lebih besar")
else:
    print("kedua angka sama")

# logical operators
# pakai and, or, & not
# bukan pakai && , || & !

# comparison operator
# sama kayak biasa

# while-loops
i = 0
while(i < 3):
    print(i)
    i += 1

# for loops
# range bisa:
#  range(5)-> print 0,1,2,3,4
#  range(1,5)-> print 1,2,3,4
#  range(1,5,2)-> print 1,3 -> range(1,5), tapi print 2 angka saja
for j in range(1, 5):
    print(f'iterasi ke-{j}')

# list
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # print data pertama

# list functions
numbers.append(6)  # tambah 6 ke belakang
numbers.insert(0, 6)  # tambah 6 ke index 0
numbers.remove(6)  # hapus 6
numbers.pop()  # hapus data index terakhir
# numbers.clear() #hapus semua data
numbers.sort()  # sort listnya
numbers.reverse()  # reverse listnya
numbers.copy()  # copy listnya

# tuples (list yang datanya tidak bisa diubah)
coordinates = (1, 2, 3)
# bisa dipecah kedalam variabel sendiri
x, y, z = coordinates
# x = 1, y = 2, z = 3

# sets (list tapi datanya ga bakal dobel)
sets = {'car', 'bike', 'motorbike'}
sets.add('car')  # tidak akan ditambahkan lagi karena sudah ada datanya
print(sets)
# menghilangkan duplikat dari suatu list
duplicateList = [1, 1, 1, 2, 2, 3, 3, 4, 5, 5]
nonDuplicateList = set(duplicateList)
print(nonDuplicateList)  # yang duplikat akan hilang

# mengubah set menjadi list
print(list(nonDuplicateList))


#dictionaries / object
customer = {
    "name": "Ray Tommy",
    "age": 20,
    "isVerified": True,
}

print("Halo nama saya" + customer['name'])  # print atribut object


# functions
def addition(num1, num2):
    return num1+num2


def greet(name):
    return 'hello ' + name


print(addition(100, 12))
print(addition(num2=100, num1=250))
print(greet("mike"))

# exception handling -> kalau error tertentu, muncul message
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Age cannot be 0')


# class
class Mammal:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age

    def eat(self):  # function didalam class disebut 'method'
        print("Eating..")


# inheritance
class Dog(Mammal):
    def bark(self):
        print("Bark")


mammal1 = Mammal("MyMammal", 22)
mammal2 = Dog("Puggy", 12)

mammal2.bark()
mammal2.eat()
