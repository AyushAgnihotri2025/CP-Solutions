/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
  if (head === null || head.next === null) {
    return head; // empty list or single node case
  }
  let prev = head;
  let curr = head.next;
  let newHead = curr;
  while (true) {
    let next = curr.next;
    curr.next = prev;
    if (next === null || next.next === null) {
      prev.next = next;
      break; // end of list case
    }
    prev.next = next.next;
    prev = next;
    curr = prev.next;
  }
  return newHead;    
};