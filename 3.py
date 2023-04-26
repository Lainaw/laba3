def isMagicDate(date):
  try:
    split = date.split('.')
    
    if len(split) != 3:
      raise ValueError

    if int(split[0]) * int(split[1]) == int(split[2][-2:]):
      print('Магическая дата')
    else:
      print('Дата не магическая')
  except ValueError:
    print('Неправильный формат даты')
  
input = input('Введите дату в формате dd.mm.yyyy: ')
isMagicDate(input)