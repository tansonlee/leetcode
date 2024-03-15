class Solution {
    public boolean asteroidsDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        long curr = mass;

        for (int a : asteroids) {
            if (a <= curr) {
                curr += a;
            } else  {
                return false;
            }
        }

        return true;
    }
}
