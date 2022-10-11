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
    public ListNode reverse(ListNode head){
        if(head==null || head.next==null)
            return head;
        ListNode curr = head;
        ListNode prev = null;
        
        while(curr!=null){
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
    public boolean isPalindrome(ListNode head) {
        if(head==null || head.next==null)
            return true;
        if(head.next.next==null){
            if(head.val==head.next.val)
                return true;
            return false;
        }
        ListNode slow = head;
        ListNode fast = head;
        
        while(fast.next!=null && fast.next.next!=null){
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = reverse(slow.next);
        slow = slow.next;
        ListNode dummy = head;
        
        while(slow!=null){
            if(dummy.val!=slow.val)
                return false;
            dummy = dummy.next;
            slow = slow.next;
        }
        return true;
    }
}