from collections import Counter

corpus = ["the cat sat", "the cat ate", "the dog ran"]

dict={}
get_each_word = " ".join(corpus).split()  # Split the corpus into individual words
# print(get_each_word)  # Output: ["the", "cat", "sat", "the", "cat", "ate", "the", "dog", "ran"]


 # List comprehension to flatten the list of words
count = 0
for data in get_each_word:
    print(data)
    if(not dict.get(data)):
        dict[data]=count + 1

    else:
        print("inside else")
        dict[data]= dict.get(data) + 1



print(dict)
#  // Output: {'the': 3, 'cat': 2, 'sat': 1, 'ate': 1, 'dog': 1, 'ran': 1}