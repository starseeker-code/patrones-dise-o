# Design patterns - A review with different languages

**Author**: [Joaquin Hernandez Martinez](https://github.com/starseeker-code)

This is a personal repository aiming to document and store all main design patterns in Python, Typescript, Go and Rust programming languages. A comprehensive index will be provided in order to navigate this repository.

## Index

### Creational patterns

* [Factory](#factory) --->  [Python](https://github.com/starseeker-code/patrones-diseno/blob/main/Python/factory.py) | [Typescript]() | [Go]() | [Rust]()
* [Abstract factory](#abstract-factory) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Builder](#builder) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Prototype](#prototype) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Singleton](#singleton) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()

### Structural patterns

* [Adapter](#adapter) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Bridge](#bridge) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Composite](#composite) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Decorator](#decorator) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Facade](#facade) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Flyweight](#flyweight) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Proxy](#proxy) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()

### Behavioral patterns

* [Chain of responsibility](#chain-of-responsibility) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Command](#command) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Iterator](#iterator) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Mediator](#mediator) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Memento](#memento) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Observer](#observer) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [State](#state) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Strategy](#strategy) --->  [Python](https://github.com/starseeker-code/patrones-diseno/blob/main/Python/strategy.py) | [Typescript]() | [Go]() | [Rust]()
* [Template](#template) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
* [Visitor](#visitor) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()

## Introduction

...

## How to run the code

<details>
<summary>Python</summary>

Python is an interpreted language (requires a Python 3.12+ interpreter) that [can be found here](https://www.python.org/downloads/).

An online Python interpreter [may be found here](https://www.programiz.com/python-programming/online-compiler/) for code inspection and run.

Each python script includes an entrypoint for module testing. The way of running a module is by calling it:

```bash
python <module_name>
```
</details>

<details>
<summary>Typescript</summary>
...
</details>

<details>
<summary>Go</summary>
...
</details>

<details>
<summary>Rust</summary>
...
</details>

## SOLID principles
[Python](https://github.com/starseeker-code/patrones-diseno/blob/main/Python/SOLID.py) | [Typescript]() | [Go]() | [Rust]()

...

<details>
<summary>Single responsibility</summary>

**Definition**
> A class should have one and only one reason to change, meaning that a class should have only one job

This principle aims to atomize the code into small, functional parts. Improves cohesion but usually introduces coupling by it's own.
The main objective with this first principle is to achieve a well organized code that is easier to change and maintain while guaranteeing that each component has max cohesion.
</details>

<details>
<summary>Open/Closed</summary>

**Definition**
> Objects or entities should be open for extension but closed for modification

This principle allows for code evolution without introducing breaking changes. While it introduces more coupling, it allows for nice tree-like structures of inheritance. Badly done, it'll form a spagghetti anti-pattern.

</details>

<details>
<summary>Liskov substitution</summary>

**Definition**
> Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T

Meaning that every child class should be blindly substitutable for their parent class. This culminates into duck typing, that Python already implements. Thus, the only care needed is to define correct interfaces.

</details>

<details>
<summary>Interface segregation</summary>

**Definition**
> A class should never be forced to implement an interface that it doesn’t use, or classes shouldn’t be forced to depend on methods they do not use

Basic principle of abstraction and decoupling. Avoids inheritance or mappings to unnecesary interfaces, segregating them according to functional dependencies of child classes.

</details>

<details>
<summary>Dependency inversion</summary>

**Definition**
> Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions

Very useful technique (dependency injection) that allows for complete decoupling between behaviour and implementation. Done right, it could provide strongly abstracted code while maintaining high cohesion (and low coupling).

</details>

## Factory
[Python](https://github.com/starseeker-code/patrones-diseno/blob/main/Python/factory.py) | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Abstract factory
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Builder
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Prototype
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Singleton
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Adapter
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Bridge
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Composite
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Decorator
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Facade
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Flyweight
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Proxy
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Chain of responsibility
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Command
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Iterator
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Mediator
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Memento
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Observer
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## State
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Strategy
[Python](https://github.com/starseeker-code/patrones-diseno/blob/main/Python/strategy.py) | [Typescript]() | [Go]() | [Rust]()

The strategy pattern separates the different behaviour algorithms (strategies) for a concrete class (context).
The *context* must store the reference for one of the *strategies*, delegating the behaviour to a linked *strategy object*, decoupling it.
The *context* isn't responsible for selecting the *strategy*, instead, it's injected as a dependency (or it could be automated somewhat in the interface). All *strategies* share the same interface, that exposes a single method for triggering the *strategy* for the *context*.
This allows for an independent *context* and easy creation or modification of new *strategies*.

![strategy diagram](https://refactoring.guru/images/patterns/diagrams/strategy/structure-indexed-2x.png "Strategy pattern")

<details>
<summary>Diagram explanation</summary>

1. The Context maintains a reference to one of the concrete strategies and communicates with this object only via the strategy interface.

2. The Strategy interface is common to all concrete strategies. It declares a method the context uses to execute a strategy.

3. Concrete Strategies implement different variations of an algorithm the context uses.

4. The context calls the execution method on the linked strategy object each time it needs to run the algorithm. The context doesn’t know what type of strategy it works with or how the algorithm is executed.

5. The Client creates a specific strategy object and passes it to the context. The context exposes a setter which lets clients replace the strategy associated with the context at runtime.
</details>

**How to implement the pattern**

1. In the context class, identify an algorithm that’s prone to frequent changes. It may also be a massive conditional that selects and executes a variant of the same algorithm at runtime.

2. Declare the strategy interface common to all variants of the algorithm.

3. One by one, extract all algorithms into their own classes. They should all implement the strategy interface.

4. In the context class, add a field for storing a reference to a strategy object. Provide a setter for replacing values of that field. The context should work with the strategy object only via the strategy interface. The context may define an interface which lets the strategy access its data.

5. Clients of the context must associate it with a suitable strategy that matches the way they expect the context to perform its primary job.

**When to use it and gotchas**

* It lets you indirectly alter the object’s behavior at runtime by associating it with different sub-objects which can perform specific sub-tasks in different ways

* It's perfect for extracting the varying behavior into a separate class hierarchy and combine the original classes into one, thereby reducing duplicate code

* Allows for code isolation, internal data, and dependencies of various algorithms from the rest of the code. Various clients get a simple interface to execute the algorithms and switch them at runtime

* It's perfect for long if-else statements, because it extracts all algorithms into separate classes, all of which implement the same interface. The original object delegates execution to one of these objects, instead of implementing all variants of the algorithm

---  

* If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern

* Clients must be aware of the differences between strategies to be able to select a proper one

* There's usually code patterns (pattern matching, functional programming, lambdas and arrow functions, ...) that don't involve extra classes and inheritance, providing a good mid-ground solution


<a href="#index"><sub>⬆ Return to Index</sub></a>

## Template
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Visitor
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>


