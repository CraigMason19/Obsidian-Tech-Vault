#concept 

[[#Static Typing]]
[[#Dynamic Typing]]
[[#Duck Typing]]
## Static Typing

Also known as Strict Typing, cannot change a variable type after it has been created.

Certain languages like TypeScript have typing inference, meaning the type will be inferred and can declared much more simply. e.g.

```TypeScript 
const x: number = 5;
const y = 10; // Will be inferred as a number
```

- C#, C++, TypeScript
- Compile-time type checking rather than run-time. Resulting in fewer errors.
- Better tooling / error / intellisense support
- Type annotation serve as documentation for large projects and working with others.
## Dynamic Typing

Also known as Loose Typing, can change a variables type at any point.

- JavaScript, Python
- Flexible
- Ease of use, particularly for rapid prototyping and scripting tasks
- Difficult for large scale projects.

## Duck Typing

[The Duck Test](https://en.wikipedia.org/wiki/Duck_test)
_If it looks like a duck_, swims like a duck, and quacks like a duck, then it probably is a duck.

[Corey Schafer YT](https://www.youtube.com/watch?v=x3v9zMX1s4s&list=WL&index=38)

This means that we dont care what an object is, we just care about what it can do. Only care that it behaves like a duck when asked to do so.
### Easier to ask forgiveness than permission

This means that it is easier to try and do something and handle a error if it occurs rather than asking if it can be called. 
- The 'Pythonic' way of doing things.
- Often faster as we make one call rather than multiple calls to the object to determine if it is possible to call it.
- Often easier to read.

```Python
class Duck:
    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")

def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')


    # LBYL - Look Before You Leap (Non-Pythonic)
    # if hasattr(thing, 'quack'):    <- Asking for permission
    #     if callable(thing.quack):  <- Asking for permission
    #         thing.quack()
    #
    # if hasattr(thing, 'fly'):      <- Asking for permission
    #     if callable(thing.fly):    <- Asking for permission
    #         thing.fly()


    # EAFP - Easier to ask forgiveness than permission (Pythonic)
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e: #     <- Asking for forgiveness
        print(e)

thing = Duck()
quack_and_fly(thing)
```

``` Output
Quack, quack
Flap, Flap!
'Duck' object has no attribute 'bark'
```