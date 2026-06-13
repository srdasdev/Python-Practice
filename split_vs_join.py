# split vs join
# split() method is used to split a string into a list of substrings based on a specified delimiter.
# join() method is used to concatenate a list of strings into a single string, using a

# Split -> string to list
sentence = "Hello, how are you?"
words = sentence.split()  # Default delimiter is whitespace
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']
# Join -> list to string
joined_sentence = ' '.join(words)  # Join the list back into a string with spaces
print(joined_sentence)  # Output: "Hello, how are you?"


# You can also specify a different delimiter for split and join
csv_string = "apple,banana,cherry"
fruits = csv_string.split(',')  # Split by comma
print(fruits)  # Output: ['apple', 'banana', 'cherry']
joined_csv = ';'.join(fruits)  # Join with a semicolon
print(joined_csv)  # Output: "apple;banana;cherry"

