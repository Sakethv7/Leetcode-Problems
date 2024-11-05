class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:

        def dfs(pattern, string, mapping):
            if not pattern and not string:  # if both pattern and string are exhausted, a valid mapping is found
                return True
            if not pattern: # If pattern is empty but string still has characters, mapping is invalid
                return False

            # Iterate through possible substrings for the current pattern character
            for end in range(1, len(string) - len(pattern) + 2):
                # Current substring from string and current character from pattern
                current_char = pattern[0]
                current_substring = string[:end]

                # Check if current pattern character already has a mapping
                if current_char not in mapping and current_substring not in mapping.values():
                    mapping[current_char] = current_substring # Create a new mapping and proceed with recursion
                    if dfs(pattern[1:], string[end:], mapping):
                        return True
                    del mapping[current_char]  # Backtrack by removing the mapping
                elif current_char in mapping and mapping[current_char] == current_substring:
                    # If the current pattern character is already mapped and matches the substring,
                    # continue to the next character in the pattern and substring
                    if dfs(pattern[1:], string[end:], mapping):
                        return True
            return False  # No valid mapping found for this pattern and string combination

        return dfs(pattern, string, {}) # Call dfs function with initial parameters

