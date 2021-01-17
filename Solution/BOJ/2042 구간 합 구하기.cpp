#include <iostream>

typedef long long ll;
using namespace std;
int N, M, K, S;

long makeTree(int node, int left, int right, ll arr[], ll tree[]) {
	if (left == right) {
		if (left <= N) {
			return tree[node] = arr[left];	
		} else {
			return tree[node] = 0;
		}
	}
	
	int mid = (left + right) / 2;
	tree[node] = makeTree(node * 2, left, mid, arr, tree);
	tree[node] += makeTree(node * 2 + 1, mid + 1, right, arr, tree);
	
	return tree[node];
}

long query(int node, int left, int right, int qLeft, int qRight, ll tree[]) {
	if (right < qLeft || qRight < left) {
		return 0;
	} else if (qLeft <= left && right <= qRight) {
		return tree[node];
	} else {
		int mid = (left + right) / 2;
		return query(node * 2, left, mid, qLeft, qRight, tree) + query(node * 2 + 1, mid + 1, right, qLeft, qRight, tree);
	}
}

void update(int node, int left, int right, int index, ll diff, ll tree[]) {
	if (left <= index && index <= right) {
		tree[node] += diff;
		if (left != right) {
			int mid = (left + right) / 2;
			update(node * 2, left, mid, index, diff, tree);
			update(node * 2 + 1, mid + 1, right, index, diff, tree);
		}
	}
}

int main() {
	cin >> N >> M >> K;
	ll arr[N+1];
	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}
	S = 1;
	while (S < N) {
		S *= 2;
	}
	ll tree[S * 2];
	makeTree(1, 1, S, arr, tree);
	for (int i = 0; i < M + K; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		if (a == 1) {
			update(1, 1, S, b, c - arr[b], tree);
		} else {
			cout << query(1, 1, S, b, c, tree) << endl;
		}
	}
}
