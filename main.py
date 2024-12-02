with open ("raqamlar", "w") as file:
    for i in range(10):
        file.write(str(i)+ "\n")

count = 0

with open ("raqamlar", "r") as file:
    for line in file:
        count += 1

print(count)
        
