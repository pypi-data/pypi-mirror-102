# Zanza

[![PyPI version](https://badge.fury.io/py/zanza.svg)](https://badge.fury.io/py/zanza)

Dead-simple string obfuscation algorithm.

Obfuscation works by identifying the Unicode code points (character codes) of
each character in the input string. The return value is a *list*, in which the
first element is also a list containing the first character's code point digits.
The rest of the elements are the code point delta values, where each element is
compared to the previous one.

As the project supports **Python 3.0 and up**, all Unicode strings should work.

## Installation

To install as a **project dependency**, or **global package**, execute the
following command in the project's directory:

    pip install zanza

To use as a standalone **command-line utility**, add the `--user` flag to the
previous command:

    pip install --user zanza

## Usage

This package contains scripts for both string _obfuscation_ (`zanza`) and
_deobfuscation_ (`dezanza`)

### Obfuscation

```python
>>> from zanza import zanza

>>> zanza("I am awesome!")
[[7, 3], -41, 65, 12, -77, 65, 22, -18, 14, -4, -2, -8, -68]

>>> zanza("Emojis will work, too: 💪")
[[6, 9], 40, 2, -5, -1, 10, -83, 87, -14, 3, 0, -76, 87, -8, 3, -7, -63, -12, 84, -5, 0, -53, -26, 65501]

>>> zanza("""Another
... fancy
... stuff""")
[[6, 5], 45, 1, 5, -12, -3, 13, -104, 92, -5, 13, -11, 22, -111, 105, 1, 1, -15, 0]
```

In the command line input can be passed as a *script argument* or from *stdin*.

```bash
$ zanza "foo bar baz"
[[1, 0, 2], 9, 0, -79, 66, -1, 17, -82, 66, -1, 25]

$ echo "Encrypt me" | zanza
[[6, 9], 41, -11, 15, 7, -9, 4, -84, 77, -8]
```

### Deobfuscation

```python
>>> from dezanza import dezanza

>>> dezanza([[8, 3], 18, -2, 15, -13, 15, -84, 83, 1, -2, -9, 5, -7, -71, 82, -13, 17, -17, -4, 11, -7, -1])
'Secret string revealed'

>>> dezanza([[7, 8], 33, -101, 98, 3, -1, -7, -2, 13, -104, 101, -13, 4, 15, -2, -16, -2, 19, -15, -1])
'No\nlonger\nobfuscated'
```

Using the command line:

```bash
$ dezanza "[[7, 6], 35, 0, -4, -75, 65, 19, -84, 77, -8, -69, 78, 1, 8]"
Look at me now

$ echo "[[7, 3], 43, -84, 87, -8, 3, -7, 8, -82]" | dezanza
It works!
```

## License

[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)
