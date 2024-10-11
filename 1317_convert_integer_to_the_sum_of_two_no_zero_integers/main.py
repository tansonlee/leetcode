class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        for (int i = 1; i < n; ++i) {
            if (!has_zeros(i) && !has_zeros(n - i)) {
                return {i, n - i};
            }
        }

        return {0, 0};
    }

private:
    bool has_zeros(int n) {
        while (n > 0) {
            if (n % 10 == 0) {
                return true;
            }
            n /= 10;
        }

        return false;
    }
};
