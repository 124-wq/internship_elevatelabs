from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/',methods=['GET'])
def portfolio():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug = True)

