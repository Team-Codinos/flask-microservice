# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle
from flask_cors import CORS


zeroes=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]

app = Flask(__name__)
CORS(app)

# Load the model
model = pickle.load(open('model1.pkl','rb'))


@app.route('/api',methods=['POST'])
def predict():
   
    data = request.get_json(force=True)
    
    # Expected data format {"predict":[year,male_percentage,no_of_schools,cost_of_education]}
    if(data["predict"] == None):
        return jsonify({"error":"can't find predict key in body"})
    
    
    data["predict"].extend(zeroes)
    
    print(data)
    
    
    prediction = model.predict([np.array(data["predict"])])
    
    
    
    return jsonify({"pass-fail-rate":prediction[0]})


if __name__ == '__main__':
    app.run(port=8080, debug=False)
