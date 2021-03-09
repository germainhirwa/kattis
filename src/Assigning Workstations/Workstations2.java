// Using Reader class to further improve I/O runtime

import java.io.*;
import java.util.*;

public class Workstations2 {
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
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        BinaryHeapR pqR = new BinaryHeapR();
        BinaryHeapW pqW = new BinaryHeapW();

        for (int i = 0; i < n; i++) {
            int a = sc.nextInt();
            int s = sc.nextInt();
            pqR.insert(new Researcher(a,s)); // insert the researchers into the researcher PQ
        }

        long locked = 0L;

        for (int i = 0; i < n; i++) {
            Researcher maxR = pqR.extractMax(); // next researcher to be assigned
            Workstation currW;
            while (!pqW.isEmpty()) { // keep extracting locked-for-good workstations
                currW = pqW.peekMax();
                if (currW.curr + currW.lock < maxR.arrTime) {
                    pqW.extractMax();
                    locked++;
                } else { // we have an unlocked workstation!
                    break;
                }
            }

            if (!pqW.isEmpty()) {
                currW = pqW.peekMax();
                if (currW.curr <= maxR.arrTime && maxR.arrTime <= currW.curr + currW.lock) { // the workstation is not used and is unlocked
                    currW = pqW.extractMax();
                    currW.curr = maxR.leaveTime;
                    pqW.insert(currW);
                } else { // must assign new workstation since the current closest workstation is still in use
                    Workstation newW = new Workstation(m);
                    newW.curr = maxR.leaveTime;
                    pqW.insert(newW);
                }
            } else { // must assign new workstation since the new PQ is empty
                Workstation newW = new Workstation(m);
                newW.curr = maxR.leaveTime;
                pqW.insert(newW);
            }
        }

        writer.println(n-locked-pqW.size());
        writer.flush();
    }
}

class Workstation {
    public int lock;
    public int curr;

    public Workstation(int m) {
        lock = m;
        curr = 0; // last time used
    }

    public int compareTo(Workstation another) {
        return this.curr - another.curr;
    }
}

class Researcher {
    public int arrTime;
    public int leaveTime;

    public Researcher(int a, int s) {
        arrTime = a;
        leaveTime = a+s;
    }

    public int compareTo(Researcher another) {
        return this.arrTime - another.arrTime;
    }
}

class BinaryHeapR {
    public ArrayList<Researcher> A;
    public int BinaryHeapSize;

    BinaryHeapR() {
        A = new ArrayList<Researcher>();
        A.add(new Researcher(0,0)); // dummy value
        BinaryHeapSize = 0;
    }

    int parent(int i) { return i>>1; } // shortcut for i/2, round down
    
    int left(int i) { return i<<1; } // shortcut for i*2
    
    int right(int i) { return (i<<1) + 1; } // shortcut for i*2 + 1
    
    void shiftUp(int i) {
        while (i > 1 && A.get(parent(i)).compareTo(A.get(i)) > 0) {
            Researcher temp = A.get(i);
            A.set(i, A.get(parent(i)));
            A.set(parent(i), temp);
            i = parent(i);
        }
    }

    void insert(Researcher key) {
        BinaryHeapSize++;
        if (BinaryHeapSize >= A.size())
            A.add(key);
        else
            A.set(BinaryHeapSize, key);
        shiftUp(BinaryHeapSize);
    }

    void shiftDown(int i) {
        while (i <= BinaryHeapSize) {
            Researcher maxV = A.get(i);
            int max_id = i;

            // compare value of this node with its left subtree, if possible
            if (left(i) <= BinaryHeapSize && maxV.compareTo(A.get(left(i))) > 0) { 
                maxV = A.get(left(i));
                max_id = left(i);
            }
            // now compare with its right subtree, if possible
            if (right(i) <= BinaryHeapSize && maxV.compareTo(A.get(right(i))) > 0) {
                max_id = right(i);
            }
    
            if (max_id != i) {
                Researcher temp = A.get(i);
                A.set(i, A.get(max_id));
                A.set(max_id, temp);
                i = max_id;
            }
            else
                break;
        }
    }
    
    Researcher extractMax() {
        // Assuming heap is never empty when extracted
        Researcher maxV = A.get(1);
        A.set(1, A.get(BinaryHeapSize));
        BinaryHeapSize--; // virtual decrease
        shiftDown(1);
        return maxV;
    }

    int size() { return BinaryHeapSize; }
}

class BinaryHeapW {
    public ArrayList<Workstation> A;
    public int BinaryHeapSize;

    BinaryHeapW() {
        A = new ArrayList<Workstation>();
        A.add(new Workstation(0)); // dummy value
        BinaryHeapSize = 0;
    }

    int parent(int i) { return i>>1; } // shortcut for i/2, round down
    
    int left(int i) { return i<<1; } // shortcut for i*2
    
    int right(int i) { return (i<<1) + 1; } // shortcut for i*2 + 1
    
    void shiftUp(int i) {
        while (i > 1 && A.get(parent(i)).compareTo(A.get(i)) > 0) {
            Workstation temp = A.get(i);
            A.set(i, A.get(parent(i)));
            A.set(parent(i), temp);
            i = parent(i);
        }
    }

    void insert(Workstation key) {
        BinaryHeapSize++;
        if (BinaryHeapSize >= A.size())
            A.add(key);
        else
            A.set(BinaryHeapSize, key);
        shiftUp(BinaryHeapSize);
    }

    void shiftDown(int i) {
        while (i <= BinaryHeapSize) {
            Workstation maxV = A.get(i);
            int max_id = i;

            // compare value of this node with its left subtree, if possible
            if (left(i) <= BinaryHeapSize && maxV.compareTo(A.get(left(i))) > 0) { 
                maxV = A.get(left(i));
                max_id = left(i);
            }
            // now compare with its right subtree, if possible
            if (right(i) <= BinaryHeapSize && maxV.compareTo(A.get(right(i))) > 0) {
                max_id = right(i);
            }
    
            if (max_id != i) {
                Workstation temp = A.get(i);
                A.set(i, A.get(max_id));
                A.set(max_id, temp);
                i = max_id;
            }
            else
                break;
        }
    }
    
    Workstation extractMax() {
        // Assuming heap is never empty when extracted
        Workstation maxV = A.get(1);
        A.set(1, A.get(BinaryHeapSize));
        BinaryHeapSize--; // virtual decrease
        shiftDown(1);
        return maxV;
    }

    Workstation peekMax() {
        return A.get(1);
    }

    int size() { return BinaryHeapSize; }
    
    boolean isEmpty() { return BinaryHeapSize == 0; }
}