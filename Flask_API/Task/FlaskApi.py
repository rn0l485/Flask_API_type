import prometheus_client
from prometheus_client import Counter
from flask import Flask, Response
from flask import request, jsonify
from FuncSet import fibonacci, ackermann, factorial
import json

app = Flask(__name__)

total_requests = Counter('request_count', 'Total webapp request count', ['method', 'status']) 
# to record the request times

@app.route('/')
def index():
	# for first Page
	total_requests.labels('get', '200').inc()	
	return jsonify("Hello!!! You run the web service successfully!!")

@app.route('/metrics')
def requests_count():
	# for the prometheus to collect the data
	total_requests.labels('get', '200').inc()
	return Response(prometheus_client.generate_latest(total_requests), mimetype='text/plain')

''' start the first part '''

@app.route('/fibonacci/<int:n>')
def CallFibonacci(n):
	# for calling fibonacci
	try:
		answer = fibonacci(n)
		total_requests.labels('get', '200').inc()
		return jsonify(answer)
	except:
		total_requests.labels('get', '500').inc()
		return jsonify({'error': 'Sorry, something goes wrong!'}),500		

@app.route('/ackermann/<int:m>/<int:n>')
def callAckermann(m,n):
	# for calling ackermann
	try:
		answer = ackermann(m,n)
		total_requests.labels('get', '200').inc()
		return jsonify(answer)
	except RuntimeError:
		# if it appears RuntimeError will return here 
		total_requests.labels('get', '500').inc()
		return jsonify({'error':"RuntimeError!!! %s and %s doesn't work! Please select other numbers."%(m,n)}), 500
	except:
		total_requests.labels('get', '500').inc()
		return jsonify({'error': 'Sorry, something goes wrong!'}),500

@app.route('/factorial/<int:n>')
def CallFactorial(n):
	# for calling factorial
	try: 
		answer = factorial(n)
		total_requests.labels('get', '200').inc()
		return jsonify(answer)
	except:
		total_requests.labels('get', '500').inc()
		return jsonify({'error': 'Sorry, something goes wrong!'}),500

''' End of the first part and start the second part '''

@app.route('/calculator', methods=['GET','POST'])
def calculator():
	# this endPoint combines two ways for passing the data, by query and by payload, depends on the request method
	try:
		if request.method == "POST":
			data = json.loads(request.data) 
			if data['Function'] == 'fibonacci':
				n = int(data['FactorN'])
				answer = fibonacci(n)
				total_requests.labels('post', '200').inc()
				return jsonify(answer)
			elif data['Function'] == 'ackermann':
				m = int(data['FactorM'])
				n = int(data['FactorN'])
				try:
					answer = ackermann(m,n)
					total_requests.labels('post', '200').inc()
					return jsonify(answer)
				except RuntimeError:
					total_requests.labels('post', '500').inc()
					return jsonify({'error':"RuntimeError!!! %s and %s doesn't work! Please select other number."%(m,n)}), 500
				except:
					total_requests.labels('get', '500').inc()
					return jsonify({'error': 'Sorry, something goes wrong!'}),500
			elif data['Function'] == 'factorial':
				n = int(data['FactorN'])
				answer = factorial(n)
				total_requests.labels('post', '200').inc()
				return jsonify(answer) 
			else:
				total_requests.labels('get', '500').inc()
				return jsonify({'error':'Please input the function name and keeps in lower case.'}), 500 

		if request.method == "GET":
			function = request.args.get("function")
			m = request.args.get("m")
			n = int(request.args.get("n"))
			
			if function == 'fibonacci':
				answer = fibonacci(str(n))
				total_requests.labels('get', '200').inc()
				return jsonify(answer)
			elif function == 'ackermann':
				try:
					m = int(m)
					answer = ackermann(m,n)
					total_requests.labels('get', '200').inc()
					return jsonify(answer)
				except RuntimeError:
					total_requests.labels('get', '500').inc()
					return jsonify({'error':"RuntimeError!!! %s and %s doesn't work! Please select other numbers."%(m,n)}), 500
				except:
					total_requests.labels('get', '500').inc()
					return jsonify({'error': 'Sorry, something goes wrong!'}),500
			elif function == 'factorial':
				answer = factorial(n)
				total_requests.labels('get', '200').inc()
				return jsonify(answer)  
			else:
				total_requests.labels('get', '500').inc()
				return jsonify({'error':'Please input the function name and keeps in lower case.'}), 500 
	except:
		total_requests.labels('get', '500').inc()
		return jsonify({'error': 'Sorry, something goes wrong!'}), 500

''' End of the second part and start the third part '''

@app.route('/HeaderCalculator')
def GetTheHeader():
	# this function is for passing data by header 
	try:
		headers = request.headers
		if 'Function' in headers:
			func = headers['Function']
		else:
			func = None
		if 'FactorN' in headers:
			n = int(headers['FactorN'])
		else:
			n = None
		if 'FactorM' in headers:
			m = headers['FactorM']
		else:
			m = None

		# for function calling
		if func == 'fibonacci':
			answer = fibonacci(n)
			total_requests.labels('get', '200').inc()
			return jsonify(answer)
		elif func == 'ackermann':
			try:
				m = int(m)
				answer = ackermann(m,n)
				total_requests.labels('get', '200').inc()
				return jsonify(answer)
			except RuntimeError:
				total_requests.labels('get', '500').inc()
				return jsonify({'error':"RuntimeError!!! %s and %s doesn't work! Please select other numbers."%(m,n)}), 500
			except:
				total_requests.labels('get', '500').inc()
				return jsonify({'error': 'Sorry, something goes wrong!'}),500	
		elif func == 'factorial':
			answer = factorial(n)
			total_requests.labels('get', '200').inc()
			return jsonify(answer) 
		else:
			total_requests.labels('get', '500').inc()
			return jsonify({'error': 'Sorry, something goes wrong!'}), 500
	except:
		total_requests.labels('get', '500').inc()
		return jsonify({'error': 'Sorry, something goes wrong!'}), 500

''' End of the third part and start for the error handler '''

@app.errorhandler(404)
def PageNotFound(error):
	total_requests.labels('get', '404').inc()
	app.logger.error('Page not found: %s', (request.path))
	return jsonify({'error':'404! End point not found!! Please check again!'}), 404
@app.errorhandler(405)
def MethodNotAllowed(error):
	total_requests.labels('get', '405').inc()
	app.logger.error('Method Not Allowed: %s', (request.method))
	return jsonify({'error':'405! Method Not Allowed!! Please check again!'}), 405

if __name__ == '__main__':
	app.run(debug=True, threaded=True,)

















