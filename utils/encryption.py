from base64 import decode
import time
import jwt
import datetime
from cryptography.fernet import Fernet
import pickle


class TokenEncryption():
	def __init__(self) -> None: 
		self.enc = _SymmetricEncryption()
		self.key = self.enc.key.decode('utf-8')

	def encrypt(self, payload:dict): 
		jwt_payload = jwt.encode( { 
			**payload,
			# "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30), 
			"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=7), 
			}, self.key,) 
		return jwt_payload 
	def decrypt(self, jwt_payload): 
		valid = False 
		time_valid = False 
		try: 
			decoded = jwt.decode( jwt_payload, self.key, algorithms=["HS256"]) 
			valid = True 
			time_valid = True 
		except jwt.exceptions.ExpiredSignatureError as e: 
			decoded = jwt.decode(jwt_payload, options={"verify_signature": False}) 
			del decoded["exp"] 
			new_token = self.encrypt(decoded) 
			valid = True 
			time_valid = False 
			return {"valid":valid, "time":time_valid, "newToken":new_token} 
		except Exception as e: 
			return {"valid":valid, "time":time_valid} 
			
		return {"valid":valid, "time":time_valid, **decoded}


class _SymmetricEncryption():
	def __init__(self) -> None:
		with open("secret.key", "rb") as f: 
			# key = Fernet.generate_key()
			self.key = pickle.load(f)
			self.fernet = Fernet(self.key) 

	def symm_encrypt(self, msg:str):
		encMessage = self.fernet.encrypt(msg.encode()) 
		print("original string: ", msg) 
		print("encrypted string: ", encMessage)
		return encMessage

	def symm_decrypt(self, secret:str): 
		return self.fernet.decrypt(secret).decode()

# if __name__ == '__main__':
	# payload = {
	# 	"name": "ibrahim",
	# 	"email":"ibrahime_lsawy@gmail.com",
	# 	"password": "12345"
	# }
	# j = encrypt(payload)
	# print(j)
	# # time.sleep(32)
	# s = list(j)
	# s[-1] = '2'
	# j = ''.join(s)
	# print(decrypt(j))