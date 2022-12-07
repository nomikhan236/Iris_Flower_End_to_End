
# import dependencies
from flask import Flask , render_template , request
import numpy as np
import pickle

# load our model
model = pickle.load(open("model.pkl" , "rb"))


app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

# Doing prediction
@app.route("/prediction", methods = ["POST"])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']

    arr = np.array([[data1, data2, data3, data4]])
    prediction = model.predict(arr)
    prediction = int(prediction)

    return render_template("prediction.html" , data = prediction)



if __name__ == "__main__":
    app.run(debug=True , port=8000)