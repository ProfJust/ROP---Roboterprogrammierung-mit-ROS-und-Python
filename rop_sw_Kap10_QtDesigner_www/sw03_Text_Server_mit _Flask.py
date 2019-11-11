### Simpler Flask Webserver
### Bsp aus https://www.youtube.com/watch?v=vyCboBjK4us 2:48

### ----------------------------------
### $sudo pip install flask
### ----------------------------------
### starten als $sudo sw03_Text_Server_mit _Flask.py

from flask import Flask

app = Flask(__name__)
@app.route("/")

def main():
	str = "Welcome to the Flask Server !"
	return str

if __name__=="__main__":
	app.run(debug=True, host="127.0.0.1", port=80)
