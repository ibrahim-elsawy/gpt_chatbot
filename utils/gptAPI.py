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
	p = info 
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

if __name__ == '__main__':
	ask("this dummy chatbot", ["how are you", "what's your name"], ["fine", "my name's jimmy"])