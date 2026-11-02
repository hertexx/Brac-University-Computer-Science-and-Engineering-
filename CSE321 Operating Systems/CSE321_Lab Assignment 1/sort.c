// sort.c
#include <stdio.h>
#include <stdlib.h>

int cmp_desc(const void *a, const void *b)
{
 return (*(int *)b) - (*(int *)a);
}

int main(int argc, char *argv[])
{
 if (argc < 2)
 {
  fprintf(stderr, "Usage: %s num1 num2 ...\n", argv[0]);
  return 1;
 }
 int n = argc - 1;
 int *arr = malloc(n * sizeof *arr);
 for (int i = 0; i < n; i++)
 {
  arr[i] = atoi(argv[i + 1]);
 }
 qsort(arr, n, sizeof *arr, cmp_desc);
 printf("Sorted (desc):");
 for (int i = 0; i < n; i++)
 {
  printf(" %d", arr[i]);
 }
 printf("\n");
 free(arr);
 return 0;
}
