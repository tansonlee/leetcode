import java.util.Arrays;

class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        int result = 0;

        Arrays.sort(tokens);
        int front = 0;
        int back = tokens.length - 1;

        while (front <= back) {
            if (power >= tokens[front]) {
                power -= tokens[front];
                result++;
                front++;
            } else if (front < back && result > 0) {
                power += tokens[back];
                result--;
                back--;
            } else {
                break;
            }
        }

        return result;
    }
}
