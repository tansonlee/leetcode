import java.util.Stack;
import java.util.Arrays;

class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();

        String[] tokens = Arrays.stream(path.split("/"))
                        .filter(x -> !x.isEmpty())
                        .toArray(String[]::new);

        for (int i = 0; i < tokens.length; ++i) {
            if (tokens[i].equals("..")) {
                if (stack.size() > 0) {
                    stack.pop();
                }
            } else if (tokens[i].equals(".")) {
                // nothing
            } else {
                stack.push(tokens[i]);
            }
        }

        return "/" + String.join("/", stack.toArray(new String[stack.size()]));
    }
}
