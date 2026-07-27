from dataclasses import dataclass


@dataclass
class Test:
    input = None
    expected = None
    result = None

    def __init__(self, input, expected, result):
        self.input = input
        self.expected = expected
        self.result = result

    def run(self):
        print(f"input: '{self.input}', expected: '{self.expected}")
        print(f"\tresult: '{self.result}' -> {self.expected == self.result}")


def foo(input):
    return "ABCDE"

tests = [
    Test("Hello", "ABCDE", foo("Hello")),
    Test("Hello", "ABCDE", foo("Hello")),
]

for t in tests:
    t.run()