// test1.cpp，最长公共子序列算法的cpp实现
#include <bits/stdc++.h>
using namespace std;

// 这是一个测试
const int N = 1010;
char a[N], b[N];
int n, m, f[N][N];

int main()
{
    cin >> n >> m;
    scanf("%s%s", a + 1, b + 1);

    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= m; j ++ )
        {
            f[i][j] = max(f[i - 1][j], f[i][j - 1]);
            if (a[i] == b[j]) f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1);
        }

    cout << f[n][m];
    return 0;
}