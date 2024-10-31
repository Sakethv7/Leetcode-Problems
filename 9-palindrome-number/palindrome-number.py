class Solution:
    def isPalindrome(self, x: int) -> bool:
        #if its an absolute number then only it can be considered for palindrome

        if x< 0:
            return False
# Initialize `divider` to find the largest place value in `x`.
# This helps isolate the most significant digit of the number.
        divider = 1
        while x >= 10 * divider:
            divider *= 10
#Loop until all digits are checked.
        while x:
            left = x//divider # Extract the leftmost digit by dividing `x` by `divider`.
            right = x%10  # Extract the rightmost digit by taking `x % 10`.

            if right!= left: # Step 4: If the leftmost and rightmost digits do not match, it’s not a palindrome.
                return False
     #Remove the leftmost and rightmost digits from `x`. First, remove the leftmost digit by calculating `x % divider` (remainder after removing left digit), then remove the rightmost digit by integer division by 10.
            x = (x % divider) // 10
            
            divider = divider//100 #Update `divider` by reducing it by 2 digits (since we removed 2 digits).

        return True # If all left and right pairs of digits matched, `x` is a palindrome.