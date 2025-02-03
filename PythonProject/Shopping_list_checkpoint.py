# creating a shopping list

shopping_list = []
item = {}
i=0
while True:
  print('\nShopping List Menu:','\n1-Add item','\n2-Remove item', '\n3-View list', '\n4-Quit')
  selection= input('MAKE A SELECTION(1/2/3/4): ')
  if selection == '1':
    item= input('Add Item:')
    if len(shopping_list)<=5:
      shopping_list.append(item)
      i+= 1
      print(f'{item} has been added to the list', '\n Do you want to continue shopping?')
    else:
      print(f'{item} can not be added, your list is full', '\n Do you want to continue shopping?')
  elif selection == '2':
    item = input('What do you want to remove? ')
    if item not in shopping_list:
      print(f'{item} is not in your list', '\nDo you want to continue shopping?')
    else:
      shopping_list.remove(item)
      i-= 1
      print(f'{item} has been removed from your list', '\n Do you want to continue shopping?')
  elif selection == '3':
    if shopping_list:
      print(f' You Have {i} Items in your shopping_list: ')
      for item in shopping_list:
        print(f'- {item}', '\n Do you want to continue shopping?')
    else :
      print('Your shopping list is empty', '\n Do you want to continue shopping?')
  elif selection == '4':
    print('goodbye see you next time')
    break
  else :
    print('Invalid choice','\nTry Again')