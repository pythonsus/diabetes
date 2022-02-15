
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split as tts
from sklearn import svm
from flask import render_template,Flask,request
from joblib import dump, load
from forms import d
application = Flask(__name__)
application.config['SECRET_KEY'] = 'iuhguivfduivdifvjdfhv'

@application.route('/', methods=['GET','POST'])
def main():
  form = d()
 
  if form.is_submitted():
    result = request.form
    scaler = StandardScaler()
    data = pd.read_csv('diabetes.csv')
    data.groupby('Outcome').mean()
    x = data.drop(columns='Outcome', axis=1)
    y = data['Outcome']
   
    scaler.fit(x)
    sd = scaler.transform(x)
    x = sd
    
    # c = svm.SVC(kernel='linear')
    # c.fit(x_train,y_train)
    # xp = c.predict(x_test)
    # tda = accuracy_score(xp,y_test)
    # tda
    c = load('lcm.joblib')
   
    input_data = (float(result['p']),float(result['g']),float(result['bp']),float(result['st']),float(result['I']),float(result['BMI']),float(result['dpf']),float(result['Age']))

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # standardize the input data
    std_data = scaler.transform(input_data_reshaped)


    prediction = c.predict(std_data)


    if (prediction[0] == 0):
      return '<h1>The person is not diabetic</h1>'
    else:
      return '<h1>The person is diabetic</h1>'
  return render_template('index.html',form=form)
  
if __name__ == '__main__':
    application.run(debug=True)