from collections import defaultdict

d = defaultdict(list)
d["fruits"].append("apple")
d["fruits"].append("banana")
d["veggies"].append("carrot")
# print(dict(d))


from collections import defaultdict

# dataset = [
#     ("cat", "image1"), ("dog", "image2"),
#     ("cat", "image3"), ("dog", "image4"), ("bird", "image5")
# ]

# grouped = defaultdict(list)

# for label, image in dataset:
#     grouped[label].append(image)

# print(dict(grouped))



students = [
    ("soumya", "AI", 82),
    ("raj", "ML", 45),
    ("priya", "AI", 91),
    ("amit", "ML", 78),
    ("sara", "AI", 38)
]


# Group students by department, but only include students who scored above 50. Use defaultdict.

grouped = defaultdict(list)
for name,department,marks in students:
    if(marks > 50):
        grouped[department].append(name)
print(dict(grouped))

# {'cat': ['image1', 'image3'], 'dog': ['image2', 'image4'], 'bird': ['image5']}