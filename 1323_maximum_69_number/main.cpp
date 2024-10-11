class Solution {
public:
    int maximum69Number (int num) {
        int position = -1;

        int n = num;
        int curr_place = 0;
        while (n > 0) {
            if (n % 10 == 6) {
                position = curr_place;
            }

            curr_place += 1;
            n /= 10;
        }

        if (position == -1) {
            return num;
        } else {
            return num + 3 * (pow(10, position));
        }
    }
};
