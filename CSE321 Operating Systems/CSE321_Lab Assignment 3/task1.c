#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include <sys/wait.h>

struct shared
{
 char sel[100];
 int b;
};

int main()
{
 int shmid;
 key_t key = 1234; // shared memory key
 struct shared *shm;
 int fd[2]; // pipe
 pid_t pid;

 // create shared memory
 shmid = shmget(key, sizeof(struct shared), 0666 | IPC_CREAT);
 if (shmid < 0)
 {
  perror("shmget");
  exit(1);
 }

 shm = (struct shared *)shmat(shmid, NULL, 0);
 if (shm == (void *)-1)
 {
  perror("shmat");
  exit(1);
 }

 // create pipe
 if (pipe(fd) == -1)
 {
  perror("pipe");
  exit(1);
 }

 printf("Provide Your Input From Given Options:\n");
 printf("1. Type a to Add Money\n");
 printf("2. Type w to Withdraw Money\n");
 printf("3. Type c to Check Balance\n");

 char input[100];
 scanf("%s", input);
 strcpy(shm->sel, input);
 shm->b = 1000;

 printf("Your selection: %s\n\n", shm->sel);

 pid = fork();

 if (pid < 0)
 {
  perror("fork");
  exit(1);
 }
 else if (pid == 0)
 {
  // Child process (opr)
  if (strcmp(shm->sel, "a") == 0)
  {
   int amt;
   printf("Enter amount to be added:\n");
   scanf("%d", &amt);
   if (amt > 0)
   {
    shm->b += amt;
    printf("Balance added successfully\n");
    printf("Updated balance after addition:\n%d\n", shm->b);
   }
   else
   {
    printf("Adding failed, Invalid amount\n");
   }
  }
  else if (strcmp(shm->sel, "w") == 0)
  {
   int amt;
   printf("Enter amount to be withdrawn:\n");
   scanf("%d", &amt);
   if (amt > 0 && amt <= shm->b)
   {
    shm->b -= amt;
    printf("Balance withdrawn successfully\n");
    printf("Updated balance after withdrawal:\n%d\n", shm->b);
   }
   else
   {
    printf("Withdrawal failed, Invalid amount\n");
   }
  }
  else if (strcmp(shm->sel, "c") == 0)
  {
   printf("Your current balance is:\n%d\n", shm->b);
  }
  else
  {
   printf("Invalid selection\n");
  }

  // write thank you to pipe
  char msg[] = "Thank you for using\n";
  write(fd[1], msg, strlen(msg));
  close(fd[1]);

  shmdt(shm);
  exit(0);
 }
 else
 {
  // Parent process (home)
  wait(NULL);

  char buffer[100];
  int n = read(fd[0], buffer, sizeof(buffer) - 1);
  if (n > 0)
  {
   buffer[n] = '\0';
   printf("%s", buffer);
  }
  close(fd[0]);

  // detach and remove shared memory
  shmdt(shm);
  shmctl(shmid, IPC_RMID, NULL);
 }

 return 0;
}
