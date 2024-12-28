while True:
    binary = input("Enter a binary number")
    if all(char in "01" for char in binary):
        break
    print("Invalid input.")
denary = 0


for i in range(len(binary)):
    if binary[len(binary) - 1 - i] == "1":  
        denary += 2**i
print(denary)
