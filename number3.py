print("\n3. Simple Calculator (Addition):")
try:
        n1 = float(input("  Angka pertama: "))
        n2 = float(input("  Angka kedua: "))
        print(f"  Hasil penjumlahan: {n1 + n2}")
except ValueError:
        print("  Input tidak valid.")