#language 

A superset of [[JavaScript]], meaning that any valid JS code is also valid TypeScript code. 
- Developed at Microsoft to combat frustration when working on large JavaScript Projects.
- Introduces [[Typing#Static Typing]]
- Will need to be converted to regular [[JavaScript]] first. (Like SASS & CSS).

Try to **NEVER** use the any keyword.

## Links
[Docs](https://www.typescriptlang.org)
[Fireship YT - 100 Seconds](https://www.youtube.com/watch?v=zQnBQ4tB3ZA&list=WL&index=35&t=4s)
[Fireship YT - The Basics](https://www.youtube.com/watch?v=ahCwqrYpIuM&list=WL&index=31)
[Net Ninja YT - Crash Course](https://www.youtube.com/watch?v=VGu1vDAWNTg&list=PL4cUxeGkcC9gNhFQgS4edYLqP7LkZcFMN)

[[#Install using Node Package Manager ( NPM )]]
[[#Configuration]]
[[#Convert to JavaScript]]

[[#Usage]]
- [[#Variables]]
- [[#Functions]]
- [[#Enum]]
- [[#Dictionaries]]
- [[#Classes]]
- [[#Interfaces]]
- [[#Generics]]
- [[#DOM]]
- [[#Type Casting]]

[[#Imports]] 
[[#Non-null assertion operator]]

## Install using Node Package Manager ([[NPM]])

```console
npm install typescript // local install
npm install -g typescript // Global install
npm install -g ts-node // ???

# Check installation 
```
## Configuration

next to the typescript files call ``tsc --init`` to create a tsconfig.json

tsconfig.json
```json
{
    "compilerOptions": {
        "target":"ES6",
        "module":"CommonJS",
        "outDir":"out",  // Define a output directory
        "sourceMap":true // Allows for debugging TS
    }
}
```
## Convert to JavaScript

Make sure the terminal location is where the TS file is.

```console
tsc hello-world.ts

tsc hello-world.ts -w // Watch. automatically recompiles when changes are made and there are no errors.

tsc -w // Watch all
```



## Usage

### Variables

```TypeScript
// Variables. Don't need to add the type as it will be inferred from it's inital value
let n : number = 0;
let b : boolean = false;
let s : string = "empty";
let o : object = { name: "Craig" };
let a : any = 25; // Behaves like regular JS

// Union types
let u : string|number = "Craig"; // OR 19

// Tuples
let t: [string, number] = ["Telecaster", 200];

//Arays
let arr : number[] = [];
let mixed: (string|number)[] = []; // Parenthesis needed

// Objects
let menuItem: {
    title: string;
    cost: number;
}

menuItem = {title:"Pizza", cost:8};

// Aliases
type stringOrNum = string|number;
type objectWithID = { id: stringOrNum };

const greet = (user: objectWithID) : void => {
    //
};
```
### Functions

```TypeScript
const square = (n: number) : number => {
    return n*n;
};

const nothing = () : void => {
    // void shows a complete lack of a return value, when compiled to JS returns undefined.
};
```
### Enum

```TypeScript
enum ResourceType { Texture, Shader, Model }

const foo = (r: ResourceType): void => {
    console.log(r)
};

foo(ResourceType.Shader); // 1
```

### Dictionaries

```TypeScript
const colorValueDict: {
  [id: string] : number;
} = {};

colorValueDict["black"] = 0;
colorValueDict["brown"] = 1;

// Or define a interface

interface OrbitalPeriod {
    [key: string]: number;
}

const orbitalPeriod: OrbitalPeriod = {
    mercury: 0.2408467,
    venus: 0.61519726,
    earth: 1.0,
    mars: 1.8808158,
    jupiter: 11.862615,
    saturn: 29.447498,
    uranus: 84.016846,
    neptune: 164.79132,
}
```

### Classes

```TypeScript
class Example {
    a: number; // public by default (unlike C#)
    public b: number;
    private c: number;
    readonly id: string;

    constructor(a: number, b: number, c: number) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.id = "ID_" + a.toString() + b.toString() + c.toString();
    }

    // Alternative constructor to defone and assign the class properties directly
    // constructor(
    //     public a: number,
    //     public b: number,
    //     private c: number,
    //     readonly id: string,
    // ){}

    format() : string {
        return `${this.a}-${this.b}-${this.c}`;
    }
}

console.log(new Example(3,4,5).format()); // 3-4-5
console.log(new Example(3,4,5).id);       // ID_345
```
### Interfaces

```TypeScript
interface Person {
    name: string;
    id: number;
}

interface Formattable {
    format(): string;
}

class Employee implements Person, Formattable {
    constructor(
        readonly name: string,
        readonly id: number,
    ){}

    format() {
        return `${this.name} has Employee ID of ${this.id}`;
    }
}

const e1 = new Employee("Craig", 5001);
const e2 = new Employee("Alexi", 5070);

let arr: Formattable[] = [e1, e2];
arr.forEach(x => console.log(x.format()));
```
### Generics

```TypeScript
interface Resource<T> {
    data: T;
}

let arr: Resource<string|number>[] = [];
arr.push({data: "hello world!"});
arr.push({data: "19"});
console.log(arr); // [ { data: 'hello world!' }, { data: '19' } ]

class Foo<T> {
    constructor(public data: T) {}
}

let f = new Foo(5);
console.log(f.data); // 5
```
### DOM

Mostly the same as in JS. TS will infer the type and will show relevant intellisense.

```TypeScript
// Check for not null
let anchor = document.querySelector('a');

if(anchor) {
    console.log(anchor);
}

// OR
anchor = document.querySelector('a')!; // <- avoid possibly null error as we are sure this will return something
console.log(anchor.href);
```
### Type Casting

We can tell the compiler what we expect a class to to be, which then will show relevant information

```TypeScript
const form = document.querySelector('.new-item-form') as HTMLFormElement;
```
## Imports

<script type="module" src="app.js"></script>

ts vs js non module imports????

Using module imports. Very similar to [[JavaScript#Imports / Exports]]

NOTE: Will need to change the module option in tsconfig to 'es2015'
NOTe comment out "module": "commonjs"

```TypeScript
import { Example } from './class.js'; // Browser will import a JS file not a TS file
import { Example } from './helper/class.js';

import { PLACE_DATA } from "./time-zones.ts"; // Deno version
```
## Non-null assertion operator

The exclamation mark (!) at the end of popA tells the TypeScript compiler that we are asserting that the expression preceding the ! will NOT be null or undefined. Used when we are absolutely sure as other wise errors may be caused.  

In this example popB might be better as that is what the pop function returns in JS. And is therefore more readable

```TypeScript
export class Stack<T> { 
  private items: T[] = [];

  push(element: T): void { 
    this.items.push(element); 
  } 

  popA(): T { 
    if (this.items.length == 0) {
      throw new Error("Can't pop from an empty stack");
    }
    
    return this.items.pop()!; // Wont be null as that will caught by guard clause above
  } 

  popB(): T | undefined {  
    return this.items.pop(); // May return undefined
  } 
}
```