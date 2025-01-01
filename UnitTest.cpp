#include <iostream>
#include <vector>
#include "Solution.hpp"

struct testcase {
    string s;
    int output;
};

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;

public:
    UnitTest() {
        testcases = {{"011101", 5}, {"00111", 5}, 
                     {"1111", 3}, {"00", 1}, {"01001", 4}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            int result = obj.maxScore(testcases[i].s);
            cout << "TestCase " << i+1 << ": " << ((result == testcases[i].output) ? "passed":"failed") << endl;            
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}