# This summary points to the important parts of chapter

## 1.2 in an assignment statement such as  

    temp = 98.6

identifier  temp  references an instance of the float class having value 98.6
it is most similar to a reference variable in Java or a pointer variable in C++.

Each identifier is implicitly associated with the memory address of the object to which it refers.
A Python identifier may be assigned to a special object named None, seving a similar purpose to a null reference in Java or C++.

Although an identifier has no declared type, the object to which it refers has a definite type. **identifiers in python are case-sensitive**.

## Instantiation

There are 3 ways for instantiating an object (creating a new instance of a class):  

1. Invoke the constructor of class.  
1. By literal form (e.g.  temp=98.6)  
1. Call a function that creats and returns such an instance (e.g. built-in function named  sorted  that takes a sequence of elements and returns a new instance of the list class in sorted order)  

## Calling Methods

Methods are also known as "member functions", There are 2 types of Methods:  

* accessors: They return infromation about the state of an object but dont change that state(e.g. sort)  
* mutators: They do change the state of an object. such as list class.  

## Python Built-in Classes

A class is immutable if each object of that calss has a fixed value upon Instantiation that cannot subsequently be changed.  

Common mutable Built-in Classes are:  

* list  
* set  
* dict  

## Sequence Types: The list, tuple, and str Classes

Python does not have a seprate class for characters, they are just "strings" with lenght one.  

## The list class

* It is a referential structure, as it technically stores a sequence of references to its elements.  

## The set and frozenset Classes

2 important restrictions due to the algorithms underpinnings:  

1. the set does not maintain the elements in any particular order.  
2. only instances of immutable types can be added to a python set.(but we can a have a set of frozensets)  

* frozenset set class is an immutable form of the set type.

* python uses curly braces { hi } as delimiters for a set, for example, but there is an exception to this rule that { } does not represent an empty set (because it represents  dictionary  which introduced in python prior to sets)  

## 1.3 Equality operators

when you write  a is b (which  is  evaluates to True) a  and  b  are aliases for the same object.  

## Sequence operators

* All sequences (except Sets and Dictionaries) define comparison operations based on   lexicographic order, performing an element by element comparison until the first differece is found.  

* Sets and Dictionaries do not guarantee a particular order of their elements, so the comparison operators, such as < are not lexicographic; rather, they are based on the mathematical notion of a subset.  

## Extended Assignment Operators

there is a differece between  ...+=...  operator and   ...=...+... operator; an example code:  

* alpha = [1, 2, 3]  
* beta = alpha             #an alias for alpha  
* beta += [4, 5]           #extends the original list with tow more elements  
* beta = beta + [6, 7]     #reassigns beta to a new lis [1, 2, 3, 4, 5, 6, 7]  
* print(alpha)             #will be [1, 2, 3, 4, 5]  

## 1.4 Functions

Function's signature: The first line, beginning with the keyword  def , is function's signature, this stablishes:  

* a new identifier as the name of the function  
* the number of parameters that it excepts  
* names identifying those parameters  

Activation record: Each time a function is called, Python creats a dedicated  activation record that stores infromation relevant to the current call.  
This  activation record  includes a  namespace  to manage all identifiers that have local scope  within the current call.  

## Return Statement

If a  return statement is executed wihtout an explicit argument, the  None  value is automatically returned.  
also, None  will be returned if the flow of control ever reaches the end of a function body wihtout having executed a return statement.  

## Infromation Passing

There are 2 main concepts of parameters in functions:   -Formal parameters: The identifiers  used to describe the excepted parameters.

Actual parameters: The objects sent by the caller when invoking the function.

consider following function:  

    def count(data, target):
        n = 0
        for item in data:
            if item == target:
                n += 1
            return n

and after that we made following call to that function:
prizes = count(grades, 'A')

which by that python will make these assignments

    data = grades
    target = 'A'

* These assignment statements establish identifier  data  as an alias for grades and target as a name for the string literal 'A'.  

