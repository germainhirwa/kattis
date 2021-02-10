// Uses ArrayDeque, still TLE :-(

import java.io.*;
import java.util.*;

public class Teque3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        Deque<Integer> tequeLeft = new ArrayDeque<>();
        Deque<Integer> tequeRight = new ArrayDeque<>();
        
        for (int i = 0; i < n; i++) {
            String[] command = sc.readLine().split(" ");
            switch (command[0]) {
                case "get":
                    if (Integer.parseInt(command[1]) < tequeLeft.size()) {
                        Deque<Integer> temp = new ArrayDeque<>();
                        for (int j = 0; j < Integer.parseInt(command[1]); j++) {
                            int moved = tequeLeft.removeFirst();
                            temp.addLast(moved);
                        }
                        writer.println(tequeLeft.peek());
                        for (int k = 0; k < Integer.parseInt(command[1]); k++) {
                            int moved = temp.removeLast();
                            tequeLeft.addFirst(moved);
                        }
                    } else {
                        Deque<Integer> temp = new ArrayDeque<>();
                        for (int j = 0; j < Integer.parseInt(command[1])-tequeLeft.size(); j++) {
                            int moved = tequeRight.removeFirst();
                            temp.addLast(moved);
                        }
                        writer.println(tequeRight.peek());
                        for (int k = 0; k < Integer.parseInt(command[1])-tequeLeft.size(); k++) {
                            int moved = temp.removeLast();
                            tequeRight.addFirst(moved);
                        }
                    }
                    break;
                case "push_front":
                    tequeLeft.addFirst(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
                case "push_back":
                    tequeRight.addLast(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
                case "push_middle":
                    tequeLeft.addLast(Integer.parseInt(command[1]));
                    balance(tequeLeft,tequeRight);
                    break;
            }
        }
        writer.flush();
    }

    public static void balance(Deque<Integer> tq1, Deque<Integer> tq2) {
        while (tq2.size() != (tq1.size()+tq2.size())/2) {
            if (tq1.size() > tq2.size()) {
                int moved = tq1.removeLast();
                tq2.addFirst(moved);
            } else {
                int moved = tq2.removeFirst();
                tq1.addLast(moved);
            }
        }
    }
}