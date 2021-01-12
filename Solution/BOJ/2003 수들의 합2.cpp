#include <iostream>

using namespace std;

int main() {
	int N, M;
	int cnt = 0;
	int data[10001];

	cin >> N >> M;
	int start = 0;
	int end = 0;
	
	for (int i = 0; i < N; i++) {
		cin >> data[i];
	}
	int sum = data[0];
	while (1) {
		if (sum == M) {
			cnt++;
			sum -= data[start++];
		} else if (sum < M) {
			sum += data[++end];
		} else if (sum > M) {
			sum -= data[start++];
		}
		if (end == N) {
			break;
		}
	}
	cout << cnt << endl;
	return 0;
}
