# Cache Locality

This branch optimizes data accesses to maximize L1 cache utilization. Since C is a row major language, it's much faster if we access 2D arrays in row major order. For example, in the code below:
```c
for(int row = 0; row < N; row++)
    for(int col = 0; col < N; col++)
        ar[col][row] = 0;
```

The code above will access the array, ar, in col major. This is **BAD** because every time we access every element in the array, we will be maximizing cache misses. In our goal of optimizing, we want to minimize cache misses, therefore to improve upon this model, we should:
```c
for(int row = 0; row < N; row++)
    for(int col = 0; col < N; col++)
        ar[row][col] = 0;
```
*Notice that we swap row and col in accessing ar*

While this move, ar[col][row] -> ar[row][col], seems simple, it optimizes data accesses so that we minimize cache misses. We go from accessing in column major to accessing in row major.

In the original source code, the naive approach, we have:
```c
for (j = 0; j < n; j++)
  for (l = 0; l < k; l++)
    for (i = 0; i < m; i++)
      C[i][j] += A[i][l] * B[l][j];
```

Upon further analysis, we find that this naive approach was accessing memory in a non-sequential way (column major way) which caused much more trips to memory (cache misses) than were necessary. This problem occurs because the cache size is in blocks, most often size 64 bytes, which can store multiple array elements, but if we are accessing in column major, then the elements we are getting will not be in the proper order.

When we access data could be cached if it were accessed in a sequential way, to combat this, reordering the for loops was applied.

After the reordering:
```c
for (i = 0; i < m; i++)
  for (j = 0; j < n; j++)
    for (l = 0; l < k; l++)
      C[i][j] += A[i][l] * B[l][j];
```

To even utilize the L1 cache even more, we also transposed the second matrix, "B" and use the transposed matrix for the matrix multiplication. Here, matrix is still being accessed in column major and there is no other way to reorder the for loops such that the A, B, and C matrices will be accessed in row major.

After the transpose:
```c
// Transposed matrix
for (i = 0; i < n; i++)
  for (j = 0; j < k; j++)
    T[i][j] = B[j][i];

for (i = 0; i < m; i++)
  for (j = 0; j < n; j++)
    for (l = 0; l < k; l++)
      C[i][j] += A[i][l] * T[j][l];
```

Overall, we gained ~75% performance.

*more detailed info: please see the full report in the master branch*
