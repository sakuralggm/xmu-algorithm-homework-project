// test2.cpp 归并排序的非递归实现
// 非递归写法二
#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using pii = pair<int, int>;
const int N = 1e5 + 10;
int a[N], t[N];

void merge(int l, int r)
{
    if (l >= r) return;
    int mid = l + r >> 1;
    int i = l, j = mid + 1, k = 0;
    int len = r - l + 1;
    if (log2(len) != floor(log2(len))) 
        mid = l - 1 + pow(2, floor(log2(len))), j = mid + 1;

    while (i <= mid && j <= r)
    {
        if (a[i] <= a[j]) t[k ++ ] = a[i ++ ];
        else t[k ++ ] = a[j ++ ];
    }
    while (i <= mid) t[k ++ ] = a[i ++ ];
    while (j <= r) t[k ++ ] = a[j ++ ];
    for (int i = l, j = 0; i <= r; i ++ , j ++ ) a[i] = t[j];
}

int main()
{
    ios::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);

    int n;
    cin >> n;
    for (int i = 1; i <= n; i ++ ) cin >> a[i];
    for (int s = 1; ; s *= 2)
    {
        for (int i = 1; i <= n; i += s)
        {
            if (i + s - 1 > n) 
            {
                merge(i, n);
                break;
            }
            else merge(i, i + s - 1);
        }
        if (s > n) break;
    }
    for (int i = 1; i <= n; i ++ ) cout << a[i] << ' ';
    return 0;
}