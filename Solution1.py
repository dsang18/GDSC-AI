def StringManipulation(str):
    # defining all alphabets
    alphabets = "abcdefghijklmnopqrstuvwxyzaABCDEFGHIJKLMNOPQRSTUVWXYZA"
    # defining all vowels
    vowels = "aeiouAEIOU"
    # initializing all strings 
    succeeding_alpha = ""
    inverted = ""
    inverted_wo_vowels = ""
    # looping through original string and replacing each alphabet with its succeeding one 
    for i in range(len(str)):
        if str[i] in alphabets:
            z = alphabets.index(str[i])
            succeeding_alpha+=alphabets[z+1]
        else:
            succeeding_alpha+=str[i]

    inverted = succeeding_alpha[::-1]
    temp = inverted
    inverted_wo_vowels += ''.join([temp[i] for i in range(len(temp)) if temp[i] not in vowels])

    print("\nOutput 1:\n",succeeding_alpha)

    print("\nOutput 2:\n",inverted_wo_vowels)

    print("\nOutput 3:\n",str[::2])



    
    

StringManipulation(input())