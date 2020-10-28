#program prints unique words in a string
string = input("Enter a string ")
words = string.split(" ")
unique = []
for word in words:
  if word not in unique:
    unique.append(word)
    
    
for word in unique:
  print(word)
