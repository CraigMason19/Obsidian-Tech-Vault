#data-structures 

- singular Linked list
- doubly linked list
- circular linked list

[C# Corner](https://www.c-sharpcorner.com/article/linked-list-implementation-in-c-sharp/)

A [[Data Structure]] that represents a non linear list in memory. Push & Pop from the front. LIFO

```
Initial state: (empty list)
    head: null
Push 1:
    head: 1-> null
Push 2:
    head: 2-> 1-> null
Push 3:
    head: 3-> 2-> 1-> null
Pop:
	head: 2-> 1-> null
Pop:
	head: 1-> null
Pop:
	head: null
```