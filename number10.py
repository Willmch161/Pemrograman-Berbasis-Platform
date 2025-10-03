print("Tugas 10: Array Filtering (Adults Only)")
ages = [12, 18, 25, 30, 15]
ADULT_AGE = 18


adults = [age for age in ages if age >= ADULT_AGE]

print(f"Daftar usia: {ages}")
print(f"Usia 18 atau lebih (Dewasa): {adults}")

adults_manual = []
for age in ages:
    if age >= ADULT_AGE:
        adults_manual.append(age)
print(f"Usia 18 atau lebih (Manual): {adults_manual}")
print("-" * 30)