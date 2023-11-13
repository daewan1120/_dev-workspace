#include <stdio.h>

void half_adder(int A, int B, int *sum, int *carry)
{
    *sum = A ^ B;
    *carry = A & B;
}

int main()
{
    int a, b, sum, carry;

    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);

    half_adder(a, b, &sum, &carry);

    printf("sum = %d, carry = %d\n", sum, carry);

    return 0;
}
