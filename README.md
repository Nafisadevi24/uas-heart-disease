# Heart Disease Prediction App
Aplikasi prediksi penyakit jantung menggunakan Random Forest Classifier.

## Struktur Folder
```
heart-disease-app/
├── templates/
│   └── index.html       ← tampilan website
├── app.py               ← server Flask
├── model_heart.pkl      ← model hasil training (dari Colab)
├── scaler.pkl           ← scaler hasil training (dari Colab)
├── Procfile             ← untuk Heroku
└── requirements.txt     ← library yang dibutuhkan
```

## Cara Deploy ke Heroku

### 1. Persiapan (lakukan sekali)
- Install [Anaconda](https://www.anaconda.com)
- Install [VS Code](https://code.visualstudio.com)
- Daftar akun di [Heroku](https://www.heroku.com)
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### 2. Letakkan file model
Copy `model_heart.pkl` dan `scaler.pkl` dari Google Colab ke folder ini.

### 3. Coba jalankan lokal dulu
```bash
# Buat virtual environment
conda create --name heart-deploy python=3.9
conda activate heart-deploy

# Install library
pip install -r requirements.txt

# Jalankan
python app.py
```
Buka browser: http://localhost:5000

### 4. Deploy ke Heroku
```bash
# Login Heroku
heroku login

# Buat app baru di Heroku (ganti nama sesuai keinginan)
heroku create nama-app-kamu

# Upload ke Heroku
git init
heroku git:remote -a nama-app-kamu
git add .
git commit -m "deploy pertama"
git push heroku master
```

### 5. Buka website
Setelah selesai, Heroku akan memberikan URL seperti:
`https://nama-app-kamu.herokuapp.com`

## Catatan Penting
- File `model_heart.pkl` dan `scaler.pkl` HARUS ada di folder ini
- Versi library di `requirements.txt` harus sama dengan yang dipakai di Colab
- Aplikasi ini hanya untuk keperluan akademis, bukan diagnosis medis
