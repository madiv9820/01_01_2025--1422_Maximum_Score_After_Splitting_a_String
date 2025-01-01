class Solution:
    def maxScore(self, s: str) -> int:
        # Initialize variables:
        # - maxScore: Tracks the maximum score found so far
        # - leftScore: Counts the number of '0's in the left part
        # - rightScore: Counts the number of '1's in the right part
        maxScore = leftScore = rightScore = 0
        n = len(s)  # Get the length of the string

        # Calculate the initial right score (count of '1's in the entire string)
        for index in range(n):
            rightScore += 1 if s[index] == '1' else 0

        # Iterate through the string, stopping at the second last character
        # to ensure both left and right parts are non-empty
        for index in range(n - 1):
            # Update left score: Increment count for '0' in the left part
            leftScore += 1 if s[index] == '0' else 0
            
            # Update right score: Decrement count for '1' in the right part
            rightScore -= 1 if s[index] == '1' else 0
            
            # Update the maximum score by comparing the current split's score
            maxScore = max(maxScore, leftScore + rightScore)

        # Return the maximum score found
        return maxScore