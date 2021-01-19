#include <iostream>

using namespace std;

int N, M, parent[1000010];

// a의 부모가 누군지 알려줌 
int findf(int a) {
	if (a == parent[a]) return a;
	// return findf(parent[a]); 재귀 -> 시간초과
	parent[a] = findf(parent[a]);
	return parent[a];
}

// a b 합침 
void unionf(int a, int b) {
	a = findf(a);
	b = findf(b);
	parent[a] = b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
	cin >> N >> M;
	for (int i = 0; i <= N; i++) {
		parent[i] = i;
	}
	while (M-- > 0) {
		int cmd, a, b;
		cin >> cmd >> a >> b;
		if (cmd == 0) {
			unionf(a, b);
		} else {
			if (findf(a) == findf(b)) {
				cout << "YES" << "\n";
			} else {
				cout << "NO" << "\n";
			}
		}
	}
    return 0;
}
