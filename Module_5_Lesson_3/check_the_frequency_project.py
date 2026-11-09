test_dictionary = {
    'Codingal': 3,
    'is': 2,
    'best': 2,
    'for': 2,
    'Coding': 1
}

print(test_dictionary)

word = input("Enter the word you want to check: ")

if word in test_dictionary:
    print("Frequency:", test_dictionary[word])
else:
    print("Word not found in dictionary.")