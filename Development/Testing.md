#Development 

Helps prevent bugs and makes refactoring much easier / safer.

[FireShip YT - Test-Driven Development // Fun TDD Introduction with JavaScript](https://www.youtube.com/watch?v=Jv2uxzhPFl4&list=WL&index=28&t=155s)

---

[[#Types]]
[[#Naming Conventions]]
[[#SetUp & TearDown]]

[[#Examples]]
- [[#C Sharp Example]]
- [[#Python Example]]
- [[#JavaScript Example (JEST)]]

---
## Types

There are 3 main types on testing

- **Unit Testing**
	- Test small sections of code / logic.
	- No external resources
	- Execute fast
	
- **Integration Testing**
	- Test with external resources (API's, Databases etc...) 
	- Take longer but give more confidence
	
- **End to end Testing**
	- Runs in a simulated environment
	- Mimics a real world user
	- Drives an application threw its UI
	- Very slow as it requires launching and using the application
	- Very brittle as any change to the UI may break a test

But there are others

- **Acceptance Testing**
	- Making sure we have met the clients requirements
	
- **System Testing**
	- Make sure the solution works on hardware or servers
	
- **Smoke Testing**
	- Run a few essential test first to make sure the project isn't 'on fire'. Smoke detects if something is wrong early

---
## Naming Conventions

Made up of 3 parts 
```name_scenario_expectation```
name = Function name
scenario = 

The method should then split int 3 


```
// Arrange 
var ball = new Ball { Number = 5, Color = ConsoleColor.Red }; 

// Act 
var result = ball.ToString(); 

// Assert 
Assert.AreEqual("05", result);
```

---
## SetUp & TearDown

Avoids code duplication inside a test suite.

Allows us to create a new object of the thing we are testing with a certain state or values in SetUp and can safely delete in TearDown (close connections for example)

---

## Examples

### C Sharp Example

**NOTE:** Community edition doesn't have code coverage so add coverlet through NuGet and then in the terminal run 

`dotnet test --collect:"XPlat Code Coverage"`

```C#
namespace LotteryApp.UnitTests
{
    [TestClass]
    public class BallTests
    {
        [TestMethod]
        public void ToString_Representation_Correct()
        {
			// Arrange 
			var ball = new Ball { Number = 5, Color = ConsoleColor.Red };
			
			// Act 
			var result = ball.ToString(); 
			
			// Assert 
			Assert.AreEqual("05", result);
        }
    }
}
```

---
### Python Example

```Python
python -m coverage run -m unittest discover




python -m coverage run -m unittest discover music_theory_tests



python -m coverage report
python -m coverage report -m

python -m coverage html
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
