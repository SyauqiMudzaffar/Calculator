import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import DES
import base64

# Fungsi padding
def pad(teks):
    while len(teks) % 8 != 0:
        teks += ' '
    return teks

# Fungsi enkripsi
def encrypt(teks_plain, key):
    des = DES.new(key, DES.MODE_ECB)
    teks_terpad = pad(teks_plain)
    teks_enkripsi = des.encrypt(teks_terpad.encode('utf-8'))
    return base64.b64encode(teks_enkripsi).decode('utf-8')

# Fungsi dekripsi
def decrypt(teks_enkripsi, key):
    des = DES.new(key, DES.MODE_ECB)
    teks_terdekripsi = base64.b64decode(teks_enkripsi)
    teks_dekripsi = des.decrypt(teks_terdekripsi).decode('utf-8')
    return teks_dekripsi.rstrip()

# Fungsi untuk enkripsi dan dekripsi pada GUI
def enkripsi():
    teks_plain = entry_teks_plain.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    key = key_input.encode('utf-8')
    teks_enkripsi = encrypt(teks_plain, key)
    entry_teks_enkripsi.delete(0, tk.END)
    entry_teks_enkripsi.insert(tk.END, teks_enkripsi)

def dekripsi():
    teks_enkripsi = entry_teks_enkripsi.get()
    key_input = entry_kunci.get()
    
    if len(key_input) != 8:
        messagebox.showerror("Error", "Kunci harus terdiri dari 8 karakter.")
        return

    key = key_input.encode('utf-8')
    teks_dekripsi = decrypt(teks_enkripsi, key)
    entry_teks_dekripsi.delete(0, tk.END)
    entry_teks_dekripsi.insert(tk.END, teks_dekripsi)

# Fungsi untuk menutup aplikasi
def close_app():
    root.quit()

# Membuat jendela GUI
root = tk.Tk()
root.title("Enkripsi dan Dekripsi DES")

# Set fullscreen
root.attributes("-fullscreen", True)

# Warna latar belakang dan teks
root.configure(bg="#1a1a1a")  # Latar belakang merah muda

# Menentukan grid layout untuk memastikan semua elemen terpusat
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Membuat dan menempatkan widget dengan warna dan font
label_style = {'font': ('Helvetica', 12), 'bg': '#ffcccc'}  # Warna merah muda
entry_style = {'font': ('Helvetica', 15), 'width': 100, 'bg': '#ffe6e6'}  # Latar belakang merah muda terang

tk.Label(root, text="Masukkan Teks Plain:", **label_style).grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_teks_plain = tk.Entry(root, **entry_style)
entry_teks_plain.grid(row=0, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Masukkan Kunci (8 karakter):", **label_style).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_kunci = tk.Entry(root, **entry_style)
entry_kunci.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Tombol Enkripsi dan Dekripsi
button_style = {'font': ('Helvetica', 12), 'bg': '#e60000', 'fg': '#ffffff', 'width': 200}  # Warna merah gelap
tk.Button(root, text="Enkripsi", command=enkripsi, **button_style).grid(row=2, column=0, columnspan=2, padx=10, pady=15)
tk.Button(root, text="Dekripsi", command=dekripsi, **button_style).grid(row=3, column=0, columnspan=2, padx=10, pady=15)

# Teks Enkripsi dan Dekripsi
tk.Label(root, text="Teks Enkripsi:", **label_style).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_teks_enkripsi = tk.Entry(root, **entry_style)
entry_teks_enkripsi.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Teks Dekripsi:", **label_style).grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_teks_dekripsi = tk.Entry(root, **entry_style)
entry_teks_dekripsi.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Tombol untuk menutup aplikasi
tk.Button(root, text="Tutup Aplikasi", command=close_app, font=('Helvetica', 12), bg='#cc0000', fg='#ffffff', width=15).grid(row=6, column=0, columnspan=2, pady=20)

# Menjalankan loop utama GUI
root.mainloop()
