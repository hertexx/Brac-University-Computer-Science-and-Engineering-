// task3.c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main()
{
 pid_t a, b, c;
 int total_forks = 0;

 a = fork();
 total_forks++;
 if (a < 0)
 {
  perror("fork a");
  exit(1);
 }

 b = fork();
 total_forks++;
 if (b < 0)
 {
  perror("fork b");
  exit(1);
 }

 c = fork();
 total_forks++;
 if (c < 0)
 {
  perror("fork c");
  exit(1);
 }

 // For each process, check the *latest* child PID (c).  If odd, fork again.
 if (c > 0 && (c % 2) == 1)
 {
  pid_t d = fork();
  total_forks++;
  if (d < 0)
  {
   perror("fork d");
   exit(1);
  }
 }

 // Wait for any children to finish
 while (wait(NULL) > 0)
 {
  ;
 }

 // Each process prints its count of forks it performed.
 // But to get the TOTAL number of distinct processes created:
 // total processes = total_forks + 1 (original)
 printf("Process PID %d: forks performed = %d; total processes = %d\n",
        getpid(), total_forks, total_forks + 1);

 return 0;
}
