import os

fayl1 = "birinchi.txt"
fayl2 = "ikkinchi.txt"


if os.path.isfile(fayl1):
    with open(fayl1, "r") as f:
        numbers = [line.strip() for line in f if line.strip() != ""]

    if numbers:
        if not os.path.isfile(fayl2):
            with open(fayl2, "w") as f2:
                f2.write(numbers[0] + "\n")
                f2.write(numbers[-1] + "\n")
