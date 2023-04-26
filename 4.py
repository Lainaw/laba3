ticketNumber = input('Введите номер билета: ')
splitted = list(ticketNumber)
length = len(splitted)

if sum([int(x) for x in splitted[int(length / 2):]]) == sum([int(x) for x in splitted[-int(length / 2):]]):
  print('Счастливый билет!')
else:
  print('Не позвело...')