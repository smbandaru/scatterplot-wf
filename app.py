from flask import Flask, request
import pandas as pd
from scipy import stats
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/fitModel', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type','Authorization'])
def fit_linear_model():
    file = request.files['file']
    data = pd.read_csv(file)
    x = data['x']
    y = data['y']
    print(x._values)
    print(y._values)

    res = stats.linregress(x, y)

    return {'slope':res.slope,'intercept':res.intercept, 'data': data.to_dict(orient='list')}

if __name__ == '__main__':
    app.run(debug=True)