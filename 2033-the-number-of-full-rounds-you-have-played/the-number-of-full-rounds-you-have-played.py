class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        loginHours, loginMinutes = map(int, loginTime.split(':'))
        loginTotal = loginHours * 60 + loginMinutes

        # Convert logoutTime to minutes since midnight.
        logoutHours, logoutMinutes = map(int, logoutTime.split(':'))
        logoutTotal = logoutHours * 60 + logoutMinutes

        # If logoutTime is earlier than loginTime, adjust for overnight play.
        if logoutTotal < loginTotal:
            logoutTotal += 24 * 60  # Add 24 hours in minutes

        # Calculate the first valid round start time (rounds start every 15 minutes).
        # Round up to the next multiple of 15 if not already on one.
        first_round = ((loginTotal + 14) // 15) * 15

        # A full round is played if the round's start time + 15 is <= logoutTotal.
        # So the latest valid round start time is logoutTotal - 15.
        last_round = ((logoutTotal - 15) // 15) * 15

        # Count the number of full rounds.
        if first_round > last_round:
            return 0
        else:
            # Each round spans 15 minutes, so we divide the difference by 15 and add 1.
            return ((last_round - first_round) // 15) + 1
        