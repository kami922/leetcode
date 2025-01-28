class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize two lists to count the trust votes.
        # trust_received[i] will hold the number of people who trust person i.
        # trust_given[i] will hold the number of people person i trusts.
        trust_received = [0] * (n + 1)
        trust_given = [0] * (n + 1)

        # Iterate through each trust relationship in the trust list.
        for giver, receiver in trust:
            # Increment the trust count: giver trusts another person,
            # and the receiver is trusted by another person.
            trust_given[giver] += 1
            trust_received[receiver] += 1

        # Iterate over each person to find the potential town judge.
        for person in range(1, n + 1):
            # The town judge should not trust anyone (trust_given[person] == 0)
            # and should be trusted by everyone else (trust_received[person] == n - 1).
            if trust_given[person] == 0 and trust_received[person] == n - 1:
                return person  # Return the town judge.

        # If no town judge is found, return -1.
        return -1