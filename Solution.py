class Solution:
    def maxScore(self, s: str) -> int:
        # Base case: If the string has only 1 character, the maximum score is 1
        if len(s) == 1:
            return 1
        
        # Base case: If the string has 2 characters, calculate the score directly
        # Score = (left part: count of '0') + (right part: count of '1')
        if len(s) == 2:
            return (1 if s[0] == '0' else 0) + (1 if s[1] == '1' else 0)

        # Initialize the maximum score and the length of the string
        maxScore, n = 0, len(s)

        # Iterate through all possible split positions
        # The split is at position `ptr`, where left part is [0...ptr] and right part is [ptr+1...n-1]
        for ptr in range(n - 1):
            # Initialize scores for the left and right parts
            leftScore, rightScore = 0, 0

            # Calculate the score for the left part (count of '0')
            for index in range(ptr, -1, -1):  # Traverse from `ptr` to the beginning
                leftScore += 1 if s[index] == '0' else 0

            # Calculate the score for the right part (count of '1')
            for index in range(ptr + 1, n):  # Traverse from `ptr + 1` to the end
                rightScore += 1 if s[index] == '1' else 0

            # Update the maximum score with the current split's score
            maxScore = max(maxScore, leftScore + rightScore)

        # Return the maximum score found
        return maxScore