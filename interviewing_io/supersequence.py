# https://start.interviewing.io/interview-ai?problemId=supersequence&mode=shuffle

# Your previous Plain Text content is preserved below:

# Hello! Your interview question is below. Write code in this pad just like you would normally – your AI Interviewer will be able to see it.

# # Supersequence

# A _supersequence_ of a string `s` is another string that contains all the same letters of `s` in the same relative order. For instance, `"aabbcc"` is a supersequence of `"abc"`, but not of `"bca"`.

# Given a non-empty array of strings, `arr`, where each string consists only of lowercase English letters, determine if it is possible to construct a _single_ supersequence of all the strings in `arr` such that no letter appears more than once. Return `true` if such a supersequence exists and `false` otherwise.

# ```
# Example 1. arr = ["abc", "bde", "df", "cfe"]
# Output: True. "abcdfe" is a supersequence.

# Example 2. arr = ["ab", "ba"]
# Output: False. Any supersequence would have to
# - include 'a' twice (like "aba") or
# - include 'b' twice (like "bab").

# Example 3. arr = ["aa"]
# Output: False.
# ```

# Constraints:

# - The length of each string is at most `100`
# - Each string consists of lowercase English letters

# '''
# n - length of array 
# s = length of string 
# lower bound: Output: O(1) 
# lower bound: Task: O(n*s)
# Upper Bound: Naive: 
# '''

# 'abc', 'adc'

# example 1: 
# a -> b -> c 
# b -> d -> e 
# d -> f 
# c -> f -> e  
# doesn't form a cycle, so can form a super string 

# example 2: 
# a -> b 
# b -> a 
# forms a cycle, so cannot form a super string 

def build_adjacency_set(arr: list[str]): 
    adjacency_set = {} 
    for s in arr: 
        n = len(s) 
        for i in range(n): 
            ch1 = s[i] 
            if ch1 not in adjacency_set: 
                adjacency_set[ch1] = set()
            if (i+1) != n: 
                ch2 = s[i+1]
                adjacency_set[ch1].add(ch2)
    return adjacency_set

def does_form_supersequence(arr: list[str]): 
    # To-Do - Adjacency Set 
    print()
    print(arr)
    adjacency_set = build_adjacency_set(arr)
    # print(adjacency_set)
    in_degree = {ch: 0 for ch in adjacency_set} 
    for ch1 in adjacency_set: 
        for ch2 in adjacency_set[ch1]: 
            in_degree[ch2] = in_degree.get(ch2, 0) + 1 
    # print(in_degree)
    
    in_degree_0 = [ch for ch in in_degree if in_degree[ch] == 0]
    topo_arr = []
    while(in_degree_0): 
        ch1 = in_degree_0.pop()
        topo_arr.append(ch1)
        for ch2 in adjacency_set[ch1]: 
            in_degree[ch2] -= 1 
            if in_degree[ch2] == 0: 
                in_degree_0.append(ch2) 

    # print(topo_arr)
    if len(topo_arr) == len(adjacency_set): 
        return True 
    return False 


print(does_form_supersequence(['ab', 'ba']))

print(does_form_supersequence(['ab', 'bc', 'ca']))

print(does_form_supersequence(['ab', 'bc', 'cd', 'de']))

print(does_form_supersequence(["abc", "bde", "df", "cfe"]))

print(does_form_supersequence(["aa"]))
