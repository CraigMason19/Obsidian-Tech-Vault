[YT - Fireship](https://www.youtube.com/watch?v=ENrzD9HAZK4&list=WL&index=44)
[Net Ninja - Node.js Crash Course](https://www.youtube.com/watch?v=zb3Qk8SG5Ms&list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU)

---

An open-source, cross-platform [[JavaScript]] runtime environment and library for running web 
applications / JavaScript outside the browser, or on a server.

JavaScript is compiled in the browser using V8 (google wrote in C++). Node.js written in C++ allows us to compile outside of the browser 

Used so I can just write a script and run in **VSCode**

Originally it could only be used on a web browser

Not just a V8 wrapper but allows extra functionallity such as reading / writting to files, server connections etc...


Pros
- Can use the same language on front / back end (JavaScript)
- Large community & 3rd party packages




[[#Core Modules]]
	- [[#OS]]
	- [[#File System]]




## Installation

Installed by downloading the exe from [node.js](https://nodejs.org/en)
## Commands


| node -v | Check if it is installed and version |
| ------- | ------------------------------------ |
|         |                                      |

nmv - node version manager

index.js - initial start by default

in browser window is the global object in node.js there is a global which is assumed but can't interact with html or dom elements

e.g. ```document.querySelector()``` 
-> not in the global object it is in window

## Imports

**Node.js-specific** due to the usage of the `module.exports` and `require` syntax, which are part of Node.js's **CommonJS** module system

people.js
```js
const NAMES = ["Craig", "John", "Jane"];

module.exports = {
    names: NAMES,
}
```

main.js
```js
const p = require("./people")

console.log(p) // { names: [ 'Craig', 'John', 'Jane' ] }
console.log(p.names) // [ 'Craig', 'John', 'Jane' ]
```

## Core Modules

## OS
### File System