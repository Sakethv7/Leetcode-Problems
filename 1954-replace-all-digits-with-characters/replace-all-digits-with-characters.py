class Solution:
    def replaceDigits(self, s: str) -> str:
        
        def shift(c, x):
            """
            Shifts the character 'c' by 'x' positions in the alphabet.
            Args:
                c: The character to shift (must be a letter).
                x: The number of positions to shift (must be a digit).
            Returns:
                The shifted character.
            """
            return chr(ord(c) + x)  # Use ASCII values to calculate the new character

        # Initialize an empty list to build the result string
        result = []
        
        # Convert the string into a list for easier indexing
        t = list(s)

        # Iterate through the characters of the string
        for i in range(len(t)):
            if t[i].isdigit():
                # If the character is a digit, apply the shift operation
                result.append(shift(t[i - 1], int(t[i])))
            else:
                # If the character is a letter, append it as is
                result.append(t[i])

        # Join the list of characters back into a string and return
        return "".join(result)
