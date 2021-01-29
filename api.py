import similarity
from flask import Flask, request, render_template,jsonify
app = Flask(__name__)

def do_something(text1,text2):
    score = similarity.main(text1,text2)
    return (score)

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word  = request.args.get('text1')
    text2 = request.form['text2']
    score = do_something(text1,text2)
    result = {
        "output": round(score,2)
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)