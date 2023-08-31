from flask import Flask,render_template

app=Flask(__name__)



@app.route("/home", methods=['GET',  'POST'])
def home():
    return "welcome"

@app.route("/chat", methods=['GET',  'POST'])
def chat():
    return render_template('index.html')


@app.route("/bot/response/")
def bot_response():
    return "hello world"
if __name__ == '__main__':
    app.run(debug=True)