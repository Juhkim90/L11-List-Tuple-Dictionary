## List
A data structure that is a mutable (changeable) ordered sequence of elements.
Defined by having values between square brackets, [].

*Ex.*
``` python
box = ["Anything", 123, True, 4.21, -13]

name = ["John", "Chloe", "Ian", "Ashley"]
print (name)
```
> ["John", "Chloe", "Ian", "Ashley"]

### Indexing List
Each item in a list corresponds to an index number, which uses aniteger; starting with 0.

*Ex.*
``` python
name = ["John", "Chloe", "Ian", "Ashley"]
print (name[2])
```
> Ian

### List Functions
	- LIST.append(ELEMENT)			# Add an item to the end of the list
	- LIST.index(INDEX, ELEMENT)		# Insert an item at a given index
	- LIST.remove(ELEMENT)			# Search the item and remove it
	- LIST.pop(INDEX)			# Remove the item at a given index

## Tuple
One of the type of lists, which stores data/values inside parenthesis, ( ).
Unlike a list, it cannot be changed (they are immutable).
It still uses an index like a list.

*Ex.*
```python
color = ("Blue", "Red", "Black", "Yellow", "White", "Cyan")
print (color[5])
```
> Cyan

## Dictionary
Another type of list, stores data/values inside the curly brackets, { }.
Simiar to a list, it is mutable, however, the index is a key, which is linked to data/values.

*Ex.*
```python
student = {}
student["name"] = "John"
student["age"] = 12
student["weight"] = 110
student["school"] = "Evergreen"
student["Python"] = True
print (student)
print (student["age"])
```
> {'name':'John', 'age':12, 'weight':110, 'school':'Evergreen', 'Python':True}
> 12