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
def eating_cookies(n, cookie_cache = {}):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in cookie_cache:
        return cookie_cache[n]
    else:
        cookie_cache[n] = eating_cookies(n-1, cookie_cache) + eating_cookies(n-2, cookie_cache) + eating_cookies(n-3, cookie_cache)
    return cookie_cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 25

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")



# Fibonacci Memoization example in Python:

# fibcache = {}
# def fib(num):
#     if num in fibcache:
#         return fibcache[num]
#     else:
#         fibcache[num] = num if num < 2 else fib(num-1) + fib(num-2)
#         return fibcache[num]