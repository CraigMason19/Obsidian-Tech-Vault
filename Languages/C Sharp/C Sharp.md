#language 

A programming language developed by Microsoft but is now fully open source & cross platform

---

[Microsoft - Naming Conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names)

[[#Useful Snippets]]
- [[#Ternary Operator]]
- [[#Is Letter & Change Each Character In String]]
- [[#Extension Methods]]
- [[#Decimal Places]]
- [[#Anonymous Classes]]




[[#Fields]]
[[#Nullable Reference Types]]
[[#Equality & GetHashCode]]
[[#Switch]]
[[#Generator]]
[[#Namespaces]]

[[#Keywords]]
- [[#Required]]
- [[#Implicit / Explicit]]

---
## Useful Snippets

### Ternary Operator

Takes the form of  ```condition ? trueExpression : falseExpression```. Exactly the same as in JavaScript

```c#
const score = 80;
const scoreRating = score > 70 ? "Excellent" : "Do better"; // Excellent
```

### Is Letter & Change Each Character In String

```C#
using System.Linq;

static bool IsLetter(char c) => char.IsLetter(c);

static char SwitchCase(char c)
{
    if(!IsLetter(c))
    {
        return c;
    }

    return char.IsUpper(c) ? char.ToLower(c) : char.ToUpper(c);
}

string example = "This Is A_example.";

var x = String.Join("", example.Select(c => SwitchCase(c)).ToArray());
Console.WriteLine(x);
```

### Extension Methods

Allow adding methods to existing types without creating a new derived type, recompiling, or otherwise modifying the original type
```C#
public static int WordCount(this string str) => return str.Split().Length;
```
## Decimal Places

```C# 
x.ToString($F{3});
```

---
### Anonymous Classes

Can be used to create a class in place without defining it. One time use classes

```c#
var data = new { a = 5, b = 10 };
Console.WriteLine(data.a * data.b); // 50
```

---
## Fields

```C#
_itemCost = 10;

public string GetItemCost() => _itemCost; // expression-bodied member 

// Property. When accessed it uses the underlying field,
public string MyProperty
{
	get
	{
		return _myField;
	}
	set
	{
		_myField = value;
	}
}

    // AutoProperty (C# 3.0 and higher) - which is a shorthand syntax
    // used to generate a private field for you
    public int AnotherProperty { get; set; } 

```

---
## Nullable Reference Types
[here](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references)

```c#
public class PersonModel
{
    public required string FirstName { get; set; }  
    public string? MiddleName { get; set; } // nullable string
    public required string LastName { get; set; }
    public override string ToString() => $"{FirstName} {MiddleName} {LastName}";
}

PersonModel p = new()
{
    FirstName = "Craig",
    //MiddleName = "Redacted", // This can be optional and will be null if not specified
    LastName = "Mason",
};

```

```c#
int a = 15;
//int b = null; // Cannot convert null to 'int' because it is a non-nullable value type
int? c = null; // Can be an int or null
Nullable<int> d = 5; // Essentially the same as the syntax above

Console.WriteLine(c is null ? "c is null" : "c is not null"); // c is null
Console.WriteLine(d is null ? "d is null" : "d is not null"); // d is not null


string? n = "craig";
string? n2 = null;

Console.WriteLine($"{n}: {n.Length}"); // craig: 5

//Console.WriteLine($"{n2}: {n2.Length}"); // NullReferenceException
Console.WriteLine($"{n2}: {n2?.Length}"); // If it is null then the rest won't be executed, nicer syntax than:
Console.WriteLine(n2 is null ? "null" : n2.Length);
```

---
## Equality & GetHashCode

```GetHashCode``` is needed so that an object can be inserted into a Set / HashSet & Dictionary etc...

```C#
public class Person
{
    public string Name { get; }
    public int ID { get; }
    
    public Person(string name, int id)
    {
        this.Name = name;
        this.ID = id;
    }
    
	public static bool operator ==(Person a, Person b)
    {
        return a.Name == b.Name && a.ID == b.ID;
    }
    
    public static bool operator !=(Person a, Person b)
    {
        return !(a == b);
    }
    
    public override bool Equals(object obj)
    {
        if (obj is Person other)
        {
            return this == other;
        }
        
        return false;
    }
    
    public override int GetHashCode()
    {
        return HashCode.Combine(Name, ID);
    }
}

namespace Application
{
    class Program
    {
        static void Main(string[] args)
        {
            var personA = new Person("Craig", 19);
            var personB = new Person("Craig", 19);
            
            Console.WriteLine(personA.Equals(personB)); // True
            Console.WriteLine(personA.Equals(new Person("Craig", 19))); // True
            
            Console.WriteLine(ReferenceEquals(personA, personA)); // True
            Console.WriteLine(ReferenceEquals(personA, personB)); // False
            Console.WriteLine(ReferenceEquals(personA, new Person("Craig", 19))); /// False
        }
    }
}
```



```C#
public struct Coord
{
    public Coord(ushort x, ushort y)
    {
        X = x;
        Y = y;
    }

    public ushort X { get; }

    public ushort Y { get; }

    public static bool operator ==(Coord a, Coord b)
    {
        return a.X == b.X && a.Y == b.Y;
    }

    public static bool operator !=(Coord a, Coord b)
    {
        return !(a == b);
    }

    public override bool Equals(object obj)
    {
        if (obj is Coord other)
        {
            return this == other;
        }

        return false;
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(X, Y);
    }
}

public struct Plot
{
    private Coord a; 
    private Coord b; 
    private Coord c;
    private Coord d;

    public Plot(Coord a, Coord b, Coord c, Coord d)
    {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }

    public override bool Equals(object obj)
    {
        if (obj is Plot other)
        {
            return a == other.a && b == other.b && c == other.c && d == other.d;
        }

        return false;
    }

    public override int GetHashCode()
    {
        return HashCode.Combine(a, b, c, d);
    }
}

```
---
## Switch

```c#
var result = prefixByte switch
{
	248 => BitConverter.ToInt64(buffer, 1),
	4   => BitConverter.ToUInt32(buffer, 1),
	252 => BitConverter.ToInt32(buffer, 1),
	2   => BitConverter.ToUInt16(buffer, 1),
	254 => BitConverter.ToInt16(buffer, 1),
	_ => 0,
};  
```

---
## Generator

```C#
IEnumerable<char> LoopString(string str)
{
    int index = 0;
    
    while (true)
    {
        if (index == str.Length)
        {
            index = 0;
        }
        
        yield return str[index++];
    }
}

var gen = LoopString("abc");
var enumerator = gen.GetEnumerator();

for (int i = 0; i < 10; i++)
{
    enumerator.MoveNext();
    
    Console.WriteLine(i.ToString() + "->" + enumerator.Current);
}
```

---
## Keywords

[[#Required]]
[[#Implicit / Explicit]]
### Required

Means that a value must be be set in the object initializer or attribute constructor

```c#
public class PersonModel
{
    public required string FirstName { get; init; } // Can only set on first time
    public required string LastName { get; set; }
    public override string ToString () { return FirstName + "" + LastName; }
}

//Member initializers
PersonModel p = new()
{
    FirstName = "Craig",
    LastName = "Mason",
};

var p2 = new PersonModel()
{
    FirstName = "John",
    //LastName = "Smith", // Error
};

//p.FirstName = "Jemma"; // Can't set on initialization 
p.LastName = "woof";     // Can change because of public set
```

### Implicit / Explicit

**Implicit Conversion** 
- Allows automatic type conversion without requiring an explicit cast.
- Should be used when the conversion is always safe and does not result in data loss.

**Explicit Conversion** 
- Requires an explicit cast in the code, indicating that the conversion might not always be safe or could result in data loss.
- Use when there's a possibility of an error or data loss.

Both can help with operator overloading, by allowing seamless and intuitive type conversions within your custom types.
This can make your code more readable and easier to maintain, especially when dealing with complex mathematical or logical operations.

```C#
public class ComplexNumber
{
    public double Real { get; private set; } = 0;
    public double Imaginary { get; private set; } = 0;
    
    public ComplexNumber(double real, double imaginary)
    {
        this.Real = real;
        this.Imaginary = imaginary;
    }
    
    public ComplexNumber Add(ComplexNumber other) => new ComplexNumber(this.Real + other.Real, this.Imaginary + other.Imaginary);
        
    public static implicit operator ComplexNumber(int real) => new ComplexNumber(real, 0);
    public static explicit operator double[](ComplexNumber c) => new double[] { c.Real, c.Imaginary };
    
    public override string ToString() => $"ComplexNumber({this.Real}, {this.Imaginary})";
}

var a = new ComplexNumber(5, 10);
Console.WriteLine(a.ToString()); // ComplexNumber(5, 10)

// Implicit
ComplexNumber b = 37;  
Console.WriteLine(b.ToString()); // ComplexNumber(37, 0)

// Explicit
var c = (double[])new ComplexNumber(7, 7);  
Console.WriteLine(string.Join(", ", c)); // 7, 7

// Easy method overloading
Console.WriteLine(new ComplexNumber(5, 10).Add(new ComplexNumber(3, 4))); // ComplexNumber(8, 14)
Console.WriteLine(x.Add(5)); // ComplexNumber(10, 10)
```

---
## Abstract
only for inheriting

---
## Interface
can have many interfaces that the class must implement

---

## Namespaces

### Reduced Namespace Brackets

You can add a ; to the namespace you are in (usually only one namespace per file) to reduce the block level scope to make code easier to read.

```c#
namespace ConsoleApp;

internal class Program
{
    static void Main(string[] args)
    {
        // ...
    }
}
```
### Static Namespaces

You can add the static keyword to reduced namespace clutter

```c#
using static System.Console; 

Console.WriteLine("Hello, World!");
WriteLine("Hello, World!");
```