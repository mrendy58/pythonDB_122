import sqlite3
import tkinter as tk

# Membuat koneksi ke database SQLite
conn = sqlite3.connect('Topic8db.db')
c = conn.cursor()

# Membuat tabel nilai_siswa
c.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_siswa TEXT,
                biologi INTEGER,
                fisika INTEGER,
                inggris INTEGER,
                prediksi_fakultas TEXT
            )''')

# Fungsi untuk menentukan prediksi fakultas
def prediksi_fakultas(nama, nilai_biologi, nilai_fisika, nilai_inggris):
    if nilai_biologi > nilai_fisika and nilai_biologi > nilai_inggris:
        prediksi = "Kedokteran"
    elif nilai_fisika > nilai_biologi and nilai_fisika > nilai_inggris:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"
    return prediksi

# Fungsi untuk menyimpan data ke database
def submit_nilai():
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
    prediksi = prediksi_fakultas(nama, biologi, fisika, inggris)
    c.execute("INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
              (nama, biologi, fisika, inggris, prediksi))
    conn.commit()
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END) 

# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = tk.Label(root, text="Nilai Biologi")
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = tk.Label(root, text="Nilai Fisika")
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = tk.Label(root, text="Nilai Inggris")
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1)

button_submit = tk.Button(root, text="Submit", command=submit_nilai)
button_submit.grid(row=4, column=0, columnspan=2)

root.mainloop()