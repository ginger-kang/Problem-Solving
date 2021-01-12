#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int N;
	cin >> N;
	int map[100001][3];
	int maxMap[2][3];
	int minMap[2][3];
	int maxVal, minVal;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < 3; i++) {
		maxMap[0][i] = minMap[0][i] = map[0][i];
	}
	for (int i = 1; i < N; i++) {
		maxMap[1][0] = map[i][0] + max(maxMap[0][0], maxMap[0][1]);
		maxMap[1][1] = map[i][1] + max(maxMap[0][0], max(maxMap[0][1], maxMap[0][2]));
		maxMap[1][2] = map[i][2] + max(maxMap[0][1], maxMap[0][2]);
		
		minMap[1][0] = map[i][0] + min(minMap[0][0], minMap[0][1]);
		minMap[1][1] = map[i][1] + min(minMap[0][0], min(minMap[0][1], minMap[0][2]));
		minMap[1][2] = map[i][2] + min(minMap[0][1], minMap[0][2]);
		
		for (int j = 0; j < 3; j++) {
			maxMap[0][j] = maxMap[1][j];
			minMap[0][j] = minMap[1][j];
		}
	}
	
	maxVal = max(maxMap[0][0], max(maxMap[0][1], maxMap[0][2]));
	minVal = min(minMap[0][0], min(minMap[0][1], minMap[0][2]));
	
	cout << maxVal << " " << minVal << endl;
	return 0;
}
