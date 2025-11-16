## 🔒 TechNovaID - Simulasi Login Hill Cipher

Ini adalah proyek web yang dibuat dengan Python & streamlit untuk mendemonstrasikan algoritma kriptografi </br> `Hill Cipher 2x2` 

Aplikasi ini berfungsi sebagai simulasi login di mana User akan melakukan login dengan mengisi Username dan Password, </br> kemudian akan dilakukan enkripsi (berdasarkan input matrix) & dekripsi kembali!

### Langkah-langkah
1. Input User: Pengguna melakukan input Username dan Password.
2. Input Key: Pengguna dapat memasukkan Matriks Kunci 2x2 mereka sendiri.
3. Proses Enkripsi: Menampilkan Ciphertext (hasil enkripsi) dari gabungan data.
4. Proses Dekripsi: Menampilkan Plaintext (hasil dekripsi) dan memisahkannya kembali menjadi </br> Username dan Password yang asli.

### requirements
- Python 3.11
- Streamlit (UI)
- NumPy

### Running projek

Clone repositori:
```
git clone [URL-GitHub]
cd [Nama-Folder-Proyek]
```

Buat virtual environment (Conda):
```
conda create -n hillcipher_env python=3.11
conda activate hillcipher_env
```

Install library yang dibutuhkan:
```
pip install -r requirements.txt
```

Jalankan Streamlit:
```
streamlit run app.py
```
