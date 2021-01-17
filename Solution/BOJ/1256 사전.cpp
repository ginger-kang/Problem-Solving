#include <iostream>
#include <string>
#include <algorithm>

typedef long long ll;
using namespace std;

ll dp[201][201];
int N, M, K;
string sb;

int combination(int n, int r) {
	if (n == r || r == 0) {
		return 1;
	} else if (dp[n][r] != 0) {
		return dp[n][r];
	} else {
		return dp[n][r] = min((int) 1e9, (combination(n-1, r-1) + combination(n-1, r)));
	}
}

void query(int n, int m, int k) {
	if (n + m == 0) {
		return;
	} else if (n == 0) {
		sb.append(1, 'z');
		query(n, m-1, k);
	} else if (m == 0) {
		sb.append(1, 'a');
		query(n-1, m, k);
	} else {
		int leftCount = combination(n + m - 1, m);
		if (leftCount >= k) {
			sb.append(1, 'a');
			query(n - 1, m, k);
		} else {
			sb.append(1, 'z');
			query(n, m-1, k - leftCount);
		}
	}
}

int main() {
	cin >> N >> M >> K;
	if (K > combination(N + M, M)) {
		cout << "-1" << endl;
	} else {
		query(N, M, K);
	}
	cout << sb;
}
