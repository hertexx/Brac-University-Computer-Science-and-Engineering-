#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 3
#define MAX_RESOURCES 3
#define MAX_NAME_LEN 20

typedef enum
{
 READ = 1,  
 WRITE = 2,  
 EXECUTE = 4 
} Permission;


typedef struct
{
 char name[MAX_NAME_LEN];
} User;

typedef struct
{
 char name[MAX_NAME_LEN];
} Resource;


typedef struct
{
 char username[MAX_NAME_LEN];
 int permissions; 
} ACLEntry;

typedef struct
{
 Resource resource;
 ACLEntry entries[MAX_USERS];
 int count;
} ACLControlledResource;


typedef struct
{
 char resourceName[MAX_NAME_LEN];
 int permissions;
} Capability;

typedef struct
{
 User user;
 Capability caps[MAX_RESOURCES];
 int count;
} CapabilityUser;

void printPermissions(int perm)
{
 int first = 1;
 if (perm & READ)
 {
  printf("%sRead", first ? "" : "|");
  first = 0;
 }
 if (perm & WRITE)
 {
  printf("%sWrite", first ? "" : "|");
  first = 0;
 }
 if (perm & EXECUTE)
 {
  printf("%sExecute", first ? "" : "|");
  first = 0;
 }
 if (first)
  printf("None");
}

int hasPermission(int userPerm, int requiredPerm)
{
 return (userPerm & requiredPerm) == requiredPerm;
}

void checkACLAccess(ACLControlledResource *res, const char *userName, int perm)
{
 for (int i = 0; i < res->count; i++)
 {
  if (strcmp(res->entries[i].username, userName) == 0)
  {
   printf("ACL Check: User %s requests ", userName);
   printPermissions(perm);
   printf(" on %s: ", res->resource.name);
   if (hasPermission(res->entries[i].permissions, perm))
   {
    printf("Access GRANTED\n");
   }
   else
   {
    printf("Access DENIED\n");
   }
   return;
  }
 }
 printf("ACL Check: User %s has NO entry for %s: Access DENIED\n", userName, res->resource.name);
}

void checkCapabilityAccess(CapabilityUser *user, const char *resourceName, int perm)
{
 for (int i = 0; i < user->count; i++)
 {
  if (strcmp(user->caps[i].resourceName, resourceName) == 0)
  {
   printf("Capability Check: User %s requests ", user->user.name);
   printPermissions(perm);
   printf(" on %s: ", resourceName);
   if (hasPermission(user->caps[i].permissions, perm))
   {
    printf("Access GRANTED\n");
   }
   else
   {
    printf("Access DENIED\n");
   }
   return;
  }
 }
 printf("Capability Check: User %s has NO capability for %s: Access DENIED\n",
        user->user.name, resourceName);
}


int main()
{

 User users[MAX_USERS] = {{"Alice"}, {"Bob"}, {"Charlie"}};
 Resource resources[MAX_RESOURCES] = {{"File1"}, {"File2"}, {"File3"}};

 ACLControlledResource aclRes[MAX_RESOURCES];
 for (int i = 0; i < MAX_RESOURCES; i++)
 {
  aclRes[i].resource = resources[i];
  aclRes[i].count = 0;
 }

 strcpy(aclRes[0].entries[0].username, "Alice");
 aclRes[0].entries[0].permissions = READ | WRITE;
 strcpy(aclRes[0].entries[1].username, "Bob");
 aclRes[0].entries[1].permissions = READ;
 aclRes[0].count = 2;


 strcpy(aclRes[1].entries[0].username, "Alice");
 aclRes[1].entries[0].permissions = EXECUTE;
 strcpy(aclRes[1].entries[1].username, "Charlie");
 aclRes[1].entries[1].permissions = READ | EXECUTE;
 aclRes[1].count = 2;

 strcpy(aclRes[2].entries[0].username, "Bob");
 aclRes[2].entries[0].permissions = WRITE;
 aclRes[2].count = 1;


 CapabilityUser capUsers[MAX_USERS];
 for (int i = 0; i < MAX_USERS; i++)
 {
  capUsers[i].user = users[i];
  capUsers[i].count = 0;
 }


 strcpy(capUsers[0].caps[0].resourceName, "File1");
 capUsers[0].caps[0].permissions = READ | WRITE;
 strcpy(capUsers[0].caps[1].resourceName, "File2");
 capUsers[0].caps[1].permissions = EXECUTE;
 capUsers[0].count = 2;


 strcpy(capUsers[1].caps[0].resourceName, "File1");
 capUsers[1].caps[0].permissions = READ;
 strcpy(capUsers[1].caps[1].resourceName, "File3");
 capUsers[1].caps[1].permissions = WRITE;
 capUsers[1].count = 2;

 strcpy(capUsers[2].caps[0].resourceName, "File2");
 capUsers[2].caps[0].permissions = READ | EXECUTE;
 capUsers[2].count = 1;


 checkACLAccess(&aclRes[0], "Alice", READ);      
 checkACLAccess(&aclRes[0], "Bob", WRITE);       
 checkACLAccess(&aclRes[0], "Charlie", READ);    
 checkACLAccess(&aclRes[1], "Charlie", EXECUTE); 


 checkCapabilityAccess(&capUsers[0], "File1", WRITE);   
 checkCapabilityAccess(&capUsers[1], "File1", WRITE);   
 checkCapabilityAccess(&capUsers[2], "File2", EXECUTE); 
 checkCapabilityAccess(&capUsers[2], "File3", READ);    

 return 0;
}
