def remove_duplicates_preserve_order(numbers: list) -> list:
    list_temp = []
    for item in numbers:
        if not item in list_temp:
            list_temp.append(item)
    return list_temp


print(remove_duplicates_preserve_order([4, 5, 6, 4, 5, 7, 8, 6, 9, 10]))  # Output: [4, 5, 6, 7, 8, 9, 10]
print(remove_duplicates_preserve_order([1, 2, 2, 3, 4, 1, 5]))           # Output: [1, 2, 3, 4, 5]
print(remove_duplicates_preserve_order([10, 20, 20, 10, 30, 40, 50]))    # Output: [10, 20, 30, 40, 50]


def find_longest_substring(s: str) -> (str, int):
    temp_s = ""
    
    for char in s: 
        if not char in temp_s:
            temp_s+=char

    return temp_s, len(temp_s)

print(find_longest_substring("abcabcbb"))
print(find_longest_substring("bbbbb"))
print(find_longest_substring("pwwkew"))
print(find_longest_substring("dvdf"))
