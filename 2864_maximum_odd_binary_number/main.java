class Solution {
    public String maximumOddBinaryNumber(String s) {
        int length = s.length();
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '1') {
                count++;
            }
        }

        StringBuilder str = new StringBuilder();
        for (int i = 0; i < count - 1; ++i) {
            str.append("1");
        }
        for (int i = 0; i < (length - count); ++i) {
            str.append("0");
        }
        str.append("1");

        return str.toString();
    }
}
