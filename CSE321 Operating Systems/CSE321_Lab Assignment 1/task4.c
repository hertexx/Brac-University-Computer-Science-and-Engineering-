// task4.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

#define N 6

int cmp_desc(const void *a, const void *b)
{
 return (*(int *)b) - (*(int *)a);
}

int main()
{
 int arr[N] = {5, 2, 9, 1, 7, 4};
 int pipefd[2];

 if (pipe(pipefd) == -1)
 {
  perror("pipe");
  exit(EXIT_FAILURE);
 }

 pid_t pid = fork();
 if (pid < 0)
 {
  perror("fork");
  exit(EXIT_FAILURE);
 }

 if (pid == 0)
 {
  // Child: sort and write to pipe
  close(pipefd[0]);
  qsort(arr, N, sizeof *arr, cmp_desc);
  write(pipefd[1], arr, N * sizeof *arr);
  close(pipefd[1]);
  exit(EXIT_SUCCESS);
 }
 else
 {
  // Parent: read sorted data and print odd/even
  close(pipefd[1]);
  wait(NULL);
  int sorted[N];
  read(pipefd[0], sorted, N * sizeof *sorted);
  close(pipefd[0]);

  printf("Odd/Even status of sorted array:\n");
  for (int i = 0; i < N; i++)
  {
   printf("%d is %s\n", sorted[i],
          (sorted[i] % 2 == 0) ? "even" : "odd");
  }
 }

 return 0;
}
