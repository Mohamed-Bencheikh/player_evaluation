from flask import Flask, request,render_template
from Code import Code
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.svm import SVR

attributes = ['potential','preferred_foot','attacking','defensing','crossing', 'finishing', 'heading',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kicks',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']

app = Flask(__name__)
@app.route('/myApp')
def game(): 
    return render_template('game.html')

@app.route('/position',methods=['POST'])
def position():
    return render_template('position.html')

@app.route('/check',methods=['POST'])
def check():
    return render_template('check.html',attributes=attributes)

selected = []
@app.route('/form',methods=['POST'])
def form():
    selected = request.form.getlist('check_attrs')
    return render_template('form.html',selected=selected)

@app.route('/predict',methods=['POST'])
def predict():
    values = []
    target = ['overall_rating']
    attrs = ['preferred_foot','dribbling']

    for attr in attributes:
        values.append(int(request.form.get(attr,50)))
    
    result = round(Code.prediction(values)[0],2)
    return render_template('predict.html',res = result)

if __name__ == '__main__':
    app.run()