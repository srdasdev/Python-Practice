list2 = [1,2,3,4,5]

it = iter(list2)
while(True):
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break



