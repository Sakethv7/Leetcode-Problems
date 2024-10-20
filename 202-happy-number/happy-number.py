class Solution:
    def isHappy(self, num):
        slow, fast = num, num

        # Detect cycle using slow and fast pointers
        while True:
            slow = self.find_squared_sum(slow)  # Move slow pointer once
            fast = self.find_squared_sum(self.find_squared_sum(fast))  # Move fast pointer twice

            if slow == fast:
                break

        # Check if the cycle ends at 1 (happy number)
        return slow == 1

    def find_squared_sum(self, num):
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit * digit  # Correct the sum of squares
            num //= 10
            
        return total_sum
