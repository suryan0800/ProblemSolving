# Problem Statement
# You are given a password string and a permutation of attacks in the form of a list of integers.
# At each time period, one attack is executed, and the password is updated by removing the character at the index specified by the attack.
# Attacks are irreversible, if attack spans more than m. An attack affects all the combination of password that is formed along with an attacked character. 
# The task is to find the time period at which the password becomes irrecoverable. 

# Example: 
# Input: password = "abcde", attacks = [2, 1, 3, 4, 5], m = 12
# Output: 3
# Explanation: 
# at time 1, password combination that include index 2 are 8
# at time 2, password combination that include index 2 & 1 are 8 + 1 = 9
# at time 3, password combination that include index 2, 1 & 3 are 9 + 3 = 12
import bisect 

def count_combinations(n): 
    return n * (n + 1) // 2

def count_combinations_with_attack(mid, max_combinations, hsh_map, n, hsh_combinations):
    min_ind, max_ind = hsh_map[mid]
    left_combinations = count_combinations(min_ind)
    right_combinations = count_combinations(n - 1 - max_ind)
    combinations = max_combinations - (left_combinations + right_combinations)
    hsh_combinations[mid] = combinations
    return combinations

def password_attack(password, attacks, m):
    n = len(password)

    min_ind = n + 1 
    max_ind = -1
    hsh_map = {}
    for ind, attack in enumerate(attacks):
        min_ind = min(min_ind, attack - 1)
        max_ind = max(max_ind, attack - 1)
        hsh_map[ind] = (min_ind, max_ind)

    max_combinations = count_combinations(n)

    hsh_combinations = {}
    if n == 1: 
        return 1  
    if max_combinations < m:
        return n 
    comb_1 = count_combinations_with_attack(0, max_combinations, hsh_map, n, hsh_combinations)
    if m <= comb_1: 
        return 1 
    l = 0 
    r = n-1 
    
    while (r - l) > 1: 
        mid = (l + r) // 2
        combinations = count_combinations_with_attack(mid, max_combinations, hsh_map, n, hsh_combinations)
        if combinations < m:
            l = mid  
        else: 
            r = mid  
    print(hsh_combinations, l, r)
    count_combinations_with_attack(r, max_combinations, hsh_map, n, hsh_combinations)
    return r + 1 if hsh_combinations[r] >= m else -1

password_attack("abcde", [2, 1, 3, 4, 5], 6)  # Example usage