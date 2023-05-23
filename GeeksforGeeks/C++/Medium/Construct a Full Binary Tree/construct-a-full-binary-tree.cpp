//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
	
	Node(int x){
	    data = x;
	    left = NULL;
	    right = NULL;
	}
};


// } Driver Code Ends
/* Structre of the Node of the Binary Tree is as follows
struct Node
{
        int data;
        struct Node *left, *right;
};
*/
// your task is to complete this function
// function should create a new binary tree
// function should return the root node to the 
// new binary tree formed
class Solution{
    int N;
  public:
    Node* constructBinaryTree(int pre[], int preMirror[], int size)
    {
        // Code here
        N = size;
        int i = 0;
        return build(pre, preMirror, i);
    }
    
    Node *build(int pre[], int preMirror[], int &i){
        if(i == N)
            return nullptr;
        Node *root = new Node(pre[i]);
        int pos;
        for(int j=0; j<N; j++){
            if(pre[i] == preMirror[j]){
                preMirror[j] = -1;
                pos = j;
            }
        }
        i++;
        for(int j=pos+1; j<N; j++)
            if(preMirror[j] != -1){
                root->left  = build(pre, preMirror, i);
                root->right = build(pre, preMirror, i);
                break;
            }
        
        return root;
    }
};

//{ Driver Code Starts.

void printInorder(Node* node)
{
	if (node == NULL)return;
	printInorder(node->left);
	cout<<node->data<<" ";
	printInorder(node->right);
}

// Driver program to test above functions
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int preOrder[n];
	    int preOrderMirror[n];
	    for(int i=0; i<n; i++)cin>>preOrder[i];
	    for(int i=0; i<n; i++)cin>>preOrderMirror[i];
	    Solution obj;
	    printInorder(obj.constructBinaryTree(preOrder, preOrderMirror, n));
	    cout<<endl;
    }
	return 0;
}
// } Driver Code Ends