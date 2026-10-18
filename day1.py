Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name="ronit"
age=22
hobby="Coding:
SyntaxError: incomplete input
>>> hobby="Coding"
>>> print(age)
22
>>> print(name)
ronit
>>> print(hobby)
Coding
>>> type(name)
<class 'str'>
>>> id(name)
1813915662896
>>> type(str(age))
<class 'str'>
>>> type(age)
<class 'int'>
>>> age=str(22)
>>> print(age)
22
>>> type(age)
<class 'str'>
>>> age=int(22)
>>> type
<class 'type'>
(
>>> type(age)
<class 'int'>
>>> married=False
>>> type(married)
<class 'bool'>
>>> <class 'bool'>
SyntaxError: invalid syntax
>>> print(married)
False
>>> parents={"papa","mummy"}
>>> type(parent)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    type(parent)
NameError: name 'parent' is not defined. Did you mean: 'parents'?
>>> type(parents)
<class 'set'>
>>> print(parents)
{'mummy', 'papa'}
>>> parents.append("bhaia"}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> parents.append{"bhaia}
...                
SyntaxError: unterminated string literal (detected at line 1)
>>> parents.append{"bhaia"}
...                
SyntaxError: invalid syntax
>>> parents.append("bhaia")
...                
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    parents.append("bhaia")
AttributeError: 'set' object has no attribute 'append'
>>> parents={"papa", "papa", "mummy"}
...                
>>> print(parents)
...                
{'mummy', 'papa'}
>>> type(parents)
...                
<class 'set'>
>>> skill=("C", "C++", "java", "python", "java")
...                
>>> skill.append("mysql")
...                
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    skill.append("mysql")
AttributeError: 'tuple' object has no attribute 'append'
>>> type(skill)
...                
<class 'tuple'>
>>> print(skill[1})
...                
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> print(skill[1])
...                
C++
skill[1]="r"
               
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    skill[1]="r"
TypeError: 'tuple' object does not support item assignment
lof=["abhijeet","harsh","harshit", "aniket"]
               
type(lof)
               
<class 'list'>
print(lof)
               
['abhijeet', 'harsh', 'harshit', 'aniket']
lof.pop()
               
'aniket'
print(lof)
               
['abhijeet', 'harsh', 'harshit']
lof.append("Sanu","Sahil")
               
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    lof.append("Sanu","Sahil")
TypeError: list.append() takes exactly one argument (2 given)
lof.append("Sanu")
               
print(lof)
               
['abhijeet', 'harsh', 'harshit', 'Sanu']
lof.append("Sahil")
               
print(lof)
               
['abhijeet', 'harsh', 'harshit', 'Sanu', 'Sahil']
lof.insert(0,"Aniket")
               
print(lof)
               
['Aniket', 'abhijeet', 'harsh', 'harshit', 'Sanu', 'Sahil']
lof[4]="piyush"
               
print(lof)
               
['Aniket', 'abhijeet', 'harsh', 'harshit', 'piyush', 'Sahil']
type(lof)
               
<class 'list'>
lof.remove("piyush")
               
print(lof)
               
['Aniket', 'abhijeet', 'harsh', 'harshit', 'Sahil']
phonebook={"sanu":7004832040, }
               
pb={"papa":9801188074, "mummy":7909067089, "raj":8294060133}
               
type(pb)
               
<class 'dict'>
pb.get("raj")
               
8294060133
