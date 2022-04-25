from unittest import result
from flask import Flask, request, jsonify, Response, make_response
import os
from waitress import serve
from middleware import HandleRequest

import os
#os.environ['ENV'] = 'production'

app = Flask(__name__)

PORT = os.environ.get("PORT")


@app.route("/id", methods=['POST'])
def getId():
	if request.method == 'POST':
		try:
			req = request.get_json()
			handler = HandleRequest()
			res = handler.id_request(req)
			return jsonify(res)
		except Exception as e:
			return Response(status=400)
@app.route("/req", methods=['POST'])
def getRequest():
	if request.method == 'POST':
		try:
			req = request.get_json()
			handler = HandleRequest()
			answer = handler.chat_request(req)
			return jsonify({'response':answer})
		except Exception as e:
			return Response(status=400)																				()

@app.route("/train", methods=['GET'])
def getTrainData():
	if request.method == 'GET':
		try:
			req = request.get_json() 
			handler = HandleRequest()
			res, status_code = handler.previos_training(req)
			
			return make_response(jsonify(res), status_code)
		except Exception as e:
			return Response(status=400)


@app.route("/train", methods=['POST'])
def trainModel():
	if request.method == 'POST':
		try:
			req = request.get_json() 
			handler = HandleRequest()
			res, status_code = handler.train_request(req)
			
			return make_response(jsonify(res), status_code)
		except Exception as e:
			return Response(status=400)

@app.route("/token", methods=['GET'])
def refreshToken():
	if request.method == 'GET':
		try:
			errorRes = {"message" : "invalid token", "error" : "Bad Request"}
			req = request.get_json()
			handler = HandleRequest()
			token = handler.refresh_token(req)
			return jsonify({'token':token}) if token != None else make_response(jsonify(errorRes),400)
		except Exception as e:
			return make_response(jsonify(errorRes),400)



			
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000)) 
	# app.run(app, port=port)
	serve(app, host="0.0.0.0", port=PORT) 
