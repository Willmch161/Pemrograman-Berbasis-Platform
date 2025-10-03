print("\n5. Multiplication Table Generator:")
try:
        num = int(input("  Masukkan angka: "))
        for i in range(1, 11):
            print(f"  {num} x {i} = {num * i}")
except ValueError:
        print("  Input tidak valid.")