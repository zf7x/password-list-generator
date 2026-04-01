import random

names = ["ziyad", "youssef", "hamza", "karim"]
symbols = ["@", "_", "-", "!", "123"]
numbers = list(range(0, 100))

output_file = "passwords.list"
count = 0

with open(output_file, "w") as f:
    for name in names:
        for num in numbers:
            for sym in symbols:
                variations = [
                    f"{name}{num}",
                    f"{name}{sym}{num}",
                    f"{name.capitalize()}{sym}{num}",
                    f"{name}{num}{sym}",
                    f"{name.upper()}{num}"
                ]

                for v in variations:
                    f.write(v + "\n")
                    count += 1

print(f"[+] Generated {count} passwords")
print(f"[+] Saved in {output_file}")
