#include <algorithm>
#include <iostream>
using namespace std;
int check[2000001] = {};
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int n, x, result = 0;
  int a[100000];
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a[i];
    check[a[i]]++;
  }
  cin >> x;
  for (int i = 0; i < n; i++)
    if ((x > a[i]) && check[x - a[i]]) result++;
  cout << result / 2;
}