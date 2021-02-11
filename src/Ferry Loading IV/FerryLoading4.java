import java.io.*;
import java.util.*;

public class FerryLoading4 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int cases = Integer.parseInt(sc.readLine());
        for (int i = 0; i < cases; i++) {
            String[] firstLine = sc.readLine().split(" ");
            int l = 100*Integer.parseInt(firstLine[0]);
            int m = Integer.parseInt(firstLine[1]);
            boolean isLeft = true;
            QueueArr left = new QueueArr(m);
            QueueArr right = new QueueArr(m);

            int tempLoad = 0;

            for (int j = 0; j < m; j++) {
                String[] line = sc.readLine().split(" ");
                int carLength = Integer.parseInt(line[0]);
                String pos = line[1];
                if (pos.equals("left")) {
                    left.offer(carLength);
                } else { // equals "right"
                    right.offer(carLength);
                }
            }

            int leftVisit = 0;
            int leftQueue = left.length;
            for (int lq = 0; lq < leftQueue; lq++) {
                if (tempLoad + left.peek() <= l) {
                    tempLoad += left.poll();
                } else {
                    tempLoad = left.poll();
                    leftVisit++;
                }
            }
            if (leftQueue > 0) {
                leftVisit++;
            }

            tempLoad = 0; // reassign to 0
            int rightVisit = 0;
            int rightQueue = right.length;
            for (int rq = 0; rq < rightQueue; rq++) {
                if (tempLoad + right.peek() <= l) {
                    tempLoad += right.poll();
                } else {
                    tempLoad = right.poll();
                    rightVisit++;
                }
            }
            if (rightQueue > 0) {
                rightVisit++;
            }

            if (leftVisit > rightVisit) {
                System.out.println(2*leftVisit-1);
            } else {
                System.out.println(2*rightVisit);
            }
        }

        writer.flush();
    }
}

class QueueArr {
    public int[] arr;
    public int front, back;
    public int capacity;
    public int length;

    public QueueArr(int size) {
        arr = new int[size+1];
        front = 0;
        back = 0;
        capacity = size+1;
    }

    public boolean empty() { 
        return (front == back); 
    }

    public Integer peek() {
        if (empty()) return null;
        else return arr[front];
    }

    public Integer poll() {
        if (empty()) return null;
        Integer item = arr[front];
        front = (front + 1) % capacity;
        length--;
        return item;
    }

    public void offer(Integer item) {
        arr[back] = item;
        back = (back + 1) % capacity;
        length++;
    }
}