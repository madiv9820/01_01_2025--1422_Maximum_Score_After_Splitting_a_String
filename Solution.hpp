#include <string>
using namespace std;

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