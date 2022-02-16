import java.io.*;
import java.util.*;

class Vertex {
    public Vertex parent, left, right;
    public int key;
    public int height;
    public int size;
    public int count;

    // Constructor
    public Vertex(int v) { 
        key = v;
        parent = left = right = null;
        height = 0;
        size = 1;
        count = 1;
    }
}

class AVL {
    public Vertex root;

    public AVL() {
        this.root = null;
    }

    public int height(Vertex T) {
        if (T == null)
            return -1;
        else
            return T.height;
    }

    public int size(Vertex T) {
        if (T == null)
            return 0;
        else
            return T.size;
    }

    public void updateHeight(Vertex T) {
        T.height = 1 + Math.max(height(T.left), height(T.right));
    }

    public void updateSize(Vertex T) {
        T.size = size(T.left) + size(T.right) + T.count;
    }

    // Balance factor of a Vertex T
    public int bf(Vertex T) {
        if (T == null)
            return 0;
        else
            return height(T.left) - height(T.right);
    }

    public void insert(int v) {
        root = insert(root, v);
    }

    // Helper method for insert
    public Vertex insert(Vertex T, int v) {
        if (T == null)
            return new Vertex(v);           // insertion point is found

        if (T.key < v) {                    // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        } else if (T.key > v) {               // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        } else {
            T.count++;
            updateSize(T);
            return T;
        }

        updateHeight(T);
        updateSize(T);
        T = rebalance(T);

        return T;                           // return the updated tree
    }  

    public Vertex leftRotate(Vertex T) { // given T.right is not null
        Vertex w = T.right;
        w.parent = T.parent;
        T.parent = w;
        T.right = w.left;
        if (w.left != null)
            w.left.parent = T;
        w.left = T;

        updateHeight(T);
        updateSize(T);
        updateHeight(w);
        updateSize(w);

        return w;
    }

    public Vertex rightRotate(Vertex T) { // given T.left is not null
        Vertex w = T.left;
        w.parent = T.parent;
        T.parent = w;
        T.left = w.right;
        if (w.right != null)
            w.right.parent = T;
        w.right = T;

        updateHeight(T);
        updateSize(T);
        updateHeight(w);
        updateSize(w);

        return w;
    }

    public Vertex rebalance(Vertex T) {
        if (T != null) {
            if (bf(T) == 2) { // T has a left child
                if (bf(T.left) == -1) { // LR case
                    T.left = leftRotate(T.left);
                }

                // Either LL or LR case, do this
                T = rightRotate(T);
            }
            else if (bf(T) == -2) { // T has a right child
                if (bf(T.right) == 1) { // RL case
                    T.right = rightRotate(T.right);
                }

                // Either RL or RR case, do this
                T = leftRotate(T);
            }
        }

        return T;
    }

    public int rank(int k) { // num of vertex < k
        return rank(root, k);
    }

    public int rank(Vertex T, int k) { // O(log N)
        if (T == null) {
            return 0;
        }

        if (T.key == k)             // it's the root
            if (T.left != null)
                return T.left.size;
            else
                return 0;
        else if (T.key > k)         // k is somewhere in the left of the subtree
            return rank(T.left, k);
        else                        // k is somewhere in the right of the subtree
            if (T.left != null)
                return rank(T.right, k) + T.left.size + T.count; // it's not itself, so add T.count instead of 1
            else
                return rank(T.right, k) + T.count; // similar to above
    }
}

public class MassiveCardGame {
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
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
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
        AVL avl = new AVL();
        while (n-- > 0) {
            avl.insert(sc.nextInt());
        }
        int q = sc.nextInt();
        Map<Long, Integer> hm = new HashMap<Long, Integer>();
        while(q-- > 0) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            long k = (long) a * 1_000_000_001 + (long) b;
            if (hm.get(k) == null) {
                int res = avl.rank(b + 1) - avl.rank(a);
                hm.put(k, res);
            }
            writer.println(hm.get(k));
        }

        writer.flush();
    }
}