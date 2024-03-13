class Solution {
    public int pivotInteger(int n) {
        if (n == 1) return 1;
        int before = 1;
        int after = (n * (n + 1)) / 2;

        for (int i = 1; i <= n; ++i) {
            before += i + 1;
            after -= i;
            if (before == after) {
                return i + 1;
            }
        }

        return -1;
    }
}
