#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int N, S;
	int data[100001];
	cin >> N >> S;
	for (int i = 0; i < N; i++) {
		cin >> data[i];
	}
	
	int start = 0;
	int end = 0;
	int sum = data[0];
	int result = 100001;
	while (1) {
		if (sum >= S) {
			result = min(result, (end - start + 1));
			sum -= data[start++];
		} else if (sum < S) {
			sum += data[++end];
		}
		if (end == N) {
			break;
		}
	}
	if (result == 100001) {
		cout << 0 << endl;
	} else {
		cout << result << endl;	
	}
	return 0;
}
