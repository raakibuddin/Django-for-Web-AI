'''Class -02
Assignment

1. Print your name.
2. Input your batch number using input() function.
3. Create 5 different valid Variables and print.
4. Create Pascal Case Variable.
5. Assign a single value to Multiple variables with memory location.
6. Input float value using input().
7. a = ‘Welcome to Django for web and Ai’ convert into upper case.
8. b = ‘ Python’ remove whitespace.
9. c = 60, d= 22 ‘Conversion int to float’.
10. Create a dictionary & print your info.'''

# 1.print your name
print('Rakib Uddin')
# 2. Input your batch name using input()function
batchname= input('Enter Your batch number: ')
print('Your batch number Django for Web & AI is:',batchname)
# 3 create different 5 valid variables and print
a = 'Rakib'
print(a)
print(type(a))
b = 10
print(b)
print(type(b))
c = 20.33
print(c)
print(type(c))
d = 10>8
print(d)
print(type(d))
e = 1+3j
print(e)
print(type(e))


# 4 create pascal case variable
PascalCaseVariable = 'Rakib Uddin'
print(PascalCaseVariable)

# 5. Assign a single value to Multiple variables with memory location
a = n = b = 4
print(a)
print(n)
print(b)

print(id(a))
print(id(n))
print(id(b))

# 6. Input float value using input().
u = float(input('Enter float number: '))
print('float value is ', u)

# 7. a = ‘Welcome to Django for web and Ai’ convert into upper case.
a = 'Welcome to Django for web and Ai'
print(a.upper())
# 8. b = ‘ Python’ remove whitespace.
b= '     python'
print(b.strip())
# 9. c = 60, d= 22 ‘Conversion int to float’.
c = 60
d= 22

#int to float
l = float(c)
print('int to float', l)
f = float(d)
print('int to float',f)
# 10. Create a dictionary & print your info.

firstdict ={
    'name' : 'Rakib Uddin',
    'batch' : 1
}
print(firstdict)
print(type(firstdict))
