# Python OOP - Abstract Class, Interface, Subclassing

## Table of Contents
1. Abstract Animal Class and its Subclasses
    - Setting up the Abstract Class
    - Implementing the Subclasses
2. Shapes, Interfaces, and Duck Typing
    - Shape Abstract Class
    - Circle and Rectangle Classes
    - shape_info Function
    - Testing
3. Extending the Python List with Notifications
    - Setting up the VerboseList Class
    - Implementing Notifications
    - Testing
4. CountedIterator - Keeping Track of Iteration
    - Setting up the CountedIterator Class
    - Overriding the next Method
    - Testing
5. The Enigmatic FlyingFish - Exploring Multiple Inheritance
    - Parent Classes Setup
    - Implementing FlyingFish
    - Testing and MRO Exploration
6. The Mystical Dragon - Mastering Mixins
    - Creating Mixins
    - Implementing Dragon
    - Testing the Dragon’s Abilities

## Abstract Animal Class and its Subclasses

### Setting up the Abstract Class
- Import the necessary components from the `abc` module.
- Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
- Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

### Implementing the Subclasses
- Create a subclass named `Dog` that inherits from the `Animal` class.
    - Implement the `sound` method in the `Dog` class to return the string “Bark”.
- Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
    - Implement the `sound` method in the `Cat` class to return the string “Meow”.

File: [task_00_abc.py](task_00_abc.py)

## Shapes, Interfaces, and Duck Typing

### Shape Abstract Class
- Define an abstract class `Shape` using the `ABC` package.
- Within `Shape`, declare two abstract methods: `area` and `perimeter`.

### Circle and Rectangle Classes
- Create a `Circle` class that inherits from `Shape`. The constructor (`__init__`) should accept a radius. Implement the `area` and `perimeter` methods.
- Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.

### shape_info Function
- Define a function named `shape_info` that takes a single argument.
- Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
- Print the area and perimeter of the shape passed to the function.

### Testing
- Instantiate a `Circle` and a `Rectangle`.
- Pass each object to the `shape_info` function and observe the output.

File: [task_01_duck_typing.py](task_01_duck_typing.py)

## Extending the Python List with Notifications

### Setting up the VerboseList Class
- Define a class `VerboseList` that inherits from the built-in `list` class.
- Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

### Implementing Notifications
- For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
- For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
- For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
- For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.

### Testing
- Instantiate a `VerboseList` object.
- Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.

File: [task_02_verboselist.py](task_02_verboselist.py)

## CountedIterator - Keeping Track of Iteration

### Setting up the CountedIterator Class
- Define a class `CountedIterator`.
- In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
- Provide a method `get_count` to return the current value of the counter.

### Overriding the next Method
- Within the `CountedIterator` class, override the `__next__` method.
- In this method, increment the counter each time the `__next__` method is called.
- Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.

### Testing
- Instantiate a `CountedIterator` object using a list or another iterable.
- Iterate over items using a loop or manual calls to the `__next__` method.
- Use the `get_count` method to retrieve and print the number of items that have been fetched.

File: [task_03_countediterator.py](task_03_countediterator.py)

## The Enigmatic FlyingFish - Exploring Multiple Inheritance

### Parent Classes Setup
- Create a `Fish` class with methods `swim` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
- Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).

### Implementing FlyingFish
- Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
- Override the `fly` method to print “The flying fish is soaring!”.
- Override the `swim` method to print “The flying fish is swimming!”.
- Override the `habitat` method to print “The flying fish lives both in water and the sky!”.

### Testing and MRO Exploration
- Instantiate an object of the `FlyingFish` class.
- Call the `fly`, `swim`, and `habitat` methods and observe the outputs.
- Use the `mro()` method or the `.__mro__` attribute on the `FlyingFish` class to investigate the method resolution order. For instance, `print(FlyingFish.mro())`.

File: [task_04_flyingfish.py](task_04_flyingfish.py)

## The Mystical Dragon - Mastering Mixins

### Creating Mixins
- Design a mixin called `SwimMixin` with a method `swim` that prints “The creature swims!”.
- Design another mixin called `FlyMixin` with a method `fly` that prints “The creature flies!”.

### Implementing Dragon
- Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
- Within the `Dragon` class, you can add additional methods or attributes if desired, such as `roar`, which could print “The dragon roars!”.

### Testing the Dragon’s Abilities
- Instantiate an object of the `Dragon` class named `draco`.
- Demonstrate `draco`‘s abilities by calling the `swim`, `fly`, and (if implemented) `roar` methods.

File: [task_05_dragon.py](task_05_dragon.py)