* The  communications of a return value from the function back to the caller is impemented as an assignment. (e.g.  the identifier  prizes  in the caller's scope is assigned to the object that is identified as  n  in the return statement within our function body.)  

* An advantage to Python's mechanism for passing infromation to and from a function is that objects are not copied.

* If a command like  data.append('F')  executes  in the body of the function, the new entry is added to the end of the list  identified as  data  within the function , which  is the one list known to the caller as  grades.  

but reassigning a new value to a formal parameter with a function body, such as by setting  data = [], does not 
alter the actual parameter with a function body;   such a reassigning simply breaks the alias.

Polymorphic Functions (functions that have Default Parameter Values)

* It is illegal to define a function with a signature such as   bar(a, b=15, c) ; If a default parameter value is present for one parameter;  it must be present for all further parameters. (so in bar function, c must have a default value)  

## 1.7

isinstance(obj, cls)  is a boolean built-in function which is used for checking the type of an object at run-time.

## Catching an Exception
Exceptions are objects that can be examined when caught.
When an error is raised within the try-block, the remainder of that body is immediately skipped.  

Two usefull features of  try-except  structure

1. It is permissible to have a final except-clause wihtout any identified error types using  except: to catch any  exception that occurred.  

2. A try-statement can have a finally clause, with a body of code that will always be executed in the standard or exceptional cases, even when an uncaught or re-raised exception occurs. (That block is typically used for critical cleanup work, such as closing an open file.)  

## 1.8 Iterators and Generators

Iterators:

* An iterator is an object that manages an iteration through a series of values.  

A  StopIteration  exception will raise when we have no further elements in our series of values.  

* An  iterable  is an object, obj, that produces an iterator via the syntax iter(obj).  

An iterator object can be produced with syntax in second line of below code:

    data = [1,2,4,8]
    i = iter(data)

* An instance of a list is an iterable, but not itself an iterator.

* It is possible to create multiple iterators based upon the same iterable object, with each iterator maintaining its own state of progress

* An iterator does not store its own copy of the list of elements. Instead, it maintains a current  index  into the original list, representing the next element to be reported.

* Python also supports functions and classes that produce an implicitl iterable series of values, that is, wihtout constructing a data structure to store all of its values at once. For example, the call  range(1000)  does not return a list of numbers; it returns a range object that is iterable. This object generates the thousand values one at a time, and only as needed.   This technique is also called   lazy evaluation.

## Generators:

The most convenient technique for creating iterators in python is through the use of  generators.  
A generator is impemented with a syntax that is very similar to a function, but instead of returning values, a  yield statment is executed to indicate each element of the series.  

## 1.9 Packing and Unpacking of sequences

Python provides two conveniences involving the treatment of tuples and other sequence types.
If a series of comma=seprated expressions are given in a larger context, they will be treated as a single tuple, for example:  

    data = 2, 4, 6, 8

This behavior is called  automatic packing  of a tuple.

* One common use of packing in Python is when returning multiple values from a function. If the body of a function executes the command,

    return x,y
    
=======
1.9
## Comprehension Syntax:
   A very common programming task is to produce one series of values based upon
   the processing of another series. As an example the the general form of list comprehension is:
    
        [ expression for value in iterable if condition ]



    [ k*k for k in range(1, n+1) ]          list comprehension
    { k*k for k in range(1, n+1) }          set comprehension
    ( k*k for k in range(1, n+1) )          generator comprehension
    { k : k*k for k in range(1, n+1) }      dictionary comprehension

    **  The generator syntax is particularly attractive when results do not need to be stored
      in memory. For example, to compute the sum of the first n squares, the generator 
      syntax, total = sum(k*k for k in range(1, n+1)), is preferred to the use of an
      explicitly instantiated list comprehension as the parameter.
    

Packing and Unpacking of sequences:
    Python provides two conveniences involving the treatment of tuples and other sequence types.
    If a series of comma=seprated expressions are given in a larger context, they will be treated as a single tuple, 
    for example:
    data = 2, 4, 6, 8
    This behavior is called  automatic packing  of a tuple.

it will be formally returning a single object that is the tuple (x, y).  
As a dual to the packing behavior, python can automatically  unpack  a sequence, allowing one to assign a series of individual identifiers to the elements of sequence. As an examplem we can write

    a, b, c, d = range(7, 11)

## Simultaneous assignments

The combination of automatic packing and Unpacking forms a technique known as  Simultaneous assignment.  
Following line is an example of simultaneous assignment:

    x, y, z = 6, 2, 5

or

    j, k = k, j

When python is performing simultaneous assignment, all of the expressions are evaluated on the right-hand side before
any of the assignments are made to the left-hand variables.

## 1.10 Scopes and Namespaces

Name resolution:
The process of determining the value associated with an identifier.

Scope:
Whenever an identifier is assigned to a value, that definition is made with a specific  scope.

Namespace:
Each distinct scope in Python is represented using an abstraction known as a  namespace.
A namespace manages all identifiers that are currently defined in a given scope.

* Python implements a namespace with its own dictionary that maps each identifying string to its associated value.

* When an identifier is indicated in command, Python searches a series of namespaces inthe process of name resolution. First, the most locally enclosing scope is searched for a given name. If not found there, the next outer scope is searched and so on.

* Each object has its own namespace to store its attributes, and that classes each have namespace as well.

## First-Class objects

They are instances of a type that can be assigned to an identifier, passed as a parameter, or returned by a function.  
In Python, functions and classes are also treated as first-class objects. For example:

    scream = print      # assign name 'scream' to the function denoted as 'print'
    scream('Hello')     # call that function

Within the body of that function, the formal parameter, key, is an 

## 1.11 Modules and the Import Statement

### Pseudo-Random Number Generation

Python's random module uses a deterministic formula to generate the next number in a sequence based upon one or more past numbers that it has generated. Because of this functionality we call it Pseudo-Random generator.  

Since the next number in a pseudo-random generator is determined by previous number(s), such a generator always needs a place to start, which is called its  SEED. The sequence of numbers generated for a given seed will always be the same.  
