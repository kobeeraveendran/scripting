input_text = input("Enter text: ")
print("Character count (including spaces): " + str(len(input_text)))
print("Character count (excluding spaces): " + str(sum(len(x) for x in input_text.split())))
print("Word count: " + str(len(input_text.split())))
