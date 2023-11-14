#include <stdio.h>

void half_adder(int A, int B, int *sum, int *carry)
{
    *sum = A ^ B;
    *carry = A & B;
}

void full_adder(int A, int B, int Ci, int *sum, int *carry)
{
    int sum1, carry1, sum2, carry2;

    half_adder(A, B, &sum1, &carry1);
    half_adder(sum1, Ci, &sum2, &carry2);

    *sum = sum2;
    *carry = carry1 | carry2;
}

int main()
{
    int a, b, sum, carry = 0;

    printf("a = ");
    scanf("%d", &a);
    printf("b = ");
    scanf("%d", &b);

    full_adder(a, b, carry, &sum, &carry);

    printf("result = %d%d\n", carry, sum);

    return 0;
}