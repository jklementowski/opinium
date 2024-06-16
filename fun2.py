def can_form_anagram(str1: str, str2: str) -> bool:
    def count_chars(s):
        count = {}
        s = s.lower()
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        return count
    str1_count = count_chars(str1)
    str2_count = count_chars(str2)

    for char in str1_count:
        if str1_count[char] > str2_count.get(char,0):
            return False
    
    return True



print(can_form_anagram("listen", "silent"))       # Output: True
print(can_form_anagram("triangle", "integral"))   # Output: True
print(can_form_anagram("apple", "pale"))          # Output: False
print(can_form_anagram("hello", "oolleh"))        # Output: True
print(can_form_anagram("test", "ttewxyz"))        # Output: True
print(can_form_anagram("anagram", "mangara"))     # Output: True
print(can_form_anagram("test", "tt"))             # Output: False
