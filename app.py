from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

filename = 'results_unsw.pkl'
classifier = pickle.load(open(filename,'rb'))
model = pickle.load(open('results_unsw.pkl','rb'))

app = Flask(__name__, template_folder= "template") #template folder

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict_value():
    input_features = [int(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    feature_name = ['rate"','sttl','sload','dload','ct_srv_src',
                    'ct_state_ttl','ct_dst_ltm','ct_dst_src_ltm','ct_srv_dst',
                    'state_CON','state_INT',]
    df = pd.DataFrame(features_value, columns = feature_name)
    output = model.predict(df)
    if output == 1:
        resvalue = 'intrusion detect'
    else:
        resvalue = " not being detected"
        
    return render_template('results_unsw.pkl', prediction_text='Following Diagnosis is made:{}'. format(resvalue))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)