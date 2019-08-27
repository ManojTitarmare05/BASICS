# To find the number of occurences of substring in main string
# You will learn the usage of find() function

"""
Date : 27-08-2019 written by Manoj Titarmare
"""

mstring = input('enter your main string')
subs = input('enter your sub-string to be searched in main string')

i = mstring.find(subs)  # searches for the first occurence of sub-string in main string
if i==-1:
    print('substring not found!!')
while i!=-1:
    print('{} present at index :{}'.format(subs,i))
    i = mstring.find(subs,i+len(subs),len(mstring)) # search in the remaining main string
total_occurences = mstring.count(subs)
print("total number of occurences of substring '{}' is {}".format(subs,total_occurences))