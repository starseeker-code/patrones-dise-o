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
* [Strategy](#strategy) --->  [Python]() | [Typescript]() | [Go]() | [Rust]()
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
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Template
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>

## Visitor
[Python]() | [Typescript]() | [Go]() | [Rust]()

...

<a href="#index"><sub>⬆ Return to Index</sub></a>


