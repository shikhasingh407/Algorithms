#


def unique_string(x):
    dict1 = {}
    for char in range(len(x)):
        if x[char] in dict1.values():
            print("False")
        else:
            dict1[char] = x[char]
            print("True")

    print("unique elements in dictionary", dict1)


unique_string("shikshiha")