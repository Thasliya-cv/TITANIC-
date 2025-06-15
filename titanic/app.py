from flask import Flask, render_template, request
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    Age=int(request.form['Age'])
    Sex=request.form['Sex']
    if Sex=='Female':
        Sex_female=1
        Sex_male=0
    else:
        Sex_female=0
        Sex_male=1
    Pclass=int(request.form['Pclass'])
    SibSp=int(request.form['SibSp'])
    Parch=int(request.form['Parch'])
    Embarked=request.form['Embarked']
    if Embarked=='C':
        Embarked_C=1
        Embarked_Q=0
    else: 
        Embarked_C=0
        Embarked_Q=1

    Prediction=model.predict([[Pclass,Age,SibSp,Parch,Sex_female,Sex_male,Embarked_C,Embarked_Q]])
    return render_template('result.html', pred_rslt=Prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
    