print("\n2. Even or Odd Checker:")
try:
        num = int(input("  Masukkan angka: "))
        print(f"  Angka {num} adalah Genap." if num % 2 == 0 else f"  Angka {num} adalah Ganjil.")
except ValueError:
        print("  Input tidak valid.")