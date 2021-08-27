# A dictionary is a collection of key value pairs - compd data type
# Made up of key and value, key can't be modified like lists - It's eithee string, tuple or number 
# Immutable - it can't change over time

dictionary = {'name':'Chiazam', 'age': 21} #see the difference between list and tuples 
print(dictionary)
print(dictionary['name'])
print(dictionary['age'])   #accessing dictionaries 
#print(dictionary['Sochi'])  #confirming if key is in the dictionary 
print(dictionary.get('school'))  # response is none because get call has been added instead of an error message like the previous line 
print(dictionary.get('age'))
print(dictionary.get('school',['rp', 'meamater','grundtvig']))
# You can't change the key, only the value 
# CHANGING VALUES 
dictionary['age'] = 20
print(dictionary)
# ADDING NEW KEYS TO DICTIONARY: if key is not in the dictionary when trying to change value of a key, it will bw added as a new key
dictionary['school'] = ['rp', 'meamater','grundtvig']
print(dictionary)

#REMOVING KEYS FROM DICTIONARY - pop
print(dictionary.pop('age')) # remove age from dictionary 
print(dictionary) # print new distionary 

# ITERATE THROUGH DICTIONARY 
for key in dictionary:
    print(key)
    print(dictionary[key])

# EXAMPLES 
synonyms = {'mountain':'peak','forest':'jungle'}
print('1.', synonyms['mountain'])
synonyms['terrain'] = 'land'
print('2.', synonyms)
synonyms.pop('forest')
print('3.',synonyms)

# Updating dictionaries 
synonyms['sky'] ='blue'
print(synonyms)
synonyms.update({'trees': 'brown & green'})
print(synonyms)
synonyms.update([('leaves', 'chorophyll'),('ground','loamy soil')])
print(synonyms)

# MERGING 2 DICTIONARIES 
dictionary.update(synonyms)
print(dictionary)