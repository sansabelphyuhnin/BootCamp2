fib.py
import fibonacci

f = fibonacci.fib2
print(f(200))
f(200)

fibonacci.fib(10000)

-----------------

from fibonacci import fib, fib2

fib(500)
print(fib2(500))

----------------

from fibonacci import * 

fib(800)
print(fib2(800))

---------------

import fibonacci as fi

fi.fib(1000)

---------------

import fibonacci as fit

fi.fib(1000)

----------------

from fibonacci import fib as fibonacci
fibonacci(500)