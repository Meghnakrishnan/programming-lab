#Form a list of vowels selected from a given word

str="umbrella"
vow="aeiou"
res=[] #initialising list to store vowels in list
#to check whether the sting contains any vowels or not and print if any present
for x in str:
    for j in vow:
        if x==j:
            res.append(x)
        else:
            pass
print("vowels in %s are:" %str,res)        

#output
vowels in umbrella are: ['u', 'e', 'a']
