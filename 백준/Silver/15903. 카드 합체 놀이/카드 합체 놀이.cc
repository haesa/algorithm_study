#include <iostream>
#include <queue>

using namespace std;

priority_queue<long long, vector<long long>, greater<long long>> pq;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, m; cin >> n >> m;
	for (int i = 0; i < n; i++) {
		long long temp; cin >> temp; pq.push(temp);
	}
	for (int i = 0; i < m; i++) {
		long long temp1 = pq.top(); pq.pop();
		long long temp2 = pq.top(); pq.pop();
		pq.push(temp1 + temp2);
		pq.push(temp1 + temp2);
	}

	long long sum = 0;
	while (!pq.empty()) {
		sum += pq.top(); pq.pop();
	}
	cout << sum;

	return 0;
}