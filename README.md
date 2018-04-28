# Register

This optimization might be the easiest optimization. In C, there's a keyword "register" which basically tells the compiler to use registers to store the data instead of the memory. Though, it's not guaranteed that by adding the keyword "register" that the compiler will always use registers; it's the compiler's responsibility to decide to use registers. "register" **only hints the compiler**.

By putting the data in the registers, we could gain some more performance because registers are **fast**. Registers are in the CPU. This means there's no overhead of going to BUS and access the memory.

Following is how to use the keyword, "register":

Original:
```c
int row = 0;
``` 

After:
```c
register int row = 0;
```

*more detailed info: please see the full report in the master branch*
