filenames = ["1.doc", "1.report", "1.presentation"]

# String transformation
# Replace . with - and add .txt
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]

print(filenames)
