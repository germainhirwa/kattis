// Using TLL but still TLE, due to O(n) get

import java.io.*;
import java.util.*;

public class Teque2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        TailedLinkedList tequeLeft = new TailedLinkedList();
        TailedLinkedList tequeRight = new TailedLinkedList();
        
        for (int i = 0; i < n; i++) {
            String[] command = sc.readLine().split(" ");
            switch (command[0]) {
                case "get":
                    if (Integer.parseInt(command[1]) < tequeLeft.size()) {
                        writer.println(tequeLeft.getItemAtIndex(Integer.parseInt(command[1])));
                    } else {
                        writer.println(tequeRight.getItemAtIndex(Integer.parseInt(command[1])-tequeLeft.size()));
                    }
                    break;
                case "push_front":
                    tequeLeft.addFront(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
                case "push_back":
                    tequeRight.addBack(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
                case "push_middle":
                    tequeLeft.addBack(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
            }
        }
        writer.flush();
    }

    public static void balance(TailedLinkedList tq1, TailedLinkedList tq2) {
        while (tq2.size() != (tq1.size()+tq2.size())/2) {
            if (tq1.size() > tq2.size()) {
                int moved = tq1.removeBack();
                tq2.addFront(moved);
            } else {
                int moved = tq2.removeFront();
                tq1.addBack(moved);
            }
        }
    }
}

class ListNode {
    public int item;
    public ListNode next;

    public ListNode(int val) { this(val, null); }

    public ListNode(int val, ListNode n) { 
        item = val; 
        next = n; 
    }

    public ListNode getNext() { return next; }
    public int getItem() { return item; }
    public void setItem(int val) { item = val; }
    public void setNext(ListNode n) { next = n; }
}

class TailedLinkedList {
    public ListNode head;
    public ListNode tail;
    public int num_nodes;

    public boolean isEmpty() { return (num_nodes == 0); }
    public int size() { return num_nodes; }

    public int getItemAtIndex(int index) { // for the get function of the teque
        int counter = 0;
        int item = 0;

        if (index == size()-1)
            item = tail.getItem();
        else {
            for (ListNode cur = head; cur != null; cur = cur.getNext(), counter++) {
                if (counter == index) {
                    item = cur.getItem();
                    break;
                }
            }
        }
        return item;
    }

    public int getFirst() { return getItemAtIndex(0); }
    public int getLast() { return getItemAtIndex(size()-1); }

    public void addFront(int item) {
        ListNode newNode = new ListNode(item);
        insert(null,newNode); 
    }
    public void addBack(int item) {
        ListNode newNode = new ListNode(item);
        insert(tail,newNode); 
    }

    public int removeAtIndex(int index) {
        ListNode cur;
        int item = 0;

        if (index >= 0 && index < size()) {
            if (index == 0)
                item = remove(null);
            else {
                cur = getNodeAtIndex(index-1);
                item = remove(cur);
            }
        }
        return item;
    }

    public int removeFront() { return remove(null); }
    public int removeBack() { return removeAtIndex(size()-1); }

    public ListNode getNodeAtIndex(int index) {
        int counter = 0;
        ListNode node = null;

        if (index == size()-1)
            return tail;
        for (ListNode cur = head; cur != null; cur = cur.getNext()) {
            if (counter == index) {
                node = cur;
                break;
            }
            counter++;
        }
        return node;
    }

    public void insert(ListNode cur, ListNode n) {
        if (cur == null) {
            n.setNext(head);
            head = n;
            if (tail == null)
                tail = head;
        }
        else {
            n.setNext(cur.getNext());
            cur.setNext(n);
            if (cur == tail)
                tail = tail.getNext();
        }
        num_nodes++;
    }

    public int remove(ListNode cur) {
        int value;

        if (cur == null) {
            value = head.getItem();
            head = head.getNext();
            if (num_nodes == 1)
                tail = null;
        }
        else {
            value = cur.getNext().getItem();
            cur.setNext(cur.getNext().getNext());
            if (cur.getNext() == null)
                tail = cur;
        }
        num_nodes--;

        return value;
    }
}