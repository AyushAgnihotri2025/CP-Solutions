//{ Driver Code Starts
// C program to find n'th Node in linked list
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace std;

/* Link list Node */
struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};

void append(struct Node** head_ref, struct Node **tail_ref,
            int new_data)
{
    struct Node* new_node = new Node(new_data);
    
    if (*head_ref == NULL)
        *head_ref = new_node;
    else
        (*tail_ref)->next = new_node;
    *tail_ref = new_node;
}

/* Function to get the middle of the linked list*/
int maxPalindrome(Node *);


/* Driver program to test above function*/
int main()
{
    int T,n,l;
    cin>>T;

    while(T--)
    {
        struct Node *head = NULL,  *tail = NULL;

        cin>>n;
        for (int i=1; i<=n; i++)
        {
            cin>>l;
            append(&head, &tail, l);
        }
      

       cout << maxPalindrome(head)<<endl;
    }
    return 0;
}



// } Driver Code Ends


/* The Node is defined 
  /* Link list Node
struct Node
{
    int data;
    struct Node* next;
    
    Node(int x){
        data = x;
        next = NULL;
    }
    
};
*/

/*The function below returns an int denoting
the length of the longest palindrome list. */
int maxPalindrome(Node *head)
{
    //Your code here
    int n=1;
    Node* temp=head;
    while(temp) {n++; temp=temp->next;}
    int s[n]={0};
    int i=0;
    while(head){ s[i++]=head->data; head=head->next;}
    int maxlen=0;
    int low,high;
    for(int i=1;i<n;i++){
        low=i-1;high=i;
        while(low>=0 && high<n && s[low]==s[high]){low--; high++;}
        low++; high--;
        if(high-low+1>maxlen && s[high]==s[low]) maxlen=high-low+1;
        
        low=i-1; high=i+1;
        while(low>=0 && high<n && s[low]==s[high]){low--; high++;}
        low++; high--;
        if(high-low+1>maxlen) maxlen=high-low+1;
    }
    return maxlen;
}