// task1.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXLINE 1024

int main(int argc, char *argv[])
{
 int fd;
 ssize_t n;
 char buffer[MAXLINE];

 if (argc != 2)
 {
  fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
  exit(EXIT_FAILURE);
 }

 // Open for read/write, create if not exists, append mode, permissions rw-r--r--
 fd = open(argv[1], O_RDWR | O_CREAT | O_APPEND, 0644);
 if (fd == -1)
 {
  perror("open");
  exit(EXIT_FAILURE);
 }

 while (1)
 {
  printf("Enter a string (or -1 to quit): ");
  if (fgets(buffer, MAXLINE, stdin) == NULL)
  {
   perror("fgets");
   break;
  }
  // Remove trailing newline
  buffer[strcspn(buffer, "\n")] = '\0';
  if (strcmp(buffer, "-1") == 0)
  {
   break;
  }
  // Write the line plus newline
  strcat(buffer, "\n");
  n = write(fd, buffer, strlen(buffer));
  if (n == -1)
  {
   perror("write");
   break;
  }
 }

 close(fd);
 return 0;
}