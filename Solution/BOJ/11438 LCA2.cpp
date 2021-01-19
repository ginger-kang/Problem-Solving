#include <iostream>
#include <vector>
using namespace std;

int n, m, depth[100010], an[100010][18]; // an -> 지수로(2^0, 2^1...2^17번째 조상) 
vector<int> adj[100010];
bool visited[100010];

void dfs(int parent, int curr, int param_depth) {
	if (visited[curr]) return;
	visited[curr] = true;
	depth[curr] = param_depth;
	an[curr][0] = parent;
	for (int i = 0; i < adj[curr].size(); i++) {
		dfs(curr, adj[curr][i], param_depth + 1);
	}
}

int lca(int a, int b) {
	// a의 깊이가 b보다 더 깊게 만듬(쉽게 처리하기 위해) 
	if (depth[a] < depth[b]) {
		int tmp = a;
		a = b;
		b = tmp;
	}
	// 만약 길이가 서로 다르면
	if (depth[a] != depth[b]) {
		// a -> b까지 깊이를 맞춤
		int diff = depth[a] - depth[b];
		for (int i = 0, j = 1; i <= 17; i++, j *= 2) {
			if (diff & j) {
				a = an[a][i];
			}
		} 
	}
	// depth[a] == depth[b]인 상태
	if (a == b) return a;
	
	for (int i = 17; i >= 0; i--) {
		if (an[a][i] != an[b][i]) {
			a = an[a][i];
			b = an[b][i];
		}
	}
	//LCA의 바로 아래까지 온 상태
	return an[a][0]; 
}

int main() {
	ios_base::sync_with_stdio(false);
	cout.tie(NULL);
	cin.tie(NULL);
	cin >> n;
	for (int i = 0; i < n - 1; i++) {
		int a, b;
		cin >> a >> b;
		// 일단 양방향으로 연결한다 
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	// LCA를 위한 자료 수집: 깊이, 1/2/4/8...번째 조상 
	dfs(1, 1, 1);
	// 2^1, 2^2, 2^3....2^17 조상구하기(sparse table) 
	for (int i = 1; i <= 17; i++) { // 2^i번째 조상 
		for (int j = 1; j <= n; j++) { // 1번 노드...n번노드 
			int tmp = an[j][i-1];
			an[j][i] = an[tmp][i-1];
		}
	}
	cin >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		cout << lca(a, b) << "\n";
	}
}
