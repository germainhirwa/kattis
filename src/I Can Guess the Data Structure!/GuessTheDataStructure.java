import java.io.*;
import java.util.*;

public class GuessTheDataStructure {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        while (true) {
            try {
                int n = Integer.parseInt(sc.readLine());
                int truth = 7;

                /*
                Represents the truth value
                0 for impossible
                1 for stack
                2 for queue
                4 for PQ
                Other than 0,1,2,4 is not sure
                */

                Deque<Integer> stack = new ArrayDeque<Integer>();
                Deque<Integer> queue = new ArrayDeque<Integer>();
                PriorityQueue pq = new PriorityQueue();


                while (n-- > 0) {
                    String[] line = sc.readLine().split(" ");
                    int c = Integer.parseInt(line[0]);
                    int k = Integer.parseInt(line[1]);
                    switch (c) {
                        case 1:
                            if (truth % 2 == 1) {
                                stack.offerLast(k);
                            }
                            if ((truth>>1) % 2 == 1) {
                                queue.offerLast(k);
                            }
                            if ((truth>>2) % 2 == 1) {
                                pq.insert(k);
                            }
                            break;
                        case 2:
                            int sPoll, qPoll;
                            if (stack.size() != 0) {
                                sPoll = stack.pollLast();
                            } else {
                                sPoll = -1;
                            }
                            if (queue.size() != 0) {
                                qPoll = queue.pollFirst();
                            } else {
                                qPoll = -1;
                            }
                            if (truth % 2 == 1 && sPoll != k) {
                                truth--;
                            }
                            if ((truth>>1) % 2 == 1 && qPoll != k) {
                                truth -= 2;
                            }
                            if ((truth>>2) % 2 == 1 && pq.extractMax() != k) {
                                truth -= 4;
                            }
                            break;
                    }
                }

                if (truth == 0) {
                    writer.println("impossible");
                } else if (truth == 1) {
                    writer.println("stack");
                } else if (truth == 2) {
                    writer.println("queue");
                } else if (truth == 4) {
                    writer.println("priority queue");
                } else {
                    writer.println("not sure");
                }
            }
            catch (NumberFormatException e) {
                writer.flush();
                return;
            }
        }
    }
}

// Will use java.util.Stack and java.util.Queue or java.util.Deque instead

class PriorityQueue {
    public ArrayList<Integer> A;
    public int PriorityQueueSize;

    PriorityQueue() {
        A = new ArrayList<Integer>();
        A.add(0);
        PriorityQueueSize = 0;
    }

    int parent(int i) { return i>>1; }
    int left(int i) { return i<<1; }
    int right(int i) { return (i<<1) + 1; }

    void shiftUp(int i) {
        while (i > 1 && A.get(parent(i)) < A.get(i)) {
            int temp = A.get(i);
            A.set(i, A.get(parent(i)));
            A.set(parent(i), temp);
            i = parent(i);
        }
    }

    void insert(int key) {
        PriorityQueueSize++;
        if (PriorityQueueSize >= A.size())
            A.add(key);
        else
            A.set(PriorityQueueSize, key);
        shiftUp(PriorityQueueSize);
    }

    void shiftDown(int i) {
        while (i <= PriorityQueueSize) {
            int maxV = A.get(i), max_id = i;

            // compare value of this node with its left subtree, if possible
            if (left(i) <= PriorityQueueSize && maxV < A.get(left(i))) { 
                maxV = A.get(left(i));
                max_id = left(i);
            }
            // now compare with its right subtree, if possible
            if (right(i) <= PriorityQueueSize && maxV < A.get(right(i))) {
                // maxV = A.get(right(i));
                max_id = right(i);
            }

            if (max_id != i) {
                int temp = A.get(i);
                A.set(i, A.get(max_id));
                A.set(max_id, temp);
                i = max_id;
            }
            else
                break;
        }
    }
  
    int extractMax() {
        int maxV=0;
        if (PriorityQueueSize != 0) {
            maxV = A.get(1);    
            A.set(1, A.get(PriorityQueueSize));
            PriorityQueueSize--; // virtual decrease
            shiftDown(1);
        } else {
            return -1; // since x is always a positive integer
        }
        return maxV;
    }

    int size() { return PriorityQueueSize; }
    boolean isEmpty() { return PriorityQueueSize == 0; }
}