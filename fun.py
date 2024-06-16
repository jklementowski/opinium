# Input
numbers = [1, 2, 3, 4, 5, 6]

# Output
[2, 4, 6]

def select_even(num):
    even = []
    for item in num:
        if (item % 2) == 0:
            even.append(item)
    return even

#print(select_even(numbers))

def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

is_palindrome("A man, a plan, a canal, Panama")

def max_occuring_char(s: str) -> str:
    if not s:
        return None
    
    char_freq = {}
    
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    

    max_char = max(char_freq, key=char_freq.get)
    
    return max_char

print(max_occuring_char("hello"))   

def sum_of_squares(n: int) -> int:
    number = 1
    sum_of_sq_num = 0
    while number <= n:
        sum_of_sq_num += number ** 2
        number += 1
    return sum_of_sq_num


print(sum_of_squares(3))   # Output: 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14
print(sum_of_squares(5))   # Output: 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 1 + 4 + 9 + 16 + 25 = 55

def reverse_string(s: str) -> str:
    return s[::-1]

print(reverse_string("hello"))   # Output: "olleh"
print(reverse_string("python"))  # Output: "nohtyp"
print(reverse_string("12345"))   # Output: "54321"


