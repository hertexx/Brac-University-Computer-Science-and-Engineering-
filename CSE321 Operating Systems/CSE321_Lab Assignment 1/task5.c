// task5.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
 pid_t pid_child, pid_gc;
 int i;

 printf("1. Parent process ID: %d\n", getpid());

 pid_child = fork();
 if (pid_child < 0)
 {
  perror("fork child");
  exit(EXIT_FAILURE);
 }

 if (pid_child == 0)
 {
  // In child
  printf("2. Child process ID: %d\n", getpid());
  // Create three grandchildren
  for (i = 0; i < 3; i++)
  {
   pid_gc = fork();
   if (pid_gc < 0)
   {
    perror("fork grandchild");
    exit(EXIT_FAILURE);
   }
   if (pid_gc == 0)
   {
    // In grandchild
    printf("3.%d Grandchild process ID: %d\n", i + 1, getpid());
    exit(EXIT_SUCCESS);
   }
   // Parent(child) continues loop to spawn next grandchild
  }
  // Wait for grandchildren
  for (i = 0; i < 3; i++)
  {
   wait(NULL);
  }
  exit(EXIT_SUCCESS);
 }
 else
 {
  // In original parent, wait for child
  wait(NULL);
 }

 return 0;
}
