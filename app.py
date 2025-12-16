from flask import Flask, request, render_template
from src.preprocess import preprocess_input
import pickle

# --- Cargar modelo y columnas ---
with open("models/modelo.pkl", "rb") as f:
    rf_model = pickle.load(f)
with open("models/columnas.pkl", "rb") as f:
    columnas = pickle.load(f)

app = Flask(__name__)

# Servicios Flask
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    probabilidad = None
    form_data = None

    if request.method == "POST":
        form_data = request.form.to_dict() 
        input_df = preprocess_input(form_data, columnas)
        prediction = rf_model.predict(input_df)[0]
        probability = float(rf_model.predict_proba(input_df)[0][1])

        resultado = "Popular" if prediction == 1 else "No Popular"
        probabilidad = round(probability * 100, 2)

    return render_template(
        "index.html",
        resultado=resultado,
        probabilidad=probabilidad,
        form_data=form_data
    )

if __name__ == "__main__":
    app.run(debug=True)