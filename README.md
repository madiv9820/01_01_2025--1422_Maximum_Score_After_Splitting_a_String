# [1422. Maximum Score After Splitting a String](https://github.com/madiv9820/01_01_2025--1422_Maximum_Score_After_Splitting_a_String) (All Approaches)
 
- ## Approach 1: Brute Force

    - ### Intuition
        The problem requires splitting the string `s` into two non-empty parts and maximizing the sum of:
        - The count of `'0'`s in the left part.
        - The count of `'1'`s in the right part.

        For each possible split, we can calculate the scores of the left and right parts and keep track of the maximum score. The goal is to evaluate every valid split and choose the one that yields the highest score.

    - ### Approach
        1. **Base Cases**:
            - If the string has only one character, the score is `1` because it satisfies the condition of being a valid split.
            - If the string has two characters, calculate the score directly by counting `'0'` in the first part and `'1'` in the second part.

        2. **Iterate Through Splits**:
            - For every position `ptr` from `0` to `n-2` (ensuring non-empty left and right parts):
                - Divide the string into the left part `[0...ptr]` and the right part `[ptr+1...n-1]`.

        3. **Calculate Scores**:
            - For the left part, count the number of `'0'`s.
            - For the right part, count the number of `'1'`s.
            - Sum the left and right scores to get the total score for the current split.

        4. **Track Maximum Score**:
            - Compare the current split's score with the previously recorded maximum score and update it if the current score is greater.

        5. **Return Result**:
            - After iterating through all possible splits, return the maximum score.

    - ### Code Implementation
        - **Python Solution**
            ```python3 []
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
            ```
        - **C++ Solution**
            ```cpp []
            class Solution {
            public:
                int maxScore(string s) {
                    // Base case: If the string has only 1 character, the maximum score is 1
                    if (s.length() == 1) return 1;
                    
                    // Base case: If the string has 2 characters, calculate the score directly
                    // Score = (left part: count of '0') + (right part: count of '1')
                    if (s.length() == 2) return ((s[0] == '0') ? 1 : 0) + ((s[1] == '1') ? 1 : 0);

                    // Initialize pointer for the split position, string length, and maxScore variable
                    int ptr = 0, n = s.length();
                    int maxScore = 0;

                    // Iterate through all possible split positions
                    // The split is at position `ptr`, where left part is [0...ptr] and right part is [ptr+1...n-1]
                    for (; ptr < n - 1; ++ptr) {
                        int leftScore = 0, rightScore = 0;

                        // Calculate the score for the left part (count of '0')
                        for (int index = ptr; index >= 0; --index)
                            leftScore += ('1' - s[index]); // '1' - s[index] converts '0' to 1 and '1' to 0

                        // Calculate the score for the right part (count of '1')
                        for (int index = ptr + 1; index < n; ++index)
                            rightScore += (s[index] - '0'); // s[index] - '0' converts '1' to 1 and '0' to 0

                        // Update maxScore with the maximum of the current score and the previously stored score
                        maxScore = max(maxScore, leftScore + rightScore);
                    }

                    // Return the maximum score found
                    return maxScore;
                }
            };
            ```

    - ### Time Complexity
        - **$O(N^2)$**:
            - For each split position (`ptr`), we traverse both the left part (from `ptr` to `0`) and the right part (from `ptr+1` to `n-1`).  
            - In the worst case, this results in a quadratic time complexity as we evaluate every possible split.

    - ### Space Complexity
        - **$O(1)$**:
            - No extra data structures are used apart from a few variables for calculations. The solution operates in constant space.

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