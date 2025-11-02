import random

# Generate a 3-digit code: each digit 0-9
code_3 = [random.randint(0, 9) for _ in range(3)]

# Generate a 4-digit code: each digit 1-6
code_4 = [random.randint(1, 6) for _ in range(4)]

# Print them in a couple of readable formats
print("3-digit code (digits 0–9):", "".join(map(str, code_3)))
print("3-digit code (separated):", " ".join(map(str, code_3)))
print("4-digit code (digits 1–6):", "".join(map(str, code_4)))
print("4-digit code (separated):", " ".join(map(str, code_4)))
