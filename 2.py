def divide(number):
  try:
    print(int(number) / 100)
  except ValueError:
    print('Это не число')
  except ZeroDivisionError:
    print('Нельзя делить на 0')

input = input('Введите число: ')
divide(input)