A Regular Expression is a sequence of characters that specifies a match pattern in text.

A very good use case for AI

[Online RegEx](https://regexr.com)
[Python Regex](https://www.w3schools.com/python/python_regex.asp)
[JavaScript RegEx](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)

---

Language Examples
- [[#Python]]
- [[#JavaScript]]
- [[#C Sharp]]

---

- **Escaping Backslashes**: Always escape `\` in string literals when defining a regex in TypeScript/JavaScript.
- **Global Flag (`g`)**: Use this flag to find all matches in a string instead of stopping at the first match.
- **Word Boundary (`\b`)**: Ensures you're matching full words, not parts of words.

---
## Python

To use [[RegEx]] in [[Python]] use the re module 

```python
import re
```

---
## JavaScript

```JS
const text = `apple xray apple outer easter`;

// Match words starting with a vowel
// const regexp = new RegExp('\\b([aeiou])\\w*');
const regexp = new RegExp('\\b([aeiou])\\w*', 'g'); // Global matching

// Group tests
const matches = text.match(regexp);
console.log(matches)

// Individual tests
for(let word of text.split(" ")) {
    console.log(`${word} -> ${regexp.test(word)} `)
}
```

---
## C Sharp

```C#
if(Regex.IsMatch(phoneNumber, "[a-zA-Z]"))
{
	throw new ArgumentException("Letters are not permitted");
}

string pattern = @"[+]?\d{3,}";
string result = string.Concat(Regex.Matches(phoneNumber, pattern));

```

---
