from flask import Flask, request,render_template
from Code import Code

app = Flask(__name__)
@app.route('/myApp')
def game():
    return render_template('game.html')

@app.route('/position',methods=['POST'])
def position():
    return render_template('position.html')

@app.route('/form',methods=['POST'])
def form():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict():
    attributes = ['potential','preferred_foot','attacking','defensing','crossing', 'finishing', 'heading',
       'short_passing', 'volleys', 'dribbling', 'curve', 'free_kicks',
       'long_passing', 'ball_control', 'acceleration', 'sprint_speed',
       'agility', 'reactions', 'balance', 'shot_power', 'jumping', 'stamina',
       'strength', 'long_shots', 'aggression', 'interceptions', 'positioning',
       'vision', 'penalties', 'marking', 'standing_tackle', 'sliding_tackle',
       'gk_diving', 'gk_handling', 'gk_kicking', 'gk_positioning',
       'gk_reflexes']
    values = []
    for attr in attributes:
        values.append(int(request.form.get(attr,50)))
    result = str(round(Code.prediction(values)[0],2))
    return render_template('predict.html',vr = result)

if __name__ == '__main__':
    app.run()