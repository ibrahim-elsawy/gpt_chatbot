
from utils.Database import Database
from utils.Unique import random_string_generator
from utils.encryption import TokenEncryption
from utils.gptAPI import ask, ask_determinsticModel, ask_generativeModel


class HandleRequest():
	def __init__(self) -> None:
		self.data = Database("chatbot")
		self.token = TokenEncryption()
		pass

	def id_request(self, req):
		id = random_string_generator()
		self.data.insertInfo('info', id, None)
		payload = {"email":req["email"], "name":req["name"], "password":req["name"]}
		jwt_token = self.token.encrypt(payload)
		return {"id":id, "token":jwt_token}

	def train_request(self, req):
		token = req['token']
		id = req["id"]
		text = req["info"]
		decode = self.token.decrypt(token)
		res = {}

		if decode['time'] == True: 
			self.data.updateInfo("info", id, text)
			if 'questions' in req.keys():
				for q, a in zip(req['questions'], req['answers']):
					self.data.cleanData('qa', id)
					self.data.insertQA('qa', id, q, a)
			
			status_code = 200
			res['status']='success'
			res['message']='Training completed'
			
		elif decode['valid'] == True: 
			res['status']='failed'
			res['message']='Your token is expired Reactivate your token'
			status_code = 401
		else: 
			res['status']='failed'
			res['message']='Unvalid token'
			status_code = 403
		return res, status_code

	def chat_request(self,req):
		id = req['id']
		query = req['query']
		questions = []
		answers = []
		info = self.data.getRowById("info", id)[0][2]
		qa = self.data.getRowById("qa", id)
		for row in qa:
			questions.append(row[2])
			answers.append(row[3])
		# res = ask(info, questions, answers, query)
		res = ask_generativeModel(info, questions, answers, query)
		# res = ask_determinsticModel(info, questions, answers, query)
		return res

	def refresh_token(self, req):
		token = req["token"]
		decode = self.token.decrypt(token)
		if decode['valid'] == True:
			return decode['newToken']
		return None