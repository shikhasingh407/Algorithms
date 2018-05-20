import string

def numberOfLines(widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        sum1 = 0
        counter = 1
        extra = 0
        line = 100

        for char1 in S:
            sum1 = sum1 + (widths[string.ascii_lowercase.index(char1)])

        if sum1 < line:
            return [1, sum1]

        for index in range(0, len(S)):
            if (line > 0) and (line >= (widths[string.ascii_lowercase.index(S[index])])):
                line = line - (widths[string.ascii_lowercase.index(S[index])])
                sum1 = sum1 - (widths[string.ascii_lowercase.index(S[index])])

            else:
                counter = counter + 1
                line = 100
                print (S[index])
                index-=1
                print (S[index])


            if (sum1 < line):
                break
            else:
                continue

        print(counter, sum1)

#         for k,v in alphaValueDict.iteritems():
#             alphaValueDict[k] = [for width in range(len(widths))]
#         print (alphaValueDict)

widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
numberOfLines(widths, S)