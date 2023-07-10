from flask import Flask, request, render_template
from Code import Code
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVR
################################
attributes = ['potential', 'preferred foot', 'attacking', 'defensing', 'crossing', 'finishing', 'heading',
              'short passing', 'volleys', 'dribbling', 'curve', 'free kicks',
              'long passing', 'ball control', 'acceleration', 'sprint speed',
              'agility', 'reactions', 'balance', 'shot power', 'jumping', 'stamina',
              'strength', 'long shots', 'aggression', 'interceptions', 'positioning',
              'vision', 'penalties', 'marking', 'standing tackle', 'sliding tackle',
              'gk diving', 'gk handling', 'gk kicking', 'gk positioning']
################################
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
################################


@app.route('/check', methods=['POST'])
def check():
    var = zip(attributes, range(len(attributes)))
    return render_template('check.html', attrs=var)


#################################
selected = []


@app.route('/form', methods=['POST'])
def form():
    selected = request.form.getlist('check_attrs')
    return render_template('form.html', selected=selected)
#################################


@app.route('/predict', methods=['POST'])
def predict():
    values = []
    target = ['overall_rating']

    for attr in attributes:
        values.append(int(request.form.get(attr, 50)))

    result = round(Code.prediction(values)[0], 2)

    return render_template('predict.html', res=result)


if __name__ == '__main__':
    app.run()
