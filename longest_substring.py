def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    """
    char_map = {}
    left = 0
    max_len = 0

    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]

    print("Running tests for Longest Substring Without Repeating Characters...")
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        status = "PASS" if result == expected else f"FAIL (Expected {expected}, got {result})"
        print(f"Input: '{s}' -> Output: {result} [{status}]")
