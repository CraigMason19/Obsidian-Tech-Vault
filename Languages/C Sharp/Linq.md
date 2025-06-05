**Language Integrated Query**

Adds query capabilities into [[C Sharp]]. Originally released as part of  [[(dot)NET]] Framework 3.5


[Microsoft - Linq](https://learn.microsoft.com/en-us/dotnet/csharp/linq/)

[[#IEnumerable & IEnumerator]]

LINQ provides a set of operators that enable developers to query, project, and filter data in arrays, collections, and other data sources.


``` using System.Linq ```


```
can call linq on any object that supports IEnumerable or generic IEnumerable<T> interface. e.g. List, Stack, Dictionary etc...
```


Array implements IEnumerable

IEnumerable allows us to use a foreach loop,

A C# enumerable behaves like a python Generator

## IEnumerable & IEnumerator

```C#
using System;
using System.Collections;

public class Repeater : IEnumerable<int>
{
    public int Max { get; }
    
    
    public Repeater(int max)
    {
        Max = max;
    }
    
    public IEnumerator GetEnumerator()
    {
        return new RepeaterEnumerator(Max);
    }
    
    IEnumerator<int> IEnumerable<int>.GetEnumerator()
    {
        return new RepeaterEnumerator(Max);
    }
}

public class RepeaterEnumerator : IEnumerator<int>
{
    public int Max { get; private set; } = 10;
    
    public int Current { get; private set; } = 0;
    
    object IEnumerator.Current => Current;
    
    
    
    public RepeaterEnumerator(int max)
    {
        Max = max;
    }
    
    public void Dispose()
    {
        // ...
    }
    
    public bool MoveNext()
    {
        Current = (Current < Max) ? Current+1 : 0;
        
        return true;
    }
    
    public void Reset()
    {
        Current = 0;
    }
}

namespace Application
{
    class Program
    {
        static void Main(string[] args)
        {
            //// Infinite
            //foreach (var value in new Repeater(20))
            //{
            //    Console.WriteLine($"{value}");
            //}
            
            // Limited - Like a generator
            var rEnumerator = new Repeater(20).GetEnumerator();
            for(int i = 0; i < 30; i++)
            {
                Console.WriteLine($"{rEnumerator.Current}");
                rEnumerator.MoveNext();
            }
            
            // Noe we can use LINQ!
            var l = new Repeater(10).Take(5).ToList();
            Console.WriteLine(string.Join(", ", l)); // 1, 2, 3, 4, 5
        }
    }
}
```