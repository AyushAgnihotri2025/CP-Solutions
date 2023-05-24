/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        ListNode*l1=head,*l2=head,*curr;
        if(head == NULL || head->next == NULL)return head;
        int n=0;
        while(l1!=NULL){
            l1=l1->next;
            n++;
        }
        if(n==k || k==0 || k%n == 0)return head;
        int val=n-k;
        if(k>n)val = n-k%n;
        for(int i=0;i<val-1;i++){
            l2=l2->next;
        }
        if(l2->next!=NULL)curr=l2->next;
        l2->next = NULL;
        ListNode *newhead = curr;
        while(curr->next!=NULL)curr=curr->next;
        curr->next = head;
        return newhead;
    }
};