# Examples of Pre-commit Hooks in Action

This document shows examples of how pre-commit hooks automatically fix and check your code.

## Example 1: Black Formatting

### Before (poorly formatted code):

```python
def calculate(x,y,z):
    result=x+y+z
    return result


class MyClass:
  def __init__(self,name):
      self.name=name
```

### After (Black auto-formats):

```python
def calculate(x, y, z):
    result = x + y + z
    return result


class MyClass:
    def __init__(self, name):
        self.name = name
```

## Example 2: isort Import Sorting

### Before (unsorted imports):

```python
import sys
from typing import Dict
import os
from collections import defaultdict
import pytest
from pathlib import Path
```

### After (isort auto-sorts):

```python
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict

import pytest
```

## Example 3: Ruff Linting

### Before (code with issues):

```python
import unused_module  # Unused import

def process_data(data):
    x = 1 + 1  # Unused variable
    if data == None:  # Should use 'is None'
        return []
    return data
```

### After (Ruff fixes):

```python
def process_data(data):
    if data is None:
        return []
    return data
```

## Example 4: mypy Type Checking

### Before (missing/incorrect types):

```python
def add_numbers(a, b):
    return a + b

def process_user(user):
    return user["name"]
```

### After (with type hints):

```python
from typing import Dict, Any

def add_numbers(a: int, b: int) -> int:
    return a + b

def process_user(user: Dict[str, Any]) -> str:
    return user["name"]
```

## Example 5: Trailing Whitespace Removal

### Before:

```python
def hello():
    return "world"
```

### After:

```python
def hello():
    return "world"
```

## Example 6: End of File Fixer

### Before (no newline at end):

```python
def main():
    print("Hello")
```

### After (newline added):

```python
def main():
    print("Hello")

```

## Example 7: Debug Statement Detection

### Will be blocked:

```python
def process():
    import pdb; pdb.set_trace()  # ❌ Commit blocked!
    data = fetch_data()
    return data
```

### Should be removed before committing:

```python
def process():
    data = fetch_data()
    return data
```

## Example 8: Testing with pytest

When you commit Python files, pytest automatically runs:

```bash
$ git commit -m "Add new feature"
Run pytest on changed files...........Passed
- hook id: pytest-check
- duration: 0.34s

...........                          [100%]
Coverage: 100%
11 passed in 0.07s
```

If tests fail, the commit is blocked:

```bash
$ git commit -m "Add broken feature"
Run pytest on changed files...........Failed
- hook id: pytest-check
- exit code: 1

FAILED tests/test_feature.py::test_new_feature - AssertionError
```

## Complete Pre-commit Flow

Here's what happens when you commit:

```bash
$ git add .
$ git commit -m "Add new calculator feature"

Trim trailing whitespace...................Passed
Fix end of files...........................Passed
Check YAML files...........................Passed
Check for large files......................Passed
Check for merge conflicts..................Passed
Format code with Black.....................Passed
Sort imports with isort....................Passed
Lint with Ruff.............................Passed
Type check with mypy.......................Passed
Run pytest.................................Passed

[main abc1234] Add new calculator feature
 2 files changed, 50 insertions(+)
```

## Tips

1. **Let the tools work for you**: Don't worry about formatting manually
2. **Fix issues incrementally**: Address hook failures one at a time
3. **Run manually during development**: Use `make format` and `make lint` while coding
4. **Review auto-fixes**: Always check what the hooks changed with `git diff`
5. **Keep hooks updated**: Run `pre-commit autoupdate` monthly

## Common Hook Failures and Fixes

### "Files were modified by this hook"

**What happened**: A hook auto-fixed your code.

**What to do**: Review changes with `git diff`, then re-add and commit:

```bash
git add .
git commit -m "Your message"
```

### "Type check with mypy...Failed"

**What happened**: Type hint issues detected.

**What to do**: Add or fix type hints in the reported files.

### "Run pytest...Failed"

**What happened**: Tests failed.

**What to do**: Fix the failing tests or the code causing test failures.

## Need Help?

See the [README.md](README.md) for more detailed information or [QUICKSTART.md](QUICKSTART.md) for setup instructions.
