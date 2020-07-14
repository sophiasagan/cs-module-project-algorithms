# Eating Cookies

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

Thus, `eating_cookies(3)` should return an answer of 4.

Can you implement a solution that runs fast enough to pass the large input test?

## Testing

For this problem, there's a test that tests your implementation with small inputs (n <= 10). There's also a separate test that tests your implementation with large inputs (n >= 50). 

You'll find that without implementing performance optimizations into your solution, your solution will likely hang on the large input test. 

To run the tests separately, run `python test_eating_cookies.py -k small` in order to run jsut the small input test. Run `python test_eating_cookies.py -k large` to execute just the large input test. If you want to run both tests, just run `python test_eating_cookies.py`.

You can also test your implementation manually by executing `python eating_cookies.py [n]`.

## Hints
 * Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
 * Think about base cases that we would want our recursive function to stop recursing on. How many ways are there to eat 0 cookies? What about a negative number of cookies? 
 * Once we've established some base cases, how can we recursively call our function such that we move towards one or more of these base cases?
 * As far as performance optimizations go, caching/memoization might be one avenue we could go down? How should we make a cache available to our recursive function through multiple recursive calls?

 Memoization effectively refers to remembering ("memoization" → "memorandum" → to be remembered) results of method calls based on the method inputs and then returning the remembered result rather than computing the result again. You can think of it as a cache for method results. For further details, see page 387 for the definition in Introduction To Algorithms (3e), Cormen et al.

A simple example for computing factorials using memoization in Python would be something like this:

```factorial_memo = {}
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]```
You can get more complicated and encapsulate the memoization process into a class:

```class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]```
Then:

```def factorial(k):
    if k < 2: return 1
    return k * factorial(k - 1)

factorial = Memoize(factorial)```


New to Python 3.2 is functools.lru_cache. By default, it only caches the 128 most recently used calls, but you can set the maxsize to None to indicate that the cache should never expire:

```import functools

@functools.lru_cache(maxsize=None)
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)```

This function by itself is very slow, try fib(36) and you will have to wait about ten seconds.

Adding lru_cache annotation ensures that if the function has been called recently for a particular value, it will not recompute that value, but use a cached previous result. In this case, it leads to a tremendous speed improvement, while the code is not cluttered with the details of caching.

Memoization is basically saving the results of past operations done with recursive algorithms in order to reduce the need to traverse the recursion tree if the same calculation is required at a later stage.

see http://scriptbucket.wordpress.com/2012/12/11/introduction-to-memoization/

Fibonacci Memoization example in Python:

```fibcache = {}
def fib(num):
    if num in fibcache:
        return fibcache[num]
    else:
        fibcache[num] = num if num < 2 else fib(num-1) + fib(num-2)
        return fibcache[num]```