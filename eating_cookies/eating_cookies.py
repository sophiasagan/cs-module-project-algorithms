'''
Input: an integer
Returns: an integer
'''

# fails large test
# def eating_cookies(n):
#     # Your code here
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

# trying cache/memoization
# passes small
# fails large -> takes 
# retrieves large data on test below
# There are 10562230626642 ways for Cookie Monster to each 50 cookies
# cookie_cache = {}
# def eating_cookies(n):
#     # Your code here
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
    
#     elif n in cookie_cache:
#         return cookie_cache[n]
#     else:
#         cookie_cache[n] = n if n < 1 else eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#         return cookie_cache[n]


# trying cache for larger with 2 arguments
# def eating_cookies(n, cookie_cache=None):
#     cookie_cache = [0 for _ in range(0, n+1)]
#     if n < 0:
#         return 0
#     elif n == 0:
#         cookie_cache[0] = 1
#         return 1
#     elif n == 1:
#         cookie_cache[1] = 1
#         return 1
#     elif n == 2:
#         cookie_cache[2] = 2
#         return 2
#     elif n == 3:
#         cookie_cache[3] = 4
#         return 4
#     elif n in cookie_cache:
#         return cookie_cache[n]
#     else:
#         cookie_cache[n] = eating_cookies(n-1, cookie_cache) + eating_cookies(n-2, cookie_cache) + eating_cookies(n-3, cookie_cache)
#         return cookie_cache[n]

# print((eating_cookies(5, [0 for i in range(6)])))
# print((eating_cookies(10, [0 for i in range(11)])))
# print((eating_cookies(15, [0 for i in range(16)])))
# print((eating_cookies(20, [0 for i in range(21)])))
# print((eating_cookies(30, [0 for i in range(31)])))
# print((eating_cookies(35, [0 for i in range(36)])))

# artem AMA instructor hour code:

def eating_cookies(n, cache):
    # Your code here
    # Base case
    if n < 0:
        return 0
    if n == 0:
        return 1

    # Before we try to solve our problem
    # lets see if the answer is already stored in cache
    if cache[n] > 0:
        # this must have been precomputed!
        return cache[n] 

    # How can we GET to the base case
    number_of_ways = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    cache[n] = number_of_ways

    return number_of_ways

# print((eating_cookies(5, [0 for i in range(6)])))
import time

start = time.time()
print(f'{eating_cookies(5, [0 for i in range(6)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

start = time.time()
print(f'{eating_cookies(10, [0 for i in range(11)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

start = time.time()
print(f'{eating_cookies(15, [0 for i in range(16)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

start = time.time()
print(f'{eating_cookies(20, [0 for i in range(21)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

start = time.time()
print(f'{eating_cookies(30, [0 for i in range(31)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

start = time.time()
print(f'{eating_cookies(35, [0 for i in range(36)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n------------------------\n')

'''
13

Result calculated in 0.00500 seconds

------------------------

274

Result calculated in 0.00100 seconds

------------------------

5768

Result calculated in 0.00200 seconds

------------------------

121415

Result calculated in 0.05000 seconds

------------------------

53798080

Result calculated in 20.44561 seconds

------------------------

1132436852

Result calculated in 418.06965 seconds

------------------------
'''


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 25

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



# Fibonacci Memoization example in Python:

# fibcache = {}
# def fib(num):
#     if num in fibcache:
#         return fibcache[num]
#     else:
#         fibcache[num] = num if num < 2 else fib(num-1) + fib(num-2)
#         return fibcache[num]