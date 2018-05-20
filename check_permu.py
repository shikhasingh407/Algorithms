
def check_permutation(x, y):

    str1 = list(x)
    str2 = list(y)
    str1.sort()
    str2.sort()

    if str1 == str2:
        print("True")
    else:
        print("False")

check_permutation("shikha", "shikah")


