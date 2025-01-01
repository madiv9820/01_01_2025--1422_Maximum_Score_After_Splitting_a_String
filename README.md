- ## Approach 2: Prefix Sum

    - ### Intuition
        The task is to maximize the score obtained by splitting the string `s` into two non-empty parts:
        - The left part contributes a score equal to the count of `'0'`s.
        - The right part contributes a score equal to the count of `'1'`s.

        To efficiently calculate the score for each split, we use a running total:
        - Incrementally compute the count of `'0'`s for the left part.
        - Decrementally compute the count of `'1'`s for the right part.

        This allows us to track the scores without recalculating from scratch for each split.

    - ### Approach
        1. **Initialization**:
            - Start with `leftScore = 0` and `rightScore = 0`.
            - Compute the total number of `'1'`s in the string as the initial `rightScore`.

        2. **Iterate Through Splits**:
            - Loop through all possible split points (up to `n-2` to ensure both parts are non-empty).
            - For each character:
                - Add to `leftScore` if the character is `'0'`.
                - Subtract from `rightScore` if the character is `'1'`.

        3. **Update Maximum Score**:
            - For each split, calculate the total score as `leftScore + rightScore`.
            - Update `maxScore` if the current score is greater.

        4. **Return Result**:
            - After evaluating all splits, return the maximum score found.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                int maxScore(string s) {
                    // Initialize variables to track the maximum score, left score, and right score
                    int maxScore = 0, leftScore = 0, rightScore = 0;
                    int n = s.length(); // Get the length of the string

                    // Calculate the initial right score (count of '1's in the entire string)
                    for (int index = 0; index < n; ++index) 
                        rightScore += (s[index] - '0'); // Convert character to integer and add it to right score

                    // Iterate through the string, stopping at the second last character to ensure non-empty left and right parts
                    for (int index = 0; index < n - 1; ++index) {
                        // Update the left score by counting '0's in the left part
                        leftScore += ('1' - s[index]); // '1' - s[index] converts '0' to 1 and '1' to 0

                        // Update the right score by subtracting the current character's value ('1' or '0')
                        rightScore -= (s[index] - '0'); // Subtract the value of the current character from right score

                        // Calculate the total score for the current split and update the maximum score
                        maxScore = max(maxScore, leftScore + rightScore);
                    }

                    // Return the maximum score found across all possible splits
                    return maxScore;
                }
            };
            ```

    - ### Time Complexity
        - **$O(N)$**:
            - Calculating the initial `rightScore` takes **$O(N)$**.
            - Iterating through the string and updating `leftScore` and `rightScore` also takes **$O(N)$**.
            - Overall, the solution runs in linear time.

    - ### Space Complexity
        - **$O(1)$**:
            - No additional data structures are used.
            - The solution only uses a few variables for calculation, resulting in constant space usage.