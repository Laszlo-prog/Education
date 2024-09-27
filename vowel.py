my_string = input('Enter your string: ')
my_char = input('Enter your Character: ')

vowels = ['a','e','i','o','u','A','E','I','O','U']
new_string = ''
for i in my_string:
    if i in vowels:
        new_string +=my_char
    else:
        new_string += i
    print(new_string)
