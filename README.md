# Loglazy

a simple (no dependency) helper library to reduce the overhead of your log statements.

---

Loglazy helps by lazily evaluating expensive log statements. It ensures that
these expensive statements are only evaluated when the logger will print them
out. You don't even have to change your main logging library, loglazy integrates
with the standard python `logging` library and uses the way the `logging` library is
implemented to make this possible.

## Usage

the usage is very simple. Loglazy exposes the `Interp` class which only evaluates it's
parameter when string interpolated.

```python
from loglazy import Interp
import logging

logging = logging.getLogger(__name__)


def expensive_computation():
  ...

def main():
  logging.info("starting the main function")
  logging.debug("the millionth prime number is %s", Interp(lambda: expensive_computation()))
```

Interp when run through `repr` and `str` evaluates to whatever the lambda passed into evalautes to.
Python's logging handlers will only interpolate the extra arguments passed into the log statement
if that the handler is currently configured to output that log statement. So you can worry-free
leave expensive debug statements in your code without having to worry about
whether or not that will slow things down in production.
