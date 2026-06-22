import time

def typewritter(
    text: str, 
    char_delay: float = 0.05,
    line_delay = 1
) -> None:
    for _ in text:
        print(_, end='', flush=True)
        time.sleep(char_delay)

    print()
    time.sleep(line_delay)


class Typewritter:
    def __init__(self, char_delay: float = 0.05, line_delay:float = 1):
        self.char_delay = char_delay
        self.line_delay = line_delay

    def print(self, text: str) -> None:
        for _ in text:
            print(_, end='', flush=True)
            time.sleep(self.char_delay)

        print()
        time.sleep(self.line_delay)


lines = [
    "Hello Craig",
    "This is a very long sentence",
    "SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 22-23: truncated escape",
]

tw = Typewritter()



for _ in lines:
    # typewritter(_)
    tw.print(_)


