import time
#ex. 1
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

print()
#ex. 2
for digit in "0165031806510":
    if digit == "0":
        print("x", end = "")
    else:
        print(digit, end = "")

print()

time.sleep(2)