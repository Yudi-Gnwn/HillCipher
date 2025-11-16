import streamlit as st
import numpy as np

# Fungsi logika Dasar

# konversi teks ke angka (0-25)
def teks_ke_angka(teks):
    return [ord(c.upper()) - ord('A') for c in teks if c.isalpha()]

# konversi angka ke teks
def angka_ke_teks(angka):
    return ''.join([chr(n % 26 + ord('A')) for n in angka])

# mencari modular inverse dengan (a^-1 mod m)
def invers_mod(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# mencari invers matriks (K^-1) mod 26
def invers_matriks_mod(matriks, mod):
    determinan = int(np.round(np.linalg.det(matriks)))
    invers_det = invers_mod(determinan % mod, mod)
    
    # validasi jika tidak memiliki invers
    if invers_det is None:
        raise ValueError("Matriks tidak memiliki invers modulus 26. Coba matriks lain.")
    
    # rumus: K^-1 = (det(K))^-1 * Adj(K) mod 26
    adjugate = np.round(determinan * np.linalg.inv(matriks)).astype(int)
    return (invers_det * adjugate) % mod


# fungsi hill cipher

def hill_cipher(teks_input, kunci_matriks, enkripsi=True):
    n = len(kunci_matriks)

    # pembersihan texs, upercase
    teks = "".join(c for c in teks_input.upper() if c.isalpha())
    
    # padding x
    while len(teks) % n != 0:
        teks += 'X'
    
    # pilih matriks: K untuk enkripsi, K^-1 untuk dekripsi
    teks_yang_diproses = teks
    matriks = kunci_matriks if enkripsi else invers_matriks_mod(kunci_matriks, 26)

    # proses per blok
    angka = teks_ke_angka(teks_yang_diproses)
    hasil = []
    for i in range(0, len(angka), n):
        blok = np.array(angka[i:i+n])
        hasil_blok = np.dot(matriks, blok) % 26
        hasil.extend(hasil_blok)
    
    # return hasil - teks
    return angka_ke_teks(hasil), teks_yang_diproses


# UI Streamlit

st.set_page_config(page_title="TecNovaID Login", layout="centered")
st.title("🔒 TechNovaID")
st.subheader("Login Karyawan - HillCipher 2x2")

# Form input
with st.form("hill_cipher_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    st.write("**Masukkan Key Matrix 2x2 (0-25):**")
    
    # input matriks 
    col1, col2 = st.columns(2)
    with col1:
        k00 = st.number_input("a", min_value=0, max_value=25, value=3, step=1)
        k10 = st.number_input("c", min_value=0, max_value=25, value=2, step=1)
    with col2:
        k01 = st.number_input("b", min_value=0, max_value=25, value=3, step=1)
        k11 = st.number_input("d", min_value=0, max_value=25, value=5, step=1)

    submit_button = st.form_submit_button("Proses")

# Output
if submit_button:
    # validasi
    if not username or not password:
        st.warning("Username dan Password harus diisi.")
    else:
        key_matrix = np.array([[k00, k01], [k10, k11]])
        
        # bersihkan input
        clean_username = "".join(c for c in username.upper() if c.isalpha())
        clean_password = "".join(c for c in password.upper() if c.isalpha())
        
        # simpan panjang
        len_clean_username = len(clean_username)
        
        # gabungkan untuk enkripsi
        combined_clean_text = clean_username + clean_password
        
        try:
            # enkripsi-
            ciphertext, processed_plaintext = hill_cipher(combined_clean_text, key_matrix, enkripsi=True)
            
            # dekripsi-
            decrypted_text_padded, _ = hill_cipher(ciphertext, key_matrix, enkripsi=False)
            
            # hapus padding x
            final_decrypted_text = decrypted_text_padded[:len(combined_clean_text)]
            
            # pisahkan kembali string yang sudah didekripsi
            decrypted_username = final_decrypted_text[:len_clean_username]
            decrypted_password = final_decrypted_text[len_clean_username:]

            # Hasil
            st.write("Original Username (Plaintext):")
            st.code(clean_username, language="text")
            
            st.write("Original Password (Plaintext):")
            st.code(clean_password, language="text")

            st.write("Key Matrix used:")
            st.code(f"{key_matrix}", language="text")

            st.write("Encrypted Text (Ciphertext):")
            st.success(ciphertext)

            st.write("Username (Decrypted):")
            st.code(decrypted_username, language="text")
            
            st.write("Password (Decrypted):")
            st.code(decrypted_password, language="text")

        except ValueError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"Error Tak Terduga: {e}")