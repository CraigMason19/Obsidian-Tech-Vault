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
### JavaScript Example (JEST)

[JEST](https://www.npmjs.com/package/jest)

```JS
// Save as a dev dependancy, don't commit to git 
npm install jest --save-dev

// In package.json add this
"scripts": {
	"test": "jest"
	// OR add extra flags
	"test": "jest --watchAll --coverage --verbose"
},

// Then create a folder called tests anf add tests that end in .test.js
lib.test.js

// Add tests here. Use describe to group related tests!
describe("absolute", () => {
    test("should return a positive number if input is positive", () => {
        const result = lib.absolute(1);
        expect(result).toBe(1); 
    });

    test("should return a positive number if input is negative", () => {
        const result = lib.absolute(-1);
        expect(result).toBe(1);
    });

    test("should return 0 if input is 0", () => {
        const result = lib.absolute(0);
        expect(result).toBe(0);
    });
});

// Then run
npm test
```

---
