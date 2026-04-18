#include <iostream>
#include <string>
using namespace std;
int main() {
  int alpha[26] = {};
  string str;
  cin >> str;
  for (char c : str) alpha[c - 'a']++;
  for (int value : alpha) cout << value << ' ';
}