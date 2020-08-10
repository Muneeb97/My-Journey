dict = {}
dict['Hot']=['balmy','summery','tropical','boiling']
dict['Cold']=['chilly','cool','freezing','icy']
dict['Happy']=['contented','content','cheerful','cheery']
dict['Sad']=['unhappy','sorrowful','dejected','regretful']

print("Welcome to the thesaurus")
print("These are the current words in the thesaurus: ")

for keys,values in dict.items():
    print("\t",keys)

word = input("For which word would you like a synonym of? ")

for keys,values in dict.items():
    if(keys.upper() == word.upper()):
        print("These are the synonyms of the word {}".format(keys))
        for i in values:
            print('\t',i)
    
    print("Not present in the thesaurus\n")


ys_no = input("Would you like to see the whole thesaurus y/n? ")
if(ys_no.upper() == "Y"):
    for keys,values in dict.items():
        print("Synonym of {} are: ".format(keys))
        for i in values:
            print('\t',i)
        print('\n')
else:
    print("Thankyou for using the thesaurus")
