class Solution {
public:
    vector<list<int>> graph;
    int bfs(int n){
        queue<int> q;
        q.push(0);
        vector<int> dist(n, 1e9);
        unordered_set<int> visited;
        visited.insert(0);
        dist[0] = 0;
        while(! q.empty()){
            int node = q.front();
            if(node == n - 1){
                return dist[node];
            }
            q.pop();
            for(auto ele : graph[node]){
                if(! visited.count(ele)){
                    dist[ele] = 1 + dist[node];
                    q.push(ele);
                    visited.insert(ele);
                }
            }
        }
        return -1;
    }
    vector<int> shortestDistanceAfterQueries(int n, vector<vector<int>>& queries) {
        graph.clear();
        graph.resize(n);
        for(int i = 0; i < n - 1; i++){
            graph[i].push_back(i+1);
        }
        int k = queries.size();
        vector<int> res(k);
        for(int i = 0; i < k; i++){
            graph[queries[i][0]].push_back(queries[i][1]);
            res[i] = bfs(n);
        }
        return res;
    }
};