i  = 'Chineye said: \'Who\'s there\'' 
print(i[-1])

j = 'Chiazam said: \'What\'s up with you girl?'
print(j[1])


k = "Chiazam is a spec"
print(k[7])

l = """Hello there
reallly!!!!!!!!!!!!!""" # 3 quotations is used for typing code in multiple lines  
print(l[-1])

# Acessing characters from strings (Index is beside the print call in the above examples )
# For slicing, the 1st index is inclusive but the last index isn't. eg. below

m = 'ICE Commercial Power'
print(m[-1:-6]) # Neagtive indexing doesn't work for slicing a string probably because it will slice it backwards
print(m[0:3])
print(m[0:-1])
print(m[0:-5])
print(m[:-1]) # : - starts from first character 
print(m[4:]) # continues to last character 
#m[0] = 'E'  # You can't change characters in a string using index but replace .... further down
print(m)

# Concatenation
n = 'Food'
o = 'is'
p = 'sweet.'
q = ' '
join = n+q+o+q+p
print(join)
join2 = n+q+'is'+q+p
print(join2)

r = p * 3
print(r)

for character in n:
    print(character)

print(len(n))

print('d' in n) # d is in n(Food) [true]
print('do' in n) # do is not in the correct order in n(Food) [false]
print('od' in n) # od is in the correct order in n(Food) [true]

#String methods

s = 'Chiazam is a good girl.' 
result = s.lower() # Change to lower case
print(result)
result2 = s.upper() # Change to upper case
print(result2)
result3 = s.find('l') # Change the index number for a character or word
print(result3)
result4 = s.find('girl') # For a word, it will give the index of the 1st letter. 
print(result4)
result5 = s.replace('good', 'bad') # replacing a word
print(result5)

# Replacing a letter 
m = 'ICE Commercial Power'
replace = m.replace('I','E')
print(replace)

quote = "Talk is cheap. Show me the code."
print('1.',quote[3])
print('2.',quote[-3])
print('3.',quote.replace('code','program'))



