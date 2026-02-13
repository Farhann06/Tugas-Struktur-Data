# Membuat array dengan ukuran tetap
size = 5

if size <= 0:
    print("Ukuran array harus lebih dari 0")
else:
    arr = [None] * size   # semua elemen diisi None

# Menampilkan panjang array
print("Panjang array:", len(arr))

# Mengisi nilai
arr[0] = 10
arr[1] = 20
arr[2] = 30

print("\nIsi array setelah diisi:")
for item in arr:
    print(item)

# Mengambil nilai tertentu
print("\nNilai pada index 1:", arr[1])

# Mengosongkan array dengan nilai 0
for i in range(len(arr)):
    arr[i] = 0

print("\nIsi array setelah clear:")
for item in arr:
    print(item)
