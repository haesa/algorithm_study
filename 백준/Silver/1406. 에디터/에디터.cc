#include <iostream>
#include <list>
#include <string>
using namespace std;
list<char> l;
list<char>::iterator t;
string s;
string cmd;
int n;
int main() {
  cin >> s;
  for (char c : s) l.push_back(c);
  t = l.end();
  cin >> n;
  cin.ignore();

  for (int i = 0; i < n; i++) {
    getline(cin, cmd);
    for (int j = 0; j < cmd.length(); j++) {
      switch (cmd[j]) {
        case 'L':
          if (t != l.begin()) t--;
          break;
        case 'D':
          if (t != l.end()) t++;
          break;
        case 'B':
          if (t == l.begin()) continue;
          if (t == l.end()) {
            t = l.erase(--t);
            t = l.end();
          } else
            t = l.erase(--t);
          break;
        case 'P':
          while (cmd[++j] == ' ')
            ;
          l.insert(t, cmd[j]);
      }
    }
  }
  for (auto i : l) cout << i;
}