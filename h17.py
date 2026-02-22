class Reverse:
    def __init__(self, s: str = ""):
        self._s = s

    def reverse_words(self) -> str:
        words = self._s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    def __str__(self) -> str:
        return f"Reverse object with string: '{self._s}'"

    def __repr__(self) -> str:
        return f"Reverse(s='{self._s}')"

user_input = input("Enter a string to reverse word by word: ")

my_string_reverser = Reverse(s=user_input)

print(f"Original string: '{my_string_reverser._s}'")

reversed_output = my_string_reverser.reverse_words()

print(f"Reversed string: '{reversed_output}'")

print(f"__str__ representation: {my_string_reverser}")
print(f"__repr__ representation: {repr(my_string_reverser)}")