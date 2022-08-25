# Import libraries
from random import random
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

# Load the model
model = pickle.load(open('model1.pkl','rb'))


@app.route('/api',methods=['POST'])
def predict():
   
    data = request.get_json(force=True)
    
    # Expected data format {"predict":[year,male_percentage,no_of_schools,cost_of_education]}
    # New Format :: {"predict":[year,state]}
    if(data["predict"] == None):
        return jsonify({"error":"can't find predict key in body"})
    

    
    
    state=state_gen(data["predict"][1])
    
    year=data["predict"][0]
    
    diff=year-2022
    male_percent=75
    no_of_schools=random.randint(110000,300000)+(5000*diff)
    cost_of_education=random.randint(850000,1000000)+(5000*diff)
    
    
    
    
    
    predict_list=[year,male_percent,no_of_schools,cost_of_education]
        
    
    prediction = model.predict([np.array(predict_list)])

    return jsonify({"pass-fail-rate":prediction[0]})


if __name__ == '__main__':
<<<<<<< HEAD
    app.run(port=8080, debug=False)


def gen_zero(n):
    zeroes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    zeroes[n]=1
    return zeroes

def state_gen(state):
    state=state+"state_"
    states_map={
        "state_Andaman and Nicobar Islands":0,
        "state_Andhra Pradesh":1,
        "state_Arunachal Pradesh":2,
        "state_Assam":3,
        "state_Bihar":4,
        "state_Chandigarh":5,
        "state_Chhattisgarh":6,
        "state_Dadra and Nagar Haveli":7,
        "state_Daman and Diu":8,
        "state_Delhi":9,
        "state_Goa":10,
        "state_Gujarat":11,
        "state_Haryana":12,
        "state_Himachal Pradesh":13,
        "state_Jammu and Kashmir":14,
        "state_Jharkhand":15,
        "state_Karnataka":16,
        "state_Kerala":17,
        "state_Lakshadweep":18,
        "state_Madhya Pradesh":19,
        "state_Maharashtra":20,
        "state_Manipur":21,
        "state_Meghalaya":22,
        "state_Mizoram":23,
        "state_Nagaland":24,
        "state_Odisha":25,
        "state_Puducherry":26,
        "state_Punjab":27,
        "state_Rajasthan":28,
        "state_Sikkim":29,
        "state_Tamil Nadu":30,
        "state_Telangana":31,
        "state_Tripura":32,
        "state_Uttar Pradesh":33,
        "state_Uttarakhand":34,
        "state_West Bengal":35,
    }
    if(state in states_map.keys()):
        return gen_zero(states_map[state])
    else:
        return gen_zero(25)
        
        


    app.run(port=8080, debug=False,host="0.0.0.0")
