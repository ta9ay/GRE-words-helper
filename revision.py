import json
import random

score_list={} #maintains scores for the program runtime

with open('c://worddata//wordlist.json', 'r') as file:
	data=json.load(file) #loads existing data from json file

ques_keys = list(data.keys()) #list of question keys

random.shuffle(ques_keys)

def quiz(ques_keys,data):
	
	with open('c://worddata//revise-score.json', 'r') as f:
		scores=json.load(f) #load json dictionary in scores

	for key in ques_keys:
		options=[] #list of options for the question
		for i in range(0,3):
			#choosing three random key values from 'data' dict and adding value to options list
			options.append(data[random.choice(list(data.keys()))])
		correct_answer = data[key]
		options.append(correct_answer)
		random.shuffle(options)
		answers={k:v for k,v in enumerate(options)}

		print("# "+key+":")
		for k,v in answers.items():
			print("	"+str(k)+" : "+v)
		
		selection= int(input('>> '))
		if selection == 9:
			break
		else:
			if answers[selection]==correct_answer:
				print("RIGHT")
				print('')

			else:
				print("WRONG. The answer was: " + correct_answer )
				print('')
				score_list[key]=1
		

		with open('c://worddata//revise-score.json', 'w') as f:
			if key in scores:
				score_list[key] = scores[key]+1 #if already in json file, update the score by 1
			scores.update(score_list)
			f.write(json.dumps(scores,indent=4))




print("Select the correct option for each of the following words: ")
quiz(ques_keys,data)