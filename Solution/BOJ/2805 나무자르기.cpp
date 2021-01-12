#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int main() {
	int N, height;
	ll mid, M, cut;
	vector<int> tree;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		tree.push_back(tmp);
	}
	
	int start = 0;
	int end = *max_element(tree.begin(), tree.end());
	int result = 0;
	while (start <= end) {
		mid = (start + end) / 2;
		cut = 0;
		for (int i = 0; i < N; i++) {
			if (tree[i] > mid) {
				cut += (tree[i] - mid);
			}
		}
		if (cut >= M) {
			result = mid;
			start = mid + 1;
		} else {
			end = mid - 1;
		}
	}
	
	cout << result << endl;
	return 0;
}
