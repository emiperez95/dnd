from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template('map.html')

@app.route('/dess/')
def map_func_dess():
	return render_template('close_map.html')

if __name__ == '__main__':
    app.run(debug = True)    