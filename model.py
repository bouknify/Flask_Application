import numpy as np
import json
import requests

MODEL_URI='http://tensorflow_service:8501/v1/models/dnn:predict'

class Model:
    def __init__(self, cylinders, displacement, horsepower, weight, acceleration, model_year, origin):
        self.cylinders = cylinders
        self.displacement = displacement
        self.horsepower = horsepower
        self.weight = weight
        self.acceleration = acceleration
        self.model_year = model_year
        self.origin = origin
        self.features_list =[]

    def origin_mapping(self):
        switcher = {
            "Europe": [1,0,0],
            "Japan" : [0,1,0],
            "USA"   : [0,0,1],
        }
        return switcher.get(self.origin, None)
    
    def generate_numeric_features(self):
        try:
            self.features_list.append(float(self.cylinders))
            self.features_list.append(float(self.displacement))
            self.features_list.append(float(self.horsepower))
            self.features_list.append(float(self.weight))
            self.features_list.append(float(self.acceleration))
            self.features_list.append(float(self.model_year))
        except ValueError:
            return False
        self.features_list.extend(self.origin_mapping())
        return True

    def get_prediction(self):
        print(self.features_list)
        self.features_list = np.expand_dims(self.features_list, axis=0)
        
        data = json.dumps({
            'instances': self.features_list.tolist()
        })
        response = requests.post(MODEL_URI, data=data.encode('utf-8'))
        result = json.loads(response.text)
        prediction = np.squeeze(result['predictions'][0])
        return prediction
