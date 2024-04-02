from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
liver_model = 'a_model.pkl'
model = joblib.load(open(liver_model, 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        age = float(request.form['age'])
        gender = int(request.form['gender'])  # Assuming binary encoding (0 or 1)
        total_bilirubin = float(request.form['total_bilirubin'])
        alkaline_phosphotase = float(request.form['alkaline_phosphotase'])
        alamine_aminotransferase = float(request.form['alamine_aminotransferase'])
        aspartate_aminotransferase = float(request.form['aspartate_aminotransferase'])
        total_proteins = float(request.form['total_proteins'])
        albumin = float(request.form['albumin'])
        albumin_globulin_ratio = float(request.form['albumin_globulin_ratio'])

        # Create a feature vector
        feature_vector = [[age, gender, total_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
                           aspartate_aminotransferase, total_proteins, albumin, albumin_globulin_ratio]]

        # Make prediction
        prediction = model.predict(feature_vector)
        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
