
# importing Flask and other modules
from flask import Flask
 
# Flask constructor
app = Flask(__name__)  
 
# A decorator used to tell the application
# which URL is associated function
@app.route('/')
def hello():
	return 'Greetings from Docker! You are connected!'
	
if __name__=='__main__':
   app.run(host='0.0.0.0', port=5000)
