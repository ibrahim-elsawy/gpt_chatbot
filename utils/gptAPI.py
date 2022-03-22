import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
def ask(info:str, questions:list, answers:list, query:str): 
	# beginOfQuestion = "\n###\nHuman: "
	beginOfQuestion = "\nHuman: "
	beginOFAnswer = "\nAI: "
	qa = ""
	for q, a in zip(questions, answers):
		qa = qa + beginOfQuestion + q + beginOFAnswer + a
	# qa = "\n###\nHuman: ?\nAI: Yes "+"\n###\nHuman: ?\nAI: Most " 
	query = beginOfQuestion + query + beginOFAnswer
	response = openai.Completion.create( 
		engine="davinci", 
		prompt= info + qa + query,
		# prompt= qa + query,
		temperature=0.7, 
		max_tokens=150, 
		top_p=1, 
		frequency_penalty=0, 
		presence_penalty=0.6, 
		# stop=["###"])
		stop=["\n", " Human:", " AI:"])
	return response['choices'][0]['text']


def ask_generativeModel(info:str, questions:list, answers:list, query:str): 
	beginOfQuestion = "\nHuman: "
	beginOFAnswer = "\nAI: "
	qa = ""
	for q, a in zip(questions, answers): 
		qa = qa + beginOfQuestion + q + beginOFAnswer + a

	query = beginOfQuestion + query + beginOFAnswer
	response = openai.Completion.create( 
		engine="text-davinci-002", 
		prompt= info + qa + query, 
		temperature=0.9, 
		max_tokens=150, 
		top_p=1, 
		frequency_penalty=0, 
		presence_penalty=0.6, 
		stop=[" Human:", " AI:"]) 
	return response['choices'][0]['text']	

def ask_determinsticModel(info:str, questions:list, answers:list, query:str): 
	beginOfQuestion = "\nHuman: "
	beginOFAnswer = "\nAI: "
	qa = ""
	for q, a in zip(questions, answers): 
		qa = qa + beginOfQuestion + q + beginOFAnswer + a

	query = beginOfQuestion + query + beginOFAnswer
	response = openai.Completion.create( 
		engine="text-davinci-002", 
		prompt= info + qa + query, 
		temperature=0, 
		max_tokens=100, 
		top_p=1, 
		frequency_penalty=0, 
		presence_penalty=0,
		stop=[" Human:", " AI:"]) 
	return response['choices'][0]['text']	
