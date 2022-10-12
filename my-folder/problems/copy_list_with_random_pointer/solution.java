/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        Node curr = head;
        HashMap<Node,Node> map = new HashMap<>();
        //first pass to create a deep copy of the nodes
        while(curr!=null){
            map.put(curr,new Node(curr.val));
            curr = curr.next;
        }
        
        curr = head;
        //second pass to set the next and random pointers of the list
        while(curr!=null){
            map.get(curr).next = map.get(curr.next);
            map.get(curr).random = map.get(curr.random);
            curr = curr.next;
        }
        return map.get(head);
    }
}