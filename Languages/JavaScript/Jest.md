A [[Testing]] framework for [[JavaScript]] & [[TypeScript]]

Docs
- https://jestjs.io
- https://jestjs.io/docs/getting-started#using-typescript

Links
 - [Introduction To Testing In JavaScript With Jest](https://www.youtube.com/watch?v=FgnxcUQ5vho&list=WL&index=44)

[[#Usage]]
- [[#JavaScript]]

## Usage

### JavaScript 

```
1. npm init -y
2. npm install --save-dev jest // save dev because we only want to use this in development
3. Make this change to package.json. Add the coverage flag to show what has been tested, can open index.html in the covergae folder to show a detailed view.

	"scripts": {
	    "test": "jest --coverage"
	},
  
4. npm test
```

### TypeScript

```
tsc -init
npm install --save-dev jest ts-jest @types/jest


```

---
