// task2.c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
 pid_t pid_child, pid_grand;

 pid_child = fork();
 if (pid_child < 0)
 {
  perror("fork");
  exit(EXIT_FAILURE);
 }

 if (pid_child == 0)
 {
  // In child
  pid_grand = fork();
  if (pid_grand < 0)
  {
   perror("fork");
   exit(EXIT_FAILURE);
  }

  if (pid_grand == 0)
  {
   // In grandchild
   printf("I am grandchild\n");
   exit(EXIT_SUCCESS);
  }
  else
  {
   // Back in child: wait for grandchild, then print
   wait(NULL);
   printf("I am child\n");
   exit(EXIT_SUCCESS);
  }
 }
 else
 {
  // In parent: wait for child (which itself waited for grandchild)
  wait(NULL);
  printf("I am parent\n");
 }

 return 0;
}
