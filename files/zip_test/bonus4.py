# String manipulation. Change first instance of . to -
# Strings are immutable, meaning that individual characters within a string cannot be reassigned
# So, we need to use the replace method on the string.
# List []
filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for name in filenames:
    print(name.replace('.', '-', 1))


# Tuple ()
# Immutable. Cannot assign or append things to tuple.
filenames = ('1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt')
