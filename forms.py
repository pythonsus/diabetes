
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired, Length,Email
class d(FlaskForm):
    p = StringField('How many pregnancies do you have', validators=[InputRequired()])
    g = StringField('Plasma glucose concentration a 2 hours in an oral glucose tolerance test', validators=[InputRequired()])
    bp = StringField('Diastolic blood pressure (mm Hg)', validators=[InputRequired()])
    st = StringField('Triceps skin fold thickness (mm)', validators=[InputRequired()])
    I = StringField('2-Hour serum insulin (mu U/ml)', validators=[InputRequired()])
    BMI = StringField('Body mass index (weight in kg/(height in m)^2)', validators=[InputRequired()])
    dpf = StringField('Diabetes pedigree function', validators=[InputRequired()])
    Age = StringField('Age (years)', validators=[InputRequired()])
    submit = SubmitField('Submit for results')














    


