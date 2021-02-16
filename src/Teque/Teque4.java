import java.io.*;
import java.util.*;

public class Teque4 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine()); // number of queries

        // Create 2 hashmaps, it will store the two halves of the teque
        Map<Integer,Integer> tequeLeft = new HashMap<Integer,Integer>();
        Map<Integer,Integer> tequeRight = new HashMap<Integer,Integer>();

        // Set pointers for each hashmap, used another variables to keep track of hashmap size for convenience
        int minLeft = 0, maxLeft = 1, minRight = -1, maxRight = 0, leftSize = 0, rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            String[] command = sc.readLine().split(" ");
            switch (command[0]) {
                case "get":
                    int idx = Integer.parseInt(command[1]);
                    if (idx >= leftSize) { // if index > size of left teque, traverse the right teque
                        writer.println(tequeRight.get(idx-leftSize+minRight+1));
                    } else { // otherwise, traverse the left teque
                        writer.println(tequeLeft.get(idx+minLeft+1));
                    }
                    break;
                case "push_front": // add element to the left teque and decrement the leftmost pointer
                    tequeLeft.put(minLeft,Integer.parseInt(command[1]));
                    leftSize++;
                    minLeft--;
                    break;
                case "push_back": // add element to the right teque and increment the rightmost pointer
                    tequeRight.put(maxRight,Integer.parseInt(command[1]));
                    rightSize++;
                    maxRight++;
                    break;
                case "push_middle": // add element to the left teque but increment the max left pointer instead
                    tequeLeft.put(maxLeft,Integer.parseInt(command[1]));
                    leftSize++;
                    maxLeft++;
                    break;
            }
            if (!command[0].equals("get")) { // for all push commands (front, back, middle)
                if (leftSize > rightSize+1) { // move from left to right since there are too many elements in the left teque
                    tequeRight.put(minRight,tequeLeft.remove(maxLeft-1));
                    leftSize--;
                    rightSize++;
                    minRight--;
                    if (leftSize == 0) { // special case, the updated pointer is different
                        minLeft++;
                    } else {
                        maxLeft--;
                    }
                } else if (rightSize >= leftSize+1) { // move from right to left since there are too many elements in the right teque
                    tequeLeft.put(maxLeft,tequeRight.remove(minRight+1));
                    leftSize++;
                    rightSize--;
                    maxLeft++;
                    if (rightSize == 0) { // special case, the updated pointer is different
                        maxRight--;
                    } else {
                        minRight++;
                    }
                }
            }
        }
        writer.flush();
    }
}