import random 

lucky_number = random.randint(1,650)

fortune_number = random.randint(1,10)

fortune_text =''

if fortune_number == 1:
	fortune_text = 'You will have a great day!'
if fortune_number == 2:
	fortune_text = 'You will win the lottery!'
if fortune_number == 3:
	fortune_text = 'You will Live!'
if fortune_number == 4:
  fortune_text = 'You are awesome!'
if fortune_number == 5:
  fortune_text = 'You are almost done!'
if fortune_number == 6:
  fortune_text = 'You are blessed!'
if fortune_number == 7:
  fortune_text = 'You have a gift!'
if fortune_number == 8:
  fortune_text = 'You can go far!'
if fortune_number == 9:
  fortune_text = 'All you need is Python!'
if fortune_number == 10:
  fortune_text = 'You won the grand prize!'

print(f'{fortune_text} Your lucky number is {lucky_number}') 