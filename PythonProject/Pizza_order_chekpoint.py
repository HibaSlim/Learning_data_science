"this exercie is to create a model for ordering pizza"

print( 'Welcome To Python Pizza Deliveries')
print('Choose your Pizza size: S, M or L')
size = str (input('size = '))
print('Do You Want some Pepperoni: ')
add_pepperoni= str (input('add_pepperoni = '))
print('Do You Want some extra cheese: ')
extra_cheese= str (input('extra_cheese = '))
final_bill = 0
if size == 'S':
  final_bill += 15
elif size == 'M':
  final_bill += 20
elif size == 'L':
  final_bill += 25
else:
  print('Invalid Input, please choose S , M or l')
if add_pepperoni == 'Y':
    if size == 'S':
        final_bill += 2
    else :
        final_bill += 3
if extra_cheese == 'Y':
    final_bill +=1

print(f'Your final bill is: ${final_bill}')