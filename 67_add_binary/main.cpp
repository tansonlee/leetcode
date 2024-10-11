class Solution {
public:
    string addBinary(string a, string b) {
        std::ostringstream oss;

        int carry = 0;
        for (int i = 0; i < max(a.size(), b.size()); ++i) {
            int a_digit = i < a.size() ? a[a.size() - i - 1] - '0' : 0;
            int b_digit = i < b.size() ? b[b.size() - i - 1] - '0' : 0;

            int digit = (a_digit + b_digit + carry) % 2;
            carry = (a_digit + b_digit + carry) >= 2 ? 1 : 0;

            oss << (char)(digit + '0');
        }

        if (carry) {
            oss << '1';
        }
        
        string result = oss.str();
        reverse(result.begin(), result.end());
        return result;
    }
};
