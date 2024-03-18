class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, Comparator.comparingInt(a -> a[0]));

        int result = 0;

        int i = 0;
        while (i < points.length) {
            int[] intersection = {points[i][0], points[i][1]};

            while (i < points.length && intersect(intersection, points[i])) {
                intersection[0] = Math.max(intersection[0], points[i][0]);
                intersection[1] = Math.min(intersection[1], points[i][1]);
                ++i;
            }
            ++result;
        }

        return result;
    }
    
    private boolean intersect(int[] a, int[] b) {
        return !(a[0] > b[1] || b[0] > a[1]);
    }
}
