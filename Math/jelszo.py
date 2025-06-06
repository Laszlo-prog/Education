
prompt =  "\nTell me youre 'password':"
prompt += "\nEnter 'quit' to end program:"

active = True
while active:
 message = input(prompt)


 if message == 'quit':
    active = False
    print('Not well my friend')
    break 
if message == 'password':
    print("Well Done!")
else:
    print('Goodbye')
print()

    
#elif password == ("devil@MAY@cry4"):
    #print("Not pass.")
#elif password == ("Justgirl1990!"):
    #print("Not pass")
#else:
    #print("Try another day")
    
