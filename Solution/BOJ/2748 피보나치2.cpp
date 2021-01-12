#include <iostream>

using namespace std;
typedef long long ll;

int main() {
	int N;
	ll data[91];
	cin >> N;
	
	data[0] = 0;
	data[1] = 1;
	data[2] = 1;
	
	for (int i = 3; i < N+1; i++) {
		data[i] = data[i-1] + data[i-2];
	}
	
	cout << data[N] << endl;
	return 0;
}
