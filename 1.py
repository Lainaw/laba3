def isDividableByThree(number):
  return number % 3 == 0

userInput = input('Введите число: ')

if isDividableByThree(int(userInput)):
  print('Число делиться на 3')
else:
  print('Число не делится на 3!')