#language

A scripting language that allows you to implement complex features on web pages.

Can write JS code in the browser console.

JavaScript doesn't need the semi colon but it's good practice. Like a full stop on a sentence.

---

[Fireship YT](https://www.youtube.com/watch?v=lkIFF4maKMU&list=WL&index=30&t=54s)

[[#Useful Snippets]]
- [[#Ternary Operator]]
- [[#Loop through an Object]]
- [[#Is Prime]]
- [[#To Binary]]
- Strings
	- [[#String Literals]]
	- [[#String Replace At / Overwrite]]
	- [[#Reverse a String]]
	- [[#Is Letter & Change Each Character In String]]
- Array
	- [[#Sort Array]]
	- [[#Sum Array]]
- [[#Numbers]]
	- [[#BigInt]]

[[#== vs ===]]
[[#Optional chaining]]
[[#Nullish coalescing operator]]
[[#Decimal Places]]
[[#Exceptions]]
[[#const, let & var]]
[[#Generators]]
[[#Private Methods]]
[[#Imports / Exports]]
[[#Comments]]
[[#Dictionaries]]

---
## Useful Snippets
### Ternary Operator

Takes the form of  ```condition ? trueExpression : falseExpression

```javascript
const score = 80;
const scoreRating = score > 70 ? "Excellent" : "Do better"; // Excellent
```

### Reverse a String

```javascript
const reverseString = (str) => {
    return str.split("").reverse().join("");
};
```
### Is Letter & Change Each Character In String
  
```javascript
const isLetter = (c) => {
    return c.toLowerCase() != c.toUpperCase();
}

const switchCase = (c) => {
    if (!isLetter(c)) {
        return c;
    }

    return (c.toLowerCase() === c) ? c.toUpperCase() : c.toLowerCase();
}

let newStr = "This is a_EXAMPLE.".split("").map(c => switchCase(c)).join("");
console.log(newStr); // tHIS IS A_example.
```
### Loop through an Object

```javascript
const dict = { firstname: 'John', lastname: 'Smith' }

for (const [key, value] of Object.entries(dict)) {
    console.log(`${key}: ${value}`);
}
```

### String Literals
```javascript
const text = `count is now ${count}`
```
### Is Prime
```javascript
const isPrime = num => {
  for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
      if(num % i === 0) return false;
  }
  return num > 1;
}
```
### In Range

``` Javascript
// Both ranges are inclussive
function inRange(value, min, max) {
    return value >= min && value <= max;
}
```
## Sort Array
        
```JS
myArray.sort((a, b) => a + b) // Ascending
myArray.sort((a, b) => b - a) // Descending
```
## To Binary

```JS 
const toBinary = (number) => (number >>> 0).toString(2);
const toBinary = (number) => (number >>> 0).toString(2).padStart(5, '0');
```

## String Replace At / Overwrite

```JS
String.prototype.replaceAt = function(index, replacement) {
    return this.substring(0, index) + replacement + this.substring(index + replacement.length);
}

let s = "_________";

console.log(s);                       //_________
console.log(s.replaceAt(2, "CRAIG")); // __CRAIG__
```


## Sum Array

```JS
const sum = (array) => {
    return array.reduce((accumulator, currentValue) => {
        return accumulator + currentValue
    }, 0);
}
```

## Numbers

### BigInt

```JavaScript
let a = BigInt(5)
let b = BigInt('5')
let c = 5n * 10n

```

## == vs ===

Double equals will compare the value whereas triple equals will compare the value and type.
```Javascript
'1234' == 1234 // True
'1234' === 1234 // False
```

## Optional chaining

[here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining)
## Nullish coalescing operator

[here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing)
```javascript
// if variable is defined, then variable.
// if variable isn’t defined, then value.

a = null;
a = a ?? 100;

b = undefined;
b ??= 50;
```
## Decimal places
 
NOTE:  ```toFixed()``` returns a string. Need to convert it to a number afterwards

```JavaScript
const num = 123.46789;
const numFixed1 = Number(num.toFixed(2));
const numFixed2 = num.toFixed(2);

console.log(num, typeof num);                // 123.46789, number
console.log(numFixed1, typeof numFixed1);    // 123.47, number
console.log(numFixed2, typeof numFixed2);    // "123.47", string

// Method 1 - convert to a number explicitly
console.log(numFixed1, typeof numFixed1);    // 123.47, number

// Method 2 - The unary plus (+) operator. Attempts to convert it into a number, if it isn't already.
console.log(+numFixed2, typeof +numFixed2);  // 123.47, number

// This matters because of strict equality
console.log(123.47 == num.toFixed(2))        // true
console.log(123.47 === num.toFixed(2))       // false
```

## Exceptions

```javascript
class ArgumentError extends Error {}

class OverheatingError extends Error {
  constructor(temperature) {
    super(`The temperature is ${temperature} ! Overheating !`);
    this.temperature = temperature;
  }
}

try {
    throw new OverheatingError(651);
}

catch (error) {
    if(error instanceof Error) {
        console.error(error.message);
    }
    else(error instanceof ArgumentError) {
	    ...
    }
    else {
	    ...
    }
}
```
## const, let & var

There are 3 ways to declare a variable. var, let and const. 

let and const are block scoped, var is function scoped. This means var is scoped wider. var can also be reassigned multiple times. This can make it easy to be overwritten by accident.
For this reason const and let are preferred. const will protect against assignment but you can change the properties if it is an object.

```JavaScript
if(true) {
  var varVariable = 'var is valid';
  let letVariable = 'let is true';
  const constVariable = 'const is true';
}

console.log(varVariable);   // fine. global
// console.log(letVariable);   // error. outside of block defnied it in
// console.log(constVariable); // error. outside of block defnied it in
```

```JavaScript
// var variables can be overwritten
var a = 10;
var a = 20;
console.log(a) // 20

// var variables can be used before they are defined.
console.log(varVariable); // undefined
var varVariable = 'true';
console.log(varVariable); // true

// const protects against assigning a different value. But still lets you change the properties in that value. Which is a bit unintuitive?? 
const b = 10;
// b = 20; // SyntaxError
console.log(b); // 10  

const c = { name: 'Craig' }
console.log(c); // 'Craig'
c.name = 'Bob';
console.log(c); // 'Bob'
```

## Private Methods

You can use # to define private methods in JavaScript, like the _ in Python methods

```javascript
class Foo {
    constructor(x) {
        this.x = x;    
        // this.#privateFunc();
    }

    publicFunc() { console.log(this.x + ' printing from publicFunc'); }

    #privateFunc() { console.log(this.x + ' printing from privateFunc'); }
}

const f = new Foo(10);
f.publicFunc();
f.#privateFunc(); // SyntaxError: Private field '#privateFunc' must be declared in an enclosing class
```

## Generators

[here](https://javascript.info/generators)

JavaScript has generators just like Python. Yay!

```JavaScript
function* oneToN(n) {
    let index = 0;
    while (index < n) {
      yield index++;
    }
}

const generator = oneToN(5);  

console.log(generator.next());        // { value: 0, done: false }
console.log(generator.next().value);  // 1

for(let value of oneToN(5)) {
    console.log(value);
}
```

---
## Imports / Exports

### Common JS Modules
To import functionality from script a into script b

**a.js**
```JS
const CONST_EXAMPLE = 5;

const functionExample = () => {
  return "function example";
};

class ClassExample { 
  constructor(value) { 
      this.data = value; 
  }
}

module.exports = { CONST_EXAMPLE, functionExample, ClassExample };
```

**b.js**
```js
const myImports = require('./a');
  
console.log(myImports.CONST_EXAMPLE);
console.log(myImports.functionExample()); 

let ex = new myImports.ClassExample("Class Example");
console.log(ex.data); // Class Example
```

---

## Comments

Use the JSDoc standard

```    
/**
 * Sets the value at the specified cell.
 * @param {number} x - The row index of the cell.
 * @param {number} y - The column index of the cell.
 * @param {any} [fillValue=0] - The value to set at the specified cell.
 * @throws {Error} If the coordinates are out of bounds.
 */
```




---
## Dictionaries

### Method 1 - Objects

```JS
let teams = {
    "TeamA" : { matchesPlayed:2, wins:2, draws:0, losses:0,points:6 },            
    "TeamB" : { matchesPlayed:2, wins:0, draws:0, losses:2,points:0 },    
};

console.log(teams["TeamA"]);
console.log(teams["TeamA"].matchesPlayed);

console.log(teams["TeamC"]); // undefined
teams["TeamC"] = 5; // Will add to the dict

// Loop over
for (let [key, value] of Object.entries(teams)) 
{
    console.log(key, value);
};
```
### Method 2 - Map Object

Very similar but has features like .keys, .values & .has

```JS
let teams = new Map([
    ["TeamA", { matchesPlayed:2, wins:2, draws:0, losses:0,points:6 }],            
    ["TeamB", { matchesPlayed:2, wins:0, draws:0, losses:2,points:0 }],    
]);

console.log(teams.get("TeamA"));
console.log(teams.get("TeamA").matchesPlayed);

console.log(teams.set("TeamA"));
console.log(teams.set("TeamA").matchesPlayed = 100);

console.log(teams.get("TeamC"));  // undefined
teams.set("TeamC", { wins:100 }); // Will add to the dict
console.log(teams.get("TeamC")); 

// Loop over
for (let [key, value] of Object.entries(teams)) 
{
    console.log(key, value);
};
```




---
## DOMContentLoaded

---
# JSDoc

In visual studio you can add `/**` and then auto complete to add a JSDoc template

```js
/**
 * Checks if a given value is within a specified range, inclusive of the minimum and maximum.
 *
 * @param {number} value - The value to check.
 * @param {number} inclusiveMin - The minimum value of the range (inclusive).
 * @param {number} inclusiveMax - The maximum value of the range (inclusive).
 * @returns {boolean} - Returns `true` if the value is within the range, otherwise `false`.
 */
export function isInRange(value, inclusiveMin, inclusiveMax) {
    return value >= inclusiveMin && value <= inclusiveMax;
}
```