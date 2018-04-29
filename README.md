# Yet another register optimization

In the previous for loop of the matrix multiplication, C was being accessed multiple times and C is stored in the memory. This is **bad** because there will be a memory overhead in every iteration. So, the trick to eliminate this problem is to store C in a register and use that register to do the calculation. Later, we put the value back from the register into the memory. Following is the change:

Before:
```c
for (i = 0; i < m; i++) {
  for (j = 0; j < n; j++) {
    for (l = 0; l < k; l++) {
      C[i][j] += A[i][l] * T[j][l];
    }
  }
}
```

After:
```c
for (i = 0; i < m; i++){
  for (j = 0; j < n; j++) {
    register double r = C[i][j];
    for (l = 0; l < k; l++) {
      r += A[i][l] * T[j][l];
    }
    C[i][j] = r;
  }
}
```