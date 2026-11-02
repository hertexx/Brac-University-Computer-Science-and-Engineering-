#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/wait.h>

struct msg
{
 long int type;
 char txt[6];
};

int main()
{
 key_t key = 1234;
 int msgid;
 struct msg message;

 // Create message queue
 msgid = msgget(key, 0666 | IPC_CREAT);
 if (msgid == -1)
 {
  perror("msgget");
  exit(1);
 }

 // Take workspace input
 char workspace[20];
 printf("Please enter the workspace name:\n");
 scanf("%s", workspace);

 if (strcmp(workspace, "cse321") != 0)
 {
  printf("Invalid workspace name\n");
  msgctl(msgid, IPC_RMID, NULL);
  exit(0);
 }

 // Send workspace name to OTP generator
 message.type = 1;
 strncpy(message.txt, workspace, sizeof(message.txt));
 msgsnd(msgid, &message, sizeof(message.txt), 0);
 printf("Workspace name sent to otp generator from log in: %s\n\n", message.txt);

 pid_t pid1 = fork();

 if (pid1 == 0)
 {
  // Child process → OTP generator

  // Receive workspace from log in
  msgrcv(msgid, &message, sizeof(message.txt), 1, 0);
  printf("OTP generator received workspace name from log in: %s\n\n", message.txt);

  // Generate OTP (PID of generator)
  pid_t otp = getpid();
  snprintf(message.txt, sizeof(message.txt), "%d", otp);

  // Send OTP to log in
  message.type = 2;
  msgsnd(msgid, &message, sizeof(message.txt), 0);
  printf("OTP sent to log in from OTP generator: %s\n", message.txt);

  // Send OTP to mail
  message.type = 3;
  msgsnd(msgid, &message, sizeof(message.txt), 0);
  printf("OTP sent to mail from OTP generator: %s\n", message.txt);

  pid_t pid2 = fork();

  if (pid2 == 0)
  {
   // Grandchild process → Mail

   // Receive OTP from generator
   msgrcv(msgid, &message, sizeof(message.txt), 3, 0);
   printf("Mail received OTP from OTP generator: %s\n", message.txt);

   // Send OTP to log in
   message.type = 4;
   msgsnd(msgid, &message, sizeof(message.txt), 0);
   printf("OTP sent to log in from mail: %s\n", message.txt);

   exit(0);
  }
  else
  {
   wait(NULL); // wait for mail
   exit(0);
  }
 }
 else
 {
  // Parent process (log in)
  wait(NULL); // wait for OTP generator + mail

  // Read OTP from OTP generator
  msgrcv(msgid, &message, sizeof(message.txt), 2, 0);
  char otp1[6];
  strncpy(otp1, message.txt, sizeof(otp1));
  printf("Log in received OTP from OTP generator: %s\n", otp1);

  // Read OTP from mail
  msgrcv(msgid, &message, sizeof(message.txt), 4, 0);
  char otp2[6];
  strncpy(otp2, message.txt, sizeof(otp2));
  printf("Log in received OTP from mail: %s\n", otp2);

  // Verify
  if (strcmp(otp1, otp2) == 0)
   printf("OTP Verified\n");
  else
   printf("OTP Incorrect\n");

  // Remove message queue
  msgctl(msgid, IPC_RMID, NULL);
 }

 return 0;
}
