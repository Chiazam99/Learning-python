#  Immutable objects = strings, tuples and numbers are used
# Can't be mutable objects like: lists and dictionaries
# Items of a set are not in any partivular order
# Items can't b e repeated 
# no duplicate items are allowed. 

#EXAMPLES 
animals = {'mum', 'dad', 'muna','meso','zammy','gee','dochima'}
print(animals)
animals = {'mum','mum','gee','dad', 'muna','meso','zammy','gee','dochima'}
print(animals)
# Empty set
empty_set = set()
print(empty_set)

# Lists and tuples, dictionaries, strings  can be converted into a set using the set function 
leest = [1,2,3,4,'ri','pi']
print(set(leest))
tupel = ( 'tie',45,'rest','tea')
print(set(tupel))
dictonaray =  {'mountain':'peak','forest':'jungle'}
print(set(dictonaray))
string = 'James'
print(set(string))
# number = 123456789
# print(set(number))  wouldn't run beacause it number variable can;t be converted to set 

# ADDING & REMOVING ITEMS TO A SET 
print(animals.add('gorilla'))
print(animals.remove('mum')) # will return an error message if ran and value in bracket is not in the set. 
print(animals)
print(animals.discard('tissue')) # works like remove but will run when value in bracket is not in the set. 

# ADDING SET,LIST,TUPLES,STRINGS & DICTIONARIES TO A SET - UPDATE
birds = {'peguin', 'chicken', 'duck','goose'}
animals.update(birds)
print(animals)

# CLEAR A SET 
#animals.clear()
#print(animals)

# CHECK IF AN ITEM IS IN THE SET 
print('giraffe' in animals)
print('chicken' in birds)

for animal in animals:
    print(animal)

# UNION AND INTERSECTION OF SETS 
insects = {'cockroach','mot','grasshopper','duck'}
animals2 = birds.union(insects)  #   --- or ---
print(animals2)
animals4 = animals | insects  # note the symbol 
print(animals4)
animals3 = birds.intersection(insects)
print(animals3)
others = {'goat', 'cow', 'duck','chicken'}
animals5 = animals&others
print(animals5)