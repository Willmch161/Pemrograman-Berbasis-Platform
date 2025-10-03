print("Tugas 4: Grade Checker")
try:
    score = int(input("Masukkan skor siswa (0-100): "))
    
    if 90 <= score <= 100:
        grade = "A" 
    elif 80 <= score <= 89:
        grade = "B" 
    elif 70 <= score <= 79:
        grade = "C" 
    elif 0 <= score < 70:
        grade = "Fail" 
    else:
        grade = "Skor tidak valid (di luar rentang 0-100)"
        
    print(f"Skor {score} mendapatkan nilai: {grade}")
except ValueError:
    print("Input tidak valid. Masukkan bilangan bulat.")
print("-" * 30)