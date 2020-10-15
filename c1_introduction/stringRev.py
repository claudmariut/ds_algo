myName = "Clau"
myName.center(10)
print(myName.center(10))  # All string functions only return values.

print(myName.find('a'))

# Methods.
is_isogram = "isogram"
counter = 0
for digit in is_isogram:
    if is_isogram.count(digit) > 1:
        counter += 1

if counter == 0:
    print('True')

# Splits string at char, but deletes char.
print(is_isogram.split("o"))






