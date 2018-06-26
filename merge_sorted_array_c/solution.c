// 8. Об’єднати два упорядкованих за зростанням масиви F(9) та К(9) в 
// один масив С(18), також упорядкований за зростанням. 
// Вивести на екран всі масиви.
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void merge(int *a, size_t a_size, int *b, unsigned b_size)

{
    unsigned summa = a_size + b_size;
    int *output = calloc(sizeof(a[0]), summa);
    if (output == NULL) {
        return;
    }
    int i = 0;
    int j = 0;
    int k = 0;
 
    while (i < a_size && j < b_size) 
    {
        if (a[i] < b[j]) 
        {
            output[k++] = a[i++];
        }

        else 
        {
            output[k++] = b[j++];
        }
    }

    if (i >= a_size) 
    {
        while (j < b_size) 
        {
            output[k++] = b[j++];
        }
    }

    if (j >= b_size) 
    {
        while (i < a_size)
        {
            output[k++] = a[i++];
        }
    }
    printf("\n Pershii masuv: \n");
    for (i = 0; i < a_size; ++i)
    {
        printf("\n%d", a[i]);
        }
    
    printf("\n Drugii masuv: \n");
    for (i = 0; i < b_size; i++)
    {
        printf("\n%d", b[i]);
        }
    
    printf("\n Tretii masuv: \n");
    for (i = 0; i < summa; ++i)
    {
        printf("\n%d", output[i]);

        }
}

void main()
{
    int a[]={7, 15, 20};
    int b[] = {8, 12, 19, 32};
    merge(a, 3, b, 4);
}