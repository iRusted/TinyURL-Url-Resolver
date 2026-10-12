# Project: TinyURL URL Resolver

Hello! 👋 Thank you for taking the time to check out this project!

This project explores URL shorteners, randomized identifier generation, and the challenges of determining whether a generated identifier corresponds to an active shortened URL.

The script generates an eight-character identifier using randomly selected lowercase letters and digits, constructs a URL, and classifies the HTTP response.

> **Research note:** This project is intended for educational research. Automated testing against third-party services should only be performed with appropriate authorization.

---

## 🔤 Character Generation

The identifier generator selects characters from the following set:

```python
letters_and_numers = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",

    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]