#include <iostream>
using namespace std;
#define INT_MAX 9999999

int n = 4;
int dist[10][10] = {
    {0, 20, 42, 25},
    {20, 0, 30, 34},
    {42, 30, 0, 10},
    {25, 34, 10, 0}
};
int VISITED_ALL = (1 << n) - 1;
int dp[16][4]; // Adjust size as per your requirement

int tsp(int mask, int post) {
    if (mask == VISITED_ALL) {
        return dist[post][0];
    }
    int ans = INT_MAX;
    for (int city = 0; city < n; city++) {
        if ((mask & (1 << city)) == 0) {
            int newans = dist[post][city] + tsp(mask | (1 << city), city);
            ans = min(ans, newans);
        }
    }
    return dp[mask][post] = ans;
}

int main() {
    for (int i = 0; i < (1 << n); i++) {
        for (int j = 0; j < n; j++) {
            dp[i][j] = -1;
        }
    }
    cout << tsp(1, 0) << endl;
    return 0;
}
