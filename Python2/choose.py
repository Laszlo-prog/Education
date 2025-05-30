print("======Welcome=======")

name = input("Type youre name: ")
print("Welcome ", name, "your good adventure")
answer = input("Please choose you're road: ")

if answer == "left":
  answer = input("You most accross a bridge my friend:")
  if answer == "swim":
    print("You swam accross and can eaton by alligator.")
  elif answer == "walk":
     print("You walked for many miles, ran out of time. ")
  else:
      print("Dont move!!!")
elif answer == "right":
   answer = input("You come  from a forest you will be exhausted: ")
if answer == "back":
      print("You are a tired man and cannot to walk.")
elif answer == "cross":
      print("You are a brave man and you so energy. ")
else:
     print("You failed!!")
