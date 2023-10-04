#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    vector<int> dist(n, INT_MAX);
    dist[0] = 0;
    
    vector<vector<int>> graph;
    
    for (int edge_count = 0; edge_count < m; ++edge_count) {
        vector<int> edge(3);
        for (int i = 0; i < 3; ++i) {
            cin >> edge[i];
        }
        graph.push_back(edge);
    }
    
    for (int step = 0; step < n - 1; ++step) {
        for (const vector<int>& edge : graph) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            int w = edge[2];
            if (dist[u] != INT_MAX && dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }
    
    vector<int> answer(n);
    for (int i = 0; i < n; ++i) {
        if (dist[i] != INT_MAX) {
            answer[i] = dist[i];
        } else {
            answer[i] = 30000;
        }
    }
    
    for (int i = 0; i < n; ++i) {
        cout << answer[i] << " ";
    }
    
    return 0;
}
