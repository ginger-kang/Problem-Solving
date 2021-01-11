#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <string>

using namespace std;
int R, C;
char map[51][51];
int cave_x, cave_y;
int hedge_x, hedge_y;
int time;
queue<tuple<int, int, string>> q;

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int bfs() {
	while (!q.empty()) {
		int q_length = q.size();
		time++;
		for (int i = 0; i < q_length; i++) {
			int x = get<0>(q.front());
			int y = get<1>(q.front());
			string ch = get<2>(q.front());
			q.pop();
				
			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];
				if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
					if (ch.compare("S") == 0) {
						if (map[nx][ny] == '.') {
							map[nx][ny] = 'S';
							q.push(make_tuple(nx, ny, "S"));
						} else if (map[nx][ny] == 'D') {
							return 1;
						}
					} else {
						if (map[nx][ny] == '.') {
							map[nx][ny] = '*';
							q.push(make_tuple(nx, ny, "*"));
						}
					} 		
				}
			}
		}
	}
	return 0;
}

int main() {
	cin >> R >> C;
	
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			cin >> map[i][j];
			if (map[i][j] == 'S') {
				hedge_x = i;
				hedge_y = j;
			} else if (map[i][j] == 'D') {
				cave_x = i;
				cave_y = j;
			} else if (map[i][j] == '*') {
				q.push(make_tuple(i, j, "*"));
			}
		}
	}
	q.push(make_tuple(hedge_x, hedge_y, "S"));
	
	if (bfs()) {
		cout << time << endl;
	} else {
		cout << "KAKTUS" << endl;
	}
	
	return 0;
}
