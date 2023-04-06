

import traceback
from flask import Flask
from flask import request
from collections import Counter

class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
    
    def load_weights(self, model):
        return self.avaliable_models.get(model,None)

    def load_balancer(self, new_model):
        # Increment frequency of new model
        self.model_frequency[new_model] += 1
        
        # Check if there are two loaded models
        if len(self.loaded_models) == 2:
            # Get frequencies of existing models
            freq_first_model = self.model_frequency[list(self.loaded_models.keys())[0]]
            freq_second_model = self.model_frequency[list(self.loaded_models.keys())[1]]
            
            # Check which model has smaller frequency
            small_model = min(self.loaded_models, key=self.model_frequency.get)
            
            # Replace smaller model if frequencies are equal or new model has higher frequency
            if freq_first_model == freq_second_model or self.model_frequency[new_model] > self.model_frequency[small_model]:
                del self.loaded_models[small_model]
                self.loaded_models[new_model] = self.avaliable_models[new_model]
        else:
            # Load new model 
            self.loaded_models[new_model] = self.avaliable_models[new_model]
    


app = Flask(__name__)
ml = ML()

@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():
    return ml.loaded_models

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        return "processed by "+ ml.loaded_models[model]
    except:
        return str(traceback.format_exc())

app.run(host='0.0.0.0', port=5000)