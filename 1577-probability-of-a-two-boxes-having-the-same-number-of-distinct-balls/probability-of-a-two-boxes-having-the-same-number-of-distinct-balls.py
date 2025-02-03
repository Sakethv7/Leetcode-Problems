class Solution:
    def getProbability(self, balls: List[int]) -> float:
        k = len(balls)
        total_balls = sum(balls)  # = 2 * n
        n = total_balls // 2

        # We don't actually need denom separately if we incorporate (2n)! below:
        #   Total distinct permutations = (2n)! / (balls[0]! * ... * balls[k-1]!).

        # Precompute:
        two_n_fact = factorial(total_balls)  # (2n)!
        # Multiply (n!)^2 * product of factorial(balls[i])
        numerator_const = (factorial(n) ** 2)
        for b in balls:
            numerator_const *= factorial(b)

        # We'll do a backtracking over x[i], the number of color i balls that go to box1
        # subject to sum(x[i]) = n,  0 <= x[i] <= balls[i].
        self.result = 0.0
        x = [0]*k

        def backtrack(idx, chosen):
            if idx == k:
                if chosen == n:
                    # Check distinct colors in each box
                    distinct_box1 = sum(1 for i in range(k) if x[i] > 0)
                    distinct_box2 = sum(1 for i in range(k) if balls[i] - x[i] > 0)
                    if distinct_box1 == distinct_box2:
                        # denom_part = ∏( factorial(x[i]) * factorial(balls[i] - x[i]) )
                        denom_part = 1
                        for i in range(k):
                            denom_part *= factorial(x[i]) * factorial(balls[i] - x[i])
                        # fraction(x) = numerator_const / [ (2n)! * denom_part ]
                        fraction_x = numerator_const / (two_n_fact * denom_part)
                        self.result += fraction_x
                return

            max_take = balls[idx]
            for take in range(max_take + 1):
                if chosen + take > n:
                    break
                x[idx] = take
                backtrack(idx + 1, chosen + take)
                x[idx] = 0

        backtrack(0, 0)
        return self.result
