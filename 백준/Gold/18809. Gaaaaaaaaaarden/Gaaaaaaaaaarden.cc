#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second

#define u first
#define dist second
#define pos second

int n, m, g, r;
int board[50][50];

vector<pair<int, int>> pos;
int ans = 0;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

void bfs(vector<pair<int, int>>& gv, vector<pair<int, int>>& rv) {
  pair<int, int> vis[50][50];

  queue<pair<int, pair<int, int>>> q;

  for (auto c : gv) {
    q.push({1, c});
    vis[c.x][c.y].u = 1;
    vis[c.x][c.y].dist = 1;
  };

  for (auto c : rv) {
    q.push({2, c});
    vis[c.x][c.y].u = 2;
    vis[c.x][c.y].dist = 1;
  };

  int cnt = 0;

  while (!q.empty()) {
    pair<int, pair<int, int>> cur = q.front();
    q.pop();

    if (vis[cur.pos.x][cur.pos.y].u == 3) continue;

    for (int dir = 0; dir < 4; dir++) {
      int nx = cur.pos.x + dx[dir];
      int ny = cur.pos.y + dy[dir];

      if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
      if (board[nx][ny] == 0) continue;

      if (vis[nx][ny].u == 0) {
        q.push({cur.u, {nx, ny}});

        vis[nx][ny].dist = vis[cur.pos.x][cur.pos.y].dist + 1;
        vis[nx][ny].u = cur.u;
      } else if ((vis[nx][ny].dist == vis[cur.pos.x][cur.pos.y].dist + 1) &&
                 (vis[nx][ny].u == 1 && cur.u == 2 ||
                  vis[nx][ny].u == 2 && cur.u == 1)) {
        vis[nx][ny].u = 3;
        cnt++;
      }
    }
  }
  ans = max(ans, cnt);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> n >> m >> g >> r;

  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++) {
      cin >> board[i][j];
      if (board[i][j] == 2) pos.push_back({i, j});
    }

  vector<int> pg, pr;

  for (int i = 0; i < pos.size(); i++) {
    if (i < pos.size() - g) pg.push_back(0);
    if (i >= pos.size() - g) pg.push_back(1);
  }

  for (int i = 0; i < pos.size() - g; i++) {
    if (i < pos.size() - (g + r)) pr.push_back(0);
    if (i >= pos.size() - (g + r)) pr.push_back(1);
  }

  do {
    vector<pair<int, int>> gv;
    for (int i = 0; i < pos.size(); i++)
      if (pg[i] == 1) gv.push_back(pos[i]);

    do {
      vector<pair<int, int>> rv;

      for (int i = 0; i < pr.size(); i++) {
        if (pr[i] != 1) continue;
        int zero_th = 0;

        for (int j = 0; j < pg.size(); j++) {
          if (pg[j] == 0) {
            zero_th++;
            if (zero_th == i + 1) {
              rv.push_back(pos[j]);
            }
          }
        }
      }
      bfs(gv, rv);
    } while (next_permutation(pr.begin(), pr.end()));
  } while (next_permutation(pg.begin(), pg.end()));

  cout << ans;
}