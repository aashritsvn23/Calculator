import string
import random

p1 = list(string.ascii_lowercase)
p2 = list(string.ascii_uppercase)
p3 = list(string.digits)
user_input = input("How many characters of Password ")

while True:

	try:

		characters_number = int(user_input)

		if characters_number<5:

			print("Your number should be at least 5.")

			user_input = input("Please, Enter your number again: ")

		else:
			break
	except:

		print("Please, Enter numbers only.")

		user_input = input("How many characters of password? ")

random.shuffle(p1)
random.shuffle(p2)
random.shuffle(p3)

part1 = round(characters_number * (40/100))
part2 = round(characters_number * (30/100))

result = []

for x in range(part1):

	result.append(p1[x])
	result.append(p2[x])

for x in range(part2):

	result.append(p3[x])

random.shuffle(result)
password = "".join(result)
print("Strong Password: ", password)
