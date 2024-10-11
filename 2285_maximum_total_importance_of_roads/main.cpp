class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        // Assign nodes with more neighbors a higher value.

        // First, determine the value of each node.
        vector<pair<int, int>> neighbors;
        for (int i = 0; i < n; ++i) {
            neighbors.push_back({0, i});
        }

        for (auto& road : roads) {
            neighbors[road[0]].first++;
            neighbors[road[1]].first++;
        }

        sort(neighbors.begin(), neighbors.end(), compare);

        unordered_map<int, int> node_to_value;
        for (int i = 0; i < neighbors.size(); ++i) {
            node_to_value[neighbors[i].second] = i + 1;
        }

        // Second, determine the sum of importances.
        long long result = 0;
        for (auto &road : roads) {
            result += node_to_value[road[0]];
            result += node_to_value[road[1]];
        }

        return result;
    }

private:
    // Comparator function to sort by the first element of the pair (the number)
    static bool compare(const std::pair<int, int>& a, const std::pair<int, int>& b) {
        return a.first < b.first;
    }
};
