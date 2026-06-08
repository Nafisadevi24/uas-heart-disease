from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model dan scaler
model  = joblib.load("model_heart.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================================
# KOLOM YANG DIHASILKAN SETELAH get_dummies drop_first=True
# Urutan ini HARUS persis sama dengan saat training
# Didapat dari: list(X_train.columns) setelah encoding
# =====================================================
FEATURE_COLUMNS = [
    "age", "trestbps", "chol", "thalch", "oldpeak", "ca",
    "sex_Male",
    "cp_atypical angina", "cp_non-anginal", "cp_typical angina",
    "fbs_True",
    "restecg_normal", "restecg_st-t abnormality",
    "exang_True",
    "slope_flat", "slope_upsloping",
    "thal_normal", "thal_reversable defect"
]

def preprocess_input(data):
    """
    Manual encoding — tidak pakai get_dummies agar kolom selalu konsisten.
    Mapping persis sama seperti yang dihasilkan get_dummies(drop_first=True)
    pada data training.
    """
    # Nilai numerik langsung
    age      = float(data["age"])
    trestbps = float(data["trestbps"])
    chol     = float(data["chol"])
    thalch   = float(data["thalch"])
    oldpeak  = float(data["oldpeak"])
    ca       = float(data["ca"])

    # sex: drop_first → Male jadi reference, sisanya sex_Male
    sex = data["sex"]   # "Male" atau "Female"
    sex_Male = 1 if sex == "Male" else 0

    # cp: drop_first → "asymptomatic" jadi reference
    cp = data["cp"]
    cp_atypical_angina = 1 if cp == "atypical angina" else 0
    cp_non_anginal     = 1 if cp == "non-anginal" else 0
    cp_typical_angina  = 1 if cp == "typical angina" else 0

    # fbs: True/False string → fbs_True
    fbs = data["fbs"]
    fbs_True = 1 if fbs in ("True", "Ya", True, "1") else 0

    # restecg: drop_first → "lv hypertrophy" jadi reference
    restecg = data["restecg"]
    restecg_normal           = 1 if restecg == "normal" else 0
    restecg_st_t_abnormality = 1 if restecg == "st-t abnormality" else 0

    # exang: True/False string → exang_True
    exang = data["exang"]
    exang_True = 1 if exang in ("True", "Ya", True, "1") else 0

    # slope: drop_first → "downsloping" jadi reference
    slope = data["slope"]
    slope_flat      = 1 if slope == "flat" else 0
    slope_upsloping = 1 if slope == "upsloping" else 0

    # thal: drop_first → "fixed defect" jadi reference
    thal = data["thal"]
    thal_normal           = 1 if thal == "normal" else 0
    thal_reversable_defect = 1 if thal == "reversable defect" else 0

    # Susun sesuai FEATURE_COLUMNS
    row = {
        "age"                      : age,
        "trestbps"                 : trestbps,
        "chol"                     : chol,
        "thalch"                   : thalch,
        "oldpeak"                  : oldpeak,
        "ca"                       : ca,
        "sex_Male"                 : sex_Male,
        "cp_atypical angina"       : cp_atypical_angina,
        "cp_non-anginal"           : cp_non_anginal,
        "cp_typical angina"        : cp_typical_angina,
        "fbs_True"                 : fbs_True,
        "restecg_normal"           : restecg_normal,
        "restecg_st-t abnormality" : restecg_st_t_abnormality,
        "exang_True"               : exang_True,
        "slope_flat"               : slope_flat,
        "slope_upsloping"          : slope_upsloping,
        "thal_normal"              : thal_normal,
        "thal_reversable defect"   : thal_reversable_defect,
    }

    df = pd.DataFrame([row], columns=FEATURE_COLUMNS)
    return df


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = {
            "age"     : request.form.get("age"),
            "sex"     : request.form.get("sex"),
            "cp"      : request.form.get("cp"),
            "trestbps": request.form.get("trestbps"),
            "chol"    : request.form.get("chol"),
            "fbs"     : request.form.get("fbs"),
            "restecg" : request.form.get("restecg"),
            "thalch"  : request.form.get("thalch"),
            "exang"   : request.form.get("exang"),
            "oldpeak" : request.form.get("oldpeak"),
            "slope"   : request.form.get("slope"),
            "ca"      : request.form.get("ca"),
            "thal"    : request.form.get("thal"),
        }

        df_input  = preprocess_input(input_data)
        df_scaled = scaler.transform(df_input)

        result = model.predict(df_scaled)[0]
        prob   = model.predict_proba(df_scaled)[0]

        if result == 1:
            prediction = "POSITIF Penyakit Jantung"
            prob_val   = round(prob[1] * 100, 1)
            status     = "danger"
            emoji      = "⚠️"
        else:
            prediction = "NEGATIF Penyakit Jantung"
            prob_val   = round(prob[0] * 100, 1)
            status     = "safe"
            emoji      = "✅"

        return render_template(
            "index.html",
            prediction = prediction,
            prob       = prob_val,
            status     = status,
            emoji      = emoji,
            form_data  = input_data
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction = f"Error: {str(e)}",
            status     = "error",
            emoji      = "❌"
        )


if __name__ == "__main__":
    app.run(debug=True)
