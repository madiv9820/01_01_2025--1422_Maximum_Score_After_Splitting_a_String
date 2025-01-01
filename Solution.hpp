#include <string>
using namespace std;

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