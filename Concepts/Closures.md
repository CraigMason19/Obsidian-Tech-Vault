#concept 

Examples
	[[#JavaScript]]
	[[#Python]]
	
Links
	Corey Schafer
	https://www.youtube.com/watch?v=swU3c34d2NQ&list=WL&index=21

A closure is a concept supported in multiple languages ([[Python]], [[JavaScript]])

Therefore, in simple terms: A closure is an inner function that remembers and has access to variables in the local scope in which it was created even after the outer function has finished executing

 functions that can acces values outside of their scope

 allows variablees from an outer lexical scope to be used inside a nested block of code.

 var in a for loop gets hoisted up into the global scope

function defined in  af unction has acces to the parents scope (the outer function) even if the outer finishes executing and those variables are no longer accessable

outside that function

has access to a variable outside of the function



  

// A closure is an inner function that remembers and has access to variables in the local scope in which it was created. Even after the outer function has finished executing.



## JavaScript

```JavaScript
function html_tag(tag) {
    function wrap_text(msg) {
        console.log('<' + tag + '>' + msg + '</' + tag + '>')
    }

    return wrap_text
}

print_h1 = html_tag('h1')
print_h1("Test Headline!") // <h1>Test Headline!</h1>
print_h1("Another Headline!") // <h1>Another Headline!</h1>

print_img = html_tag('img')
print_img("glass.png") // <img>glass.png</img>
```

## Python

```python
# example 1
def enter_number_outer():
    numbers = []

    def enter_number_inner(x):
        numbers.append(x)
        print(numbers)

	return enter_number_inner 

enter_num = enter_number_outer()
enter_num(3) # [3]
enter_num(7) # [3, 4]
enter_num(4) # [3, 4, 7]


# example 2
def greeting(msg):
    def person(name):
        print(f"{msg} {name}!")

    return person

birthday, new_year = greeting("Happy Birthday"), greeting("Happy New Year")
birthday("Craig") # Happy Birthday Craig!
new_year("Alexi") # Happy New Year Alexi!
```