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

Look at `music_theory` for a real example. Large classes are split up by methods which become there own test classes  
#### Console commands

```python
python -m coverage run -m unittest discover music_theory_tests
python -m coverage html
```

```python
class TestExample(unittest.TestCase):
	# NOTE - the camelCase syntax. Important that they are named this way.
	
	#---------------------------------------------------------------------------
    # setUpClass and tearDownClass run before and after all tests, called once
    #---------------------------------------------------------------------------
    
    @classmethod
    def setUpClass(cls):
	    cls.x = x
	    pass
	        
    @classmethod
    def tearDownClass(cls):
        # Use for cleanup
        pass
        
    #---------------------------------------------------------------------------
    # setUp and tearDown run before every single test.
    #---------------------------------------------------------------------------
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
```

```Python
class TestBase(unittest.TestCase):
    def setUp(self):
        self.first_name = "Craig"
        
    def test_first_name(self):
        first_name = f"{self.first_name}"
        self.assertEqual(first_name, "Craig")

class TestExtra(TestBase):
    def setUp(self):
        super().setUp()  # important to inherit setup from TestBase
        self.last_name = "Mason"
        
    def test_full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        self.assertEqual(full_name, "Craig Mason")
```

---
