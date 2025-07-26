# https://start.interviewing.io/interview-ai?problemId=number-of-palindromic-splits

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Number Of Palindromic Splits

# A palindrome is a string that reads the same forward and backward, like `"abba"`.

# A _palindromic split_ of a string is a way of dividing a string into substrings where every substring is a palindrome.

# Given a string, `s`, return the number of palindromic splits.

# ```
# Example 1:
# s = "abbaab"

# Output: 6
# The palindromic splits are:
# - `a|b|b|a|a|b`
# - `a|bb|a|a|b`
# - `a|b|b|aa|b`
# - `a|bb|aa|b`
# - `abba|a|b`
# - `a|b|baab`

# Example 2:
# s = "aabaa"

# Output: 6
# The palindromic splits are:
# - `a|a|b|a|a`
# - `aa|b|a|a`
# - `a|a|b|aa`
# - `aa|b|aa`
# - `a|aba|a`
# - `aabaa`

# Example 3:
# s = "aaaaa"

# Output: 16

# Example 4:
# s = ""

# Output: 0
# ```

# Constraints:

# - The length of the string is at most `10^4`
# - Each character in the string is a lowercase English letter

# '''
# Boundary Thinking: 
# Lower Bound: Output: O(1) 
# Lower Bound: Task: O(n)
# Upper Bound: Naive: O(n^n)
# Upper Bound: TLE: Quadratic O(n^2)
# '''

# '''
# Dynamic Programming - Top Down + Memoization
# Recursive Formula 
# Base Case: 
# i == n: return 1 

# General Case: 
# f(i) = sum(f(j+1) for j in range(i, n) if (i, j) is palindrone hsh_set)


# To find all palindrome substrings: 
# There are 2 types of palindrome. Odd Palindrome and Even Palindrome 

# hsh_set = {}
# for i in range(n): 
#   hsh_set.add(i, i)
#   # Find Odd Palindrome. 
#   l, r = i-1, i+1
#   while l >= 0 and r < n and s[l] == s[r]: 
#     hsh_set.add(l, r)
#     l -= 1 
#     r += 1 

#   # Find Even Palindrome. 
#   l, r = i, i+1
#   while l >= 0 and r < n and s[l] == s[r]: 
#     hsh_set.add(l, r)
#     l -= 1 
#     r += 1 

# '''

def palindrome_substrings(s): 
    n = len(s)
    hsh_set = set()
    for i in range(n): 
        hsh_set.add((i, i))
        # Find Odd Palindrome. 
        l, r = i-1, i+1
        while l >= 0 and r < n and s[l] == s[r]: 
            hsh_set.add((l, r))
            l -= 1 
            r += 1 

        # Find Even Palindrome. 
        l, r = i, i+1
        while l >= 0 and r < n and s[l] == s[r]: 
            hsh_set.add((l, r))
            l -= 1 
            r += 1 
    return hsh_set 


def no_of_palindrome_splits(s): 
    print(s)
    if not s: return 0 
    n = len(s)
    memo = {}
    hsh_set = palindrome_substrings(s)
    def rec_call(i): 
        if i == n: return 1 
        if i in memo: return memo[i] 

        count = sum(rec_call(j+1) for j in range(i, n) if (i, j) in hsh_set)
        memo[i] = count 
        return count 

    return rec_call(0)
    

print(no_of_palindrome_splits('abbaab'))


print(no_of_palindrome_splits('abbaab'))

print(no_of_palindrome_splits('aaaaa'))

print(no_of_palindrome_splits('a'))

print(no_of_palindrome_splits(''))