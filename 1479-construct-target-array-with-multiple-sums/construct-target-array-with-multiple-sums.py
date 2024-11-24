class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # Calculate the sum of the array
        total_sum = sum(target)

        # Find the index of the maximum value
        max_value_index = target.index(max(target))

       # the remaining sum excluding the maximum value
        remaining_difference = total_sum - target[max_value_index]

        #  Base cases for returning True
        if target[max_value_index] == 1 or remaining_difference == 1:
            return True

        #  Check invalid cases where it's impossible
        if remaining_difference > target[max_value_index] or remaining_difference == 0 or target[max_value_index] % remaining_difference == 0:
            return False

        #  Replace the largest value with the modulus of the remaining difference
        target[max_value_index] %= remaining_difference

        return self.isPossible(target)
