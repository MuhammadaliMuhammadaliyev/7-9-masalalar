import os


fayl1 = "fayl1.txt"
fayl2 = "fayl2.txt"


if os.path.isfile(fayl1) and not os.path.isfile(fayl2):
    mavjud = fayl1
    yangi = fayl2
elif os.path.isfile(fayl2) and not os.path.isfile(fayl1):
    mavjud = fayl2
    yangi = fayl1
else:
    raise Exception("Shartlar bajarilmagan: faqat bittasi mavjud bo'lishi kerak")


with open(mavjud, "r") as f:
    elements = [line.strip() for line in f if line.strip() != ""]


with open(yangi, "w") as f:
    f.write(elements[0] + "\n")
    f.write(elements[-1] + "\n")  
