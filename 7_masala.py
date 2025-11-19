S = "sonlar.txt"

try:
    with open(S, "r") as f:
        numbers = [int(line.strip()) for line in f if line.strip() != ""]

    if len(numbers) > 4:
        print(numbers[0])     
        print(numbers[1])
        print(numbers[-2])
        print(numbers[-1])
    else:
        print("Faylda elementlar 4 tadan kam")
except:
    print("Fayl mavjud emas yoki xato")
