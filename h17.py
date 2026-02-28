class Reverse:
    def __init__(self, s: str = ""):
        self._s = s

    def reverse_words(self) -> str:
        words = self._s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

    def reverse_full_string(self) -> str:
        return self._s[::-1]

    def __str__(self) -> str:
        return f"Reverse object with string: '{self._s}'"

    def __repr__(self) -> str:
        return f"Reverse(s='{self._s}')"

user_input = input("Enter a string for reversal demonstration: ")

my_string_reverser = Reverse(s=user_input)

print(f"Original string: '{my_string_reverser._s}'")

reversed_words_output = my_string_reverser.reverse_words()
print(f"Word-by-word reversed string: '{reversed_words_output}'")

reversed_full_string_output = my_string_reverser.reverse_full_string()
print(f"Character-by-character reversed string: '{reversed_full_string_output}'")

print(f"__str__ representation: {my_string_reverser}")
print(f"__repr__ representation: {repr(my_string_reverser)}")
