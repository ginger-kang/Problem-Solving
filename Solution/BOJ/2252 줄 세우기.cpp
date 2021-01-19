#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M, indegree[32001]; 
vector<int> adj[32001];
queue<int> q;

int main() {
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
    	int a, b;
    	cin >> a >> b;
    	adj[a].push_back(b);
    	indegree[b]++; // b에 들어오는 노드 추가 
	}
	
	// indegree가 0인 것을 찾는다.
	// 큐를 통해 모아놓는다. 
	for (int i = 1; i <= N; i++) {
		if (indegree[i] == 0) {
			q.push(i);
		}
	}
	
	// 모아놓은 것을 하나씩 큐에 뽑으면서 출력
	while(!q.empty()) {
		int cur = q.front();
		q.pop();
		cout << cur << " "; 
		// 연결된 것들의 간선을 하나씩 줄여준다. 
		for (int i = 0; i < adj[cur].size(); i++) {
			int next = adj[cur][i];
			indegree[next]--;
			if (indegree[next] == 0) {
				q.push(next);
 			}
		}
	}
}
