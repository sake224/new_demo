## initializing string
string = "tokyo"
## initializing a dictionary
duplicates = {}
for z in string:
   ## checking whether the char is already present in dictionary or not
   if z in duplicates:
      ## increasing count if present
      duplicates[z] += 1
   else:
      ## initializing count to 1 if not present
      duplicates[z] = 1
for key, value in duplicates.items():
   if value > 1:
      print(key, end = " ")
print()