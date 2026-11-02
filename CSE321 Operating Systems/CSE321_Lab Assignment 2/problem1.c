#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

// Global variables to share between threads
int *fib_sequence = NULL;   // Will hold Fibonacci sequence
int n;                      // Number of terms
int *search_indices = NULL; // Indices to search
int s;                      // Number of searches

// Thread 1: Generate Fibonacci sequence
void *generate_fibonacci(void *arg)
{
 fib_sequence = (int *)malloc((n + 1) * sizeof(int));
 if (!fib_sequence)
 {
  perror("Memory allocation failed");
  pthread_exit(NULL);
 }

 // Generate Fibonacci sequence
 for (int i = 0; i <= n; i++)
 {
  if (i == 0)
   fib_sequence[i] = 0;
  else if (i == 1)
   fib_sequence[i] = 1;
  else
   fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2];
 }

 pthread_exit(NULL);
}

// Thread 2: Search for Fibonacci values
void *search_fibonacci(void *arg)
{
 for (int i = 0; i < s; i++)
 {
  int idx = search_indices[i];
  if (idx >= 0 && idx <= n)
  {
   printf("result of search #%d = %d\n", i + 1, fib_sequence[idx]);
  }
  else
  {
   printf("result of search #%d = -1\n", i + 1);
  }
 }
 pthread_exit(NULL);
}

int main()
{
 pthread_t tid1, tid2;

 // Input Fibonacci sequence length
 printf("Enter the term of fibonacci sequence:\n");
 scanf("%d", &n);
 if (n < 0 || n > 40)
 {
  printf("Invalid input! n must be between 0 and 40.\n");
  return 1;
 }

 // Create thread for Fibonacci generation
 pthread_create(&tid1, NULL, generate_fibonacci, NULL);
 pthread_join(tid1, NULL);

 // Print Fibonacci sequence
 for (int i = 0; i <= n; i++)
 {
  printf("a[%d] = %d\n", i, fib_sequence[i]);
 }

 // Input number of searches
 printf("How many numbers you are willing to search?:\n");
 scanf("%d", &s);
 if (s <= 0)
 {
  printf("Invalid input! Number of searches must be > 0.\n");
  free(fib_sequence);
  return 1;
 }

 // Allocate memory for search indices
 search_indices = (int *)malloc(s * sizeof(int));
 if (!search_indices)
 {
  perror("Memory allocation failed");
  free(fib_sequence);
  return 1;
 }

 // Input search queries
 for (int i = 0; i < s; i++)
 {
  printf("Enter search %d:\n", i + 1);
  scanf("%d", &search_indices[i]);
 }

 // Create thread for search
 pthread_create(&tid2, NULL, search_fibonacci, NULL);
 pthread_join(tid2, NULL);

 // Free allocated memory
 free(fib_sequence);
 free(search_indices);

 return 0;
}
