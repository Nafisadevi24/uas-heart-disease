# ❤️ Heart Disease Prediction App

Aplikasi prediksi penyakit jantung berbasis **Flask** yang menggunakan algoritma **Random Forest Classifier** untuk memprediksi kemungkinan penyakit jantung berdasarkan data kesehatan yang dimasukkan pengguna.

## 📁 Struktur Folder

```text
heart-deploy/
├── templates/
│   └── index.html
├── app.py
├── model_heart.pkl
├── scaler.pkl
├── Procfile
└── requirements.txt
```

## ⚙️ Cara Menjalankan Aplikasi

### 1. Buka Terminal
Pastikan Python 3.9 atau versi yang lebih baru telah terinstal pada sistem.
Buka VS Code → **Terminal** atau gunakan **CMD/PowerShell**.
Pastikan terminal berada pada folder project yang berisi file:

* `app.py`
* `requirements.txt`
* `model_heart.pkl`
* `scaler.pkl`

### 2. (Opsional) Membuat Virtual Environment

Disarankan untuk menghindari konflik library dengan project lain.

```bash
python -m venv venv
```

Aktifkan virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install seluruh library yang diperlukan:

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi Flask

```bash
python app.py
```

Jika berhasil, terminal akan menampilkan:

```text
Running on http://127.0.0.1:5000
```

### 5. Akses Melalui Browser

Buka browser (Chrome, Edge, Firefox, dan lain-lain), kemudian akses:

```text
http://127.0.0.1:5000
```

## 🩺 Fitur Aplikasi

* Prediksi penyakit jantung menggunakan Random Forest Classifier
* Antarmuka berbasis web menggunakan Flask
* Input parameter kesehatan secara interaktif
* Menampilkan hasil prediksi dan tingkat keyakinan (confidence)
* Mendukung penggunaan model machine learning yang telah dilatih sebelumnya

## 🛠️ Teknologi yang Digunakan

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Pickle

## 📌 Catatan Penting

* File `model_heart.pkl` dan `scaler.pkl` wajib tersedia pada folder utama project.
* Versi library pada `requirements.txt` harus sesuai dengan versi yang digunakan saat proses training model.
* Aplikasi ini dibuat untuk keperluan akademis dan tugas mata kuliah Machine Learning.
* Hasil prediksi tidak dapat digunakan sebagai diagnosis medis profesional dan tidak menggantikan konsultasi dengan tenaga kesehatan.
