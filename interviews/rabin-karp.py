def hash_code(s, base=256, prime=999979):
    """Compute the hash code for a string using a rolling hash function."""
    hash_value = 0
    for char in s:
        hash_value = (hash_value * base + ord(char)) % prime
    return hash_value

def rolling_hash(k, hash_value, old_char, new_char, base=256, prime=999979):
    """Update the hash value by removing the old character and adding the new character."""
    print(pow(base, k-1), ord(old_char))
    hash_value = (base * (hash_value - ord(old_char) * pow(base, k-1)) + ord(new_char)) % prime
    return hash_value if hash_value >= 0 else hash_value + prime


hash_value = hash_code("ABC") 
print(hash_value) 

hash_value = hash_code("DAB") 
print(hash_value) 

rolling_hash_value = rolling_hash(3, hash_code('DAB'), 'D', 'C') 
print(rolling_hash_value) 