# To print First and Last character of string in Uppercase and remaining to lowercase

s = input('enter the string : ')
print(s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper())

