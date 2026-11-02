#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_STUDENTS 10
#define NUM_CHAIRS 3

// Global variables
sem_t students;        // Counts waiting students
sem_t tutor;           // Tutor availability
pthread_mutex_t mutex; // Protects shared data

int waiting = 0;         // Students currently waiting
int served = 0;          // Students served
int queue[NUM_CHAIRS];   // Waiting queue
int front = 0, rear = 0; // Queue pointers

// Utility: add to queue
void enqueue(int student_id)
{
 queue[rear] = student_id;
 rear = (rear + 1) % NUM_CHAIRS;
}

// Utility: remove from queue
int dequeue()
{
 int id = queue[front];
 front = (front + 1) % NUM_CHAIRS;
 return id;
}

// Tutor thread
void *tutor_thread(void *arg)
{
 while (served < NUM_STUDENTS)
 {
  sem_wait(&students); // Wait for a student
  pthread_mutex_lock(&mutex);

  int student_id = dequeue();
  waiting--;

  printf("A waiting student started getting consultation\n");
  printf("Number of students now waiting: %d\n", waiting);

  pthread_mutex_unlock(&mutex);

  sem_post(&tutor); // Signal tutor is ready

  printf("ST giving consultation\n");
  printf("Student %d is getting consultation\n", student_id);

  sleep(1); // Simulate consultation time

  pthread_mutex_lock(&mutex);
  served++;
  printf("Student %d finished getting consultation and left\n", student_id);
  printf("Number of served students: %d\n", served);
  pthread_mutex_unlock(&mutex);
 }
 pthread_exit(NULL);
}

// Student thread
void *student_thread(void *arg)
{
 int id = *(int *)arg;
 sleep(rand() % 3); // Random arrival time

 pthread_mutex_lock(&mutex);
 if (waiting < NUM_CHAIRS)
 {
  // Student can wait
  enqueue(id);
  waiting++;
  printf("Student %d started waiting for consultation\n", id);

  pthread_mutex_unlock(&mutex);

  sem_post(&students); // Notify tutor
  sem_wait(&tutor);    // Wait for tutor
 }
 else
 {
  // No chairs, student leaves
  printf("No chairs remaining in lobby. Student %d Leaving.....\n", id);
  pthread_mutex_unlock(&mutex);

  // Simulate immediate leave
  pthread_mutex_lock(&mutex);
  served++;
  printf("Student %d finished getting consultation and left\n", id);
  printf("Number of served students: %d\n", served);
  pthread_mutex_unlock(&mutex);
 }

 pthread_exit(NULL);
}

int main()
{
 pthread_t st, students_threads[NUM_STUDENTS];
 int ids[NUM_STUDENTS];

 srand(time(NULL));

 sem_init(&students, 0, 0);
 sem_init(&tutor, 0, 0);
 pthread_mutex_init(&mutex, NULL);

 // Create tutor thread
 pthread_create(&st, NULL, tutor_thread, NULL);

 // Create student threads
 for (int i = 0; i < NUM_STUDENTS; i++)
 {
  ids[i] = i;
  pthread_create(&students_threads[i], NULL, student_thread, &ids[i]);
 }

 // Join all student threads
 for (int i = 0; i < NUM_STUDENTS; i++)
 {
  pthread_join(students_threads[i], NULL);
 }

 pthread_join(st, NULL);

 // Cleanup
 sem_destroy(&students);
 sem_destroy(&tutor);
 pthread_mutex_destroy(&mutex);

 return 0;
}
