class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
        if (k == 1) {
            return true;
        }

        for (int i = 0; i < m; ++i) {
            if (pattern_from(i, arr, m, k)) {
                return true;
            }
        }

        return false;
    }

private:
    bool pattern_from(int start, vector<int>& arr, int m, int k) {
        int repeats = 1;

        for (int i = start + m; i < arr.size() - m + 1; i += m) {
            if (eq_subarray(arr, i, i - m, m)) {
                repeats += 1;
            } else {
                repeats = 1;
            }

            if (repeats >= k) {
                return true;
            }
        }

        return false;
    }

    bool eq_subarray(vector<int>& arr, int s1, int s2, int m) {
        for (int i = 0; i < m; ++i) {
            if (arr[s1 + i] != arr[s2 + i]) {
                return false;
            }
        }

        return true;
    }
};
