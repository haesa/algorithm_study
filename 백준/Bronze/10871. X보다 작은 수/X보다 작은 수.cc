#include <iostream>
using namespace std;
int main()
{
  int n, x, item;
  cin >> n >> x;
  for (int i = 0; i < n; i++)
  {
    cin >> item;
    if(item < x) cout << item << ' ';
  }
}