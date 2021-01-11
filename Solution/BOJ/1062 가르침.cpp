#include <iostream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool visited[26];
int maxVal = 0;
int n, k;
vector<string> words;

int getMax() {
	int count = 0;
	bool flag = true;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < words[i].length(); j++) {
			if (visited[words[i][j] - 'a'] == false) {
				flag = false;
				break;
			}
		}
		if (flag) {
			count++;
		}
		flag = true;
	}
	return count;
}

void dfs(int idx, int selectedCount) {
	if (selectedCount == k) {
		maxVal = max(maxVal, getMax());
		return;
	}
	for (int i = idx; i < 26; i++) {
		if (visited[i] == false) {
			visited[i] = true;
			dfs(i, selectedCount + 1);
			visited[i] = false;
		}
	}
}

int main() {
	cin >> n >> k;
	
	if (k < 5) {
		cout << 0 << endl;
		return 0;
	} else if (k == 26) {
		cout << n << endl;
		return 0;
	}
	
	visited['a' - 'a'] = true;
	visited['n' - 'a'] = true;
	visited['t' - 'a'] = true;
	visited['i' - 'a'] = true;
	visited['c' - 'a'] = true;
	
	for (int i = 0; i < n; i++) {
		string word;
		cin >> word;
		words.push_back(word); 
	}
	
	for (int i = 0; i < 26; i++) {
		if (visited[i] == false) {
			dfs(i, 5);
		}
	}
	
	cout << maxVal << endl;
}
