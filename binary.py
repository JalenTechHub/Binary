while True:
    binary = "1010101"
    if all(char in "01" for char in binary):
        break
    print("Invalid input.")
denary = 0

# Loop through the binary string from right to left using a simple index
for i in range(len(binary)):
    if binary[len(binary) - 1 - i] == "1":  # Access characters from the end
        denary += 2**i
print(denary)