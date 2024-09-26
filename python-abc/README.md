# Python - Abstract Classes and Interfaces

## Table of Contents
1. Abstract Animal Class and its Subclasses
2. Shapes, Interfaces, and Duck Typing
3. Extending the Python List with Notifications
4. CountedIterator - Keeping Track of Iteration
5. The Enigmatic FlyingFish - Exploring Multiple Inheritance
6. The Mystical Dragon - Mastering Mixins

## Abstract Animal Class and its Subclasses

### Background
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s ABC package facilitates the creation of abstract base classes.

### Objective
- Create an abstract class named `Animal` using the ABC package. This class should have an abstract method called `sound`.
- Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

### Resources
- Python ABC documentation

### Instructions

#### Setting up the Abstract Class
1. Import the necessary components from the `abc` module.
2. Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
3. Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

#### Implementing the Subclasses
1. Create a subclass named `Dog` that inherits from the `Animal` class.
    - Implement the `sound` method in the `Dog` class to return the string “Bark”.
2. Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
    - Implement the `sound` method in the `Cat` class to return the string “Meow”.

### Hints
- The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
- If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a `TypeError`.

### File
- [task_00_abc.py](task_00_abc.py)

## Shapes, Interfaces, and Duck Typing

### Background
Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

### Objective
- Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
- Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
- Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.
- Test the `shape_info` function with instances of both `Circle` and `Rectangle`.

### Resources
- Python ABC documentation
- Concept of Duck Typing

### Instructions

#### Shape Abstract Class
1. Define an abstract class `Shape` using the ABC package.
2. Within `Shape`, declare two abstract methods: `area` and `perimeter`.

#### Circle and Rectangle Classes
1. Create a `Circle` class that inherits from `Shape`. The constructor (`__init__`) should accept a radius. Implement the `area` and `perimeter` methods.
2. Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.

#### shape_info Function
1. Define a function named `shape_info` that takes a single argument.
2. Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
3. Print the area and perimeter of the shape passed to the function.

#### Testing
1. Instantiate a `Circle` and a `Rectangle`.
2. Pass each object to the `shape_info` function and observe the output.

### Hints
- While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
- Duck typing in the `shape_info` function implies that you shouldn’t use `isinstance` checks. Instead, trust that the passed object adheres to the `Shape` interface.

### File
- [task_01_duck_typing.py](task_01_duck_typing.py)

## Extending the Python List with Notifications

### Background
In Python, you can extend built-in classes to add or modify behavior. The list class provides a collection of methods and functionalities that handle list operations. By extending the list class, you can provide custom behaviors while retaining the original functionalities.

### Objective
Create a class named `VerboseList` that extends the Python list class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).

### Instructions

#### Setting up the VerboseList Class
1. Define a class `VerboseList` that inherits from the built-in `list` class.
2. Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

#### Implementing Notifications
1. For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
2. For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
3. For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
4. For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.

#### Testing
1. Instantiate a `VerboseList` object.
2. Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.

### Hints
- Remember to call the original method of the list class using the `super()` function to ensure that the original functionality is retained. For example, for `append`: `super().append(item)`.
- Think about edge cases, such as trying to remove an item that doesn’t exist in the list.

### File
- [task_02_verboselist.py](task_02_verboselist.py)

## CountedIterator - Keeping Track of Iteration

### Background
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The `iter` function, which returns an iterator object, provides the `__next__` method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

### Objective
Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the `__next__` method to increment a counter each time an item is fetched.

### Instructions

#### Setting up the CountedIterator Class
1. Define a class `CountedIterator`.
2. In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
3. Provide a method `get_count` to return the current value of the counter.

#### Overriding the next Method
1. Within the `CountedIterator` class, override the `__next__` method.
2. In this method, increment the counter each time the `__next__` method is called.
3. Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.

#### Testing
1. Instantiate a `CountedIterator` object using a list or another iterable.
2. Iterate over items using a loop or manual calls to the `__next__` method.
3. Use the `get_count` method to retrieve and print the number of items that have been fetched.

### Hints
- Remember that the `__next__` method should raise a `StopIteration` exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
- You can initialize the iterator object in the `CountedIterator` constructor using: `self.iterator = iter(some_iterable)`.

### File
- [task_03_countediterator.py](task_03_countediterator.py)

## The Enigmatic FlyingFish -
