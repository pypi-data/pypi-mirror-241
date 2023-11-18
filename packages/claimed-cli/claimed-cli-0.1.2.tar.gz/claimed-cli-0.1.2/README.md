# cli
CLAIMED CLI - all components available via cli at your fingertips

## Installation

```bash
pip install claimed
```

## Usage
Run an operator locally:
```bash
claimed --component component-name [--component-parameters-name component-parameters-value ...]

# Example
claimed --component blumenstiel/claimed-generate-random-numbers --num_random 5
```

Create operators using [C3](https://github.com/claimed-framework/c3):
```bash
claimed create operator <file> -r <repository> -v <version>
```
