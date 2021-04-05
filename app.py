from flask import Flask, flash, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
import numpy as np
import os
from model import Model


app = Flask(__name__, template_folder='Template')
Bootstrap(app)

"""
Routes
"""
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        my_model = Model(request.form['Cylinders'],request.form['Displacement'],request.form['Horsepower'],request.form['Weight'],request.form['Acceleration'],request.form['Model Year'], request.form['Origin'])
        is_mapped = my_model.origin_mapping()
        if is_mapped != None:
            if my_model.generate_numeric_features():
                predicted_value = my_model.get_prediction()
                info = "All input features are valid"
            else:
                predicted_value = None
                info = "All features must be numeric!"
        else:
            predicted_value = None
            info = "Origin must be Europe, Japan or the USA!"
        
        result = {
            'MPG' : predicted_value,
            'INFO': info,
        }
        return render_template('Prediction.html', result = result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
