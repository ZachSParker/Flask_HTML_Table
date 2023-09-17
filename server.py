from flask import Flask,render_template,redirect
app = Flask(__name__)
users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'},
    {'first_name' : 'Matthew', 'last_name' : 'Broderick'},
    {'first_name' : 'Phillip J', 'last_name' : 'Fry'},
    {'first_name' : 'Kacy', 'last_name' : 'Stark'},
    {'first_name' : 'Samuel','last_name':'Parker'} 
    ]


@app.route('/')
def hello_world():
    return redirect('/home')
@app.route('/home')
def home_page():
    return render_template('index.html',table_users = users)

if __name__ == "__main__":
    app.run(debug=True)