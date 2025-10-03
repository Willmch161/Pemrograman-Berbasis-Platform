try:
    num = int(input("Masukkan sebuah angka untuk dicek: "))
    is_prime = True

    if num <= 1:
        is_prime = False 
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False 
                break 
    
    if is_prime:
        print(f"Angka {num} adalah bilangan Prima.")
    else:
        print(f"Angka {num} BUKAN bilangan Prima.")
except ValueError:
    print("Input tidak valid. Masukkan bilangan bulat.")
print("-" * 30)