# TinyURL URL Resolver

Hello! Thank you for taking the time to check out this project.

This project generates random eight-character identifiers using lowercase letters and numbers, constructs URLs, and classifies HTTP responses.

## Character Generation

The script uses the following set of characters:

```python
letters_and_numers = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]
```

Each identifier contains eight randomly selected characters.

With 36 possible characters per position, the theoretical search space is:

$$
S = 36^8 = 2{,}821{,}109{,}907{,}456
$$

This represents approximately 2.82 trillion possible combinations. It describes the generator's search space, not the total number of URLs used by TinyURL.

## Average Attempts to Find a Match

For a uniformly random identifier space of size $S$, containing $V$ active identifiers, the expected number of independent guesses until the first match is:

$$
E[N] = \frac{S}{V}
$$

Where:

- $E[N]$ is the expected number of attempts until the first match.
- $S$ is the total number of possible identifiers.
- $V$ is the number of active identifiers within that search space.

This model assumes that identifiers are selected uniformly, the active set remains fixed, and guesses are independent.

This is a theoretical model, not an estimate of TinyURL's actual inventory. Without reliable information about its active identifiers, the actual probability of finding a match is unknown.

## Response Classification

The script records HTTP responses in separate text files.

| HTTP Response | Output File | Description |
|---|---|---|
| `200 OK` | `valid_urls.txt` | Response classified as potentially valid |
| `404 Not Found` | `invalid_urls.txt` | Resource reported as not found |
| Other status codes | `other_urls.txt` | Response requiring further interpretation |

Network timeouts and other request exceptions are handled separately.

HTTP status codes alone do not always establish whether a shortened URL is valid. Redirects and destination responses can affect the result.

## Technologies Used

- Python
- Requests
- Random identifier generation
- File handling
- Exception handling

## Feedback

This is my first major public programming project, and I am still learning.

Feedback, suggestions, and bug reports are welcome.

Thank you for taking the time to check out my work!