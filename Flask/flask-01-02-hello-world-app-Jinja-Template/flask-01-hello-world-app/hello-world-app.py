from flask import Flask

app = Flask(__name__)

@app.route('/')   #http://localhost:5000
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')  #http://localhost:5000/second
def second():
    return 'This is second page!!'

@app.route('/third/subthird')  #http://localhost:5000/third/subthird
def third():
    return 'This is the subpage of third page'

@app.route('/forth/<string:id>')  #give  id number 
def forth(id):
    return f'Id number of this page is {id}'



if __name__ == '__main__':
    app.run(debug=True)
    