/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head==null || head.next==null)
            return head;
        ListNode ptr1 = head;
        ListNode ptr2 = head.next;
        ListNode prev = ptr2;
        
        while(ptr2!=null && ptr2.next!=null){
            ptr1.next = ptr2.next;
            ptr1 = ptr1.next;
            ptr2.next = ptr1.next;
            ptr2 = ptr2.next;
        }
        ptr1.next = prev;
        return head;
    }
}