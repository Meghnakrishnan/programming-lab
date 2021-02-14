#Form a list of vowels selected from a given word

w=input("enter a word:")    #input a word
vowels=['a','e','i','o','u']    #store vowels list in vowels
vowel_list=[i for i in w if i in vowels]
print("vowels",vowel_list)


'''output
enter a word:rainbow
vowels ['a', 'i', 'o']
'''
