#enter a specific letter to count the number of times it is present in the sentence.
import re
string = input('Enter a sentence\n').upper()
letter=input('Which letter to find\n').upper()
def count(letter,string):
    wrd_count = re.findall(r"['{}']".format(letter),string)
    print("The number of times letter {} is present is # ".format(letter),len(wrd_count))
    
count(letter,string)