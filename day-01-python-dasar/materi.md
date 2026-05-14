# Day 01 — Python Dasar

## Materi yang Dipelajari

Pada hari pertama, saya mempelajari dasar-dasar Python, yaitu:

- Menjalankan file Python
- Variable
- Tipe data dasar
- Input dari user
- Output menggunakan print
- Format output menggunakan f-string
- Konversi tipe data menggunakan int()

## Ringkasan Materi

Variable digunakan untuk menyimpan data.

Contoh:

```python
nama = "El"
semester = 6
```

Python memiliki beberapa tipe data dasar:

| Tipe Data | Contoh |
|---|---|
| String | "El" |
| Integer | 6 |
| Float | 3.75 |
| Boolean | True |

Input dari user dapat diambil menggunakan fungsi `input()`.

```python
nama = input("Masukkan nama: ")
```

Jika input ingin digunakan sebagai angka, maka perlu dikonversi.

```python
umur = int(input("Masukkan umur: "))
```

f-string digunakan untuk menampilkan output yang berisi variable.

```python
print(f"Halo, nama saya {nama}")
```