// oddeven.c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
 if (argc < 2)
 {
  fprintf(stderr, "Usage: %s num1 num2 ...\n", argv[0]);
  return 1;
 }
 for (int i = 1; i < argc; i++)
 {
  int x = atoi(argv[i]);
  printf("%d is %s\n", x, (x % 2 == 0) ? "even" : "odd");
 }
 return 0;
}
