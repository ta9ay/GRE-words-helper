import json

words={}



def input_words():
	print ("# Entering words")
	while True:
		word = input("	> ").lower()
		if word == '':
			with open('c://worddata//wordlist.json', 'r') as file:
				data=json.load(file) #loads existing data from json file
				
				for key in words.keys():
					if key in data.keys():
						words[key]=data[key]+";; "+words[key]

				data.update(words)

			with open('c://worddata//wordlist.json', 'w') as file: #overwrites the data back to the json file
				file.write(json.dumps(data, indent=4))
			return
		else:
			definition = input("		>> ")
		words[word] = definition
		print('')
		

def searching_words():
	with open('c://worddata//wordlist.json', 'r') as file:
		wordsearch=json.load(file) #loads json file for search
	print ("# Searching words")
	while True:
		search = input("$> ").lower()
		if search == '':
			break
		else:
			for keys in wordsearch.keys():
				if keys.startswith(search):
					print("	",keys," : ",wordsearch.get(keys))


# Minor functions
def listlength():
	with open('c://worddata//wordlist.json', 'r') as file:
		wordsearch=json.load(file)
	print(len(wordsearch))
	return

def printlist():
	with open('c://worddata//wordlist.json', 'r') as file:
		wordsearch=json.load(file)
	for key,value in wordsearch.items():
		print(key," : ",value)
	return



while True:
	x = input("Enter(1) / Search(2): ") #len for length, print for the entire list

	if x=='1':
		input_words()
	
	if x=='2':
		searching_words()

	if x== '':
		break
	
	if x== 'len':
		listlength()

	if x== 'print':
		printlist()






##convert all keys to lowercase##

'''
with open('c://worddata//wordlist.json', 'r') as file:
				data=json.load(file)
				data = {key.lower():value for key,value in data.items()}


				#file.write(json.dumps(words))
with open('c://worddata//wordlist.json', 'w') as file:
				file.write(json.dumps(data, indent=4))
'''