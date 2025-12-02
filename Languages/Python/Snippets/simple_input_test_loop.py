"""
Just a simple test script to loop over various inputs and print 
"input -> function(input)"
"""

def is_empty_or_whitespace(s: str) -> bool:
    return not s or s.isspace()

result = is_empty_or_whitespace

inputs = [
    "",
    " ",
    "     ",
]

for _ in inputs:
    print(f"{_} -> {result(_)}")