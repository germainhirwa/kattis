// Using Reader class

import java.io.*;
import java.util.*;

public class Teque2 {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return ret;
        }

        public String readWord() throws IOException {
            byte[] buf = new byte[11]; // line length, maximum at push_middle
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n' || c == ' ') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = sc.nextInt(); // number of queries

        // Create 2 hashmaps, it will store the two halves of the teque
        Map<Integer,Integer> tequeLeft = new HashMap<Integer,Integer>();
        Map<Integer,Integer> tequeRight = new HashMap<Integer,Integer>();

        // Set pointers for each hashmap, used another variables to keep track of hashmap size for convenience
        int minLeft = 0, maxLeft = 1, minRight = -1, maxRight = 0, leftSize = 0, rightSize = 0;
        
        for (int i = 0; i < n; i++) {
            String command = sc.readWord();
            switch (command) {
                case "get":
                    int idx = sc.nextInt();
                    if (idx >= leftSize) { // if index > size of left teque, traverse the right teque
                        writer.println(tequeRight.get(idx-leftSize+minRight+1));
                    } else { // otherwise, traverse the left teque
                        writer.println(tequeLeft.get(idx+minLeft+1));
                    }
                    break;
                case "push_front": // add element to the left teque and decrement the leftmost pointer
                    tequeLeft.put(minLeft,sc.nextInt());
                    leftSize++;
                    minLeft--;
                    break;
                case "push_back": // add element to the right teque and increment the rightmost pointer
                    tequeRight.put(maxRight,sc.nextInt());
                    rightSize++;
                    maxRight++;
                    break;
                case "push_middle": // add element to the left teque but increment the max left pointer instead
                    tequeLeft.put(maxLeft,sc.nextInt());
                    leftSize++;
                    maxLeft++;
                    break;
            }
            if (!command.equals("get")) { // for all push commands (front, back, middle)
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