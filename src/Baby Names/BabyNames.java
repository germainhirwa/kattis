import java.io.*;
import java.util.*;

class Vertex {
    public Vertex parent, left, right;
    public String key;
    public int height;
    public int size;

    // Constructor
    public Vertex(String v) { 
        key = v;
        parent = left = right = null;
        height = 0;
        size = 1;
    }
}

class AVL {
    public Vertex root;

    public AVL() {
        this.root = null;
    }

    public String search(String v) {
        Vertex res = search(root, v);
        return res == null ? null : res.key;
    }

    // Helper method for search
    public Vertex search(Vertex T, String v) {
        if (T == null)
            return null;                // not found
        else if (T.key.compareTo(v) == 0)
            return T;                   // found
        else if (T.key.compareTo(v) < 0)
            return search(T.right, v);  // search to the right
        else
            return search(T.left, v);   // search to the left
    }

    public String findMin() {
        return findMin(root);
    }

    // Helper method for findMin
    public String findMin(Vertex T) {
        // Empty tree
        if (T == null) {
            return null;
        }

        // Non-empty tree
        if (T.left == null)
            return T.key;               // this is the min
        else
            return findMin(T.left);     // go to the left
    }

    // Inorder traversal
    public void inorder() { 
        inorder(root);
        System.out.println();
    }

    // Helper method for inorder
    public void inorder(Vertex T) {
        if (T == null)
            return;
        inorder(T.left);                    // recursively go to the left
        System.out.print(" " + T.key.toString());
        inorder(T.right);                   // recursively go to the right
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
        T.size = size(T.left) + size(T.right) + 1;
    }

    // Balance factor of a Vertex T
    public int bf(Vertex T) {
        if (T == null)
            return 0;
        else
            return height(T.left) - height(T.right);
    }

    public String successor(String v) {
        Vertex vPos = search(root, v);
        return vPos == null ? null : successor(vPos);
    }

    // Helper method for successor
    public String successor(Vertex T) {
        if (T.right != null)                    // this subtree has a right subtree
            return findMin(T.right);            // the successor is the minimum of right subtree
        else {
            Vertex par = T.parent;
            Vertex cur = T;
            // if par(ent) is not root and cur(rent) is its right children
            while ((par != null) && (cur == par.right)) {
                cur = par;                      // continue moving up
                par = cur.parent;
            }
            return par == null ? null : par.key;  // this is the successor of T
        }
    }

    public void insert(String v) {
        root = insert(root, v);
    }

    // Helper method for insert
    public Vertex insert(Vertex T, String v) {
        if (T == null)
            return new Vertex(v);           // insertion point is found

        if (T.key.compareTo(v) < 0) {                    // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        }
        else if (T.key.compareTo(v) > 0) {               // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }

        updateHeight(T);
        updateSize(T);
        T = rebalance(T);

        return T;                           // return the updated tree
    }  

    public void delete(String v) {
        root = delete(root, v);
    }

    // Helper method for delete
    public Vertex delete(Vertex T, String v) {
        if (T == null)
            return T;                                       // cannot find the item to be deleted

        if (T.key.compareTo(v) < 0)                                      // search to the right
            T.right = delete(T.right, v);
        else if (T.key.compareTo(v) > 0)                                 // search to the left
            T.left = delete(T.left, v);
        else {                                              // this is the node to be deleted
            if (T.left == null && T.right == null)          // this is a leaf
                T = null;                                   // simply erase this node for good
            else if (T.left == null && T.right != null) {   // only one child at right
                T.right.parent = T.parent;
                T = T.right;                                // bypass T
            }
            else if (T.left != null && T.right == null) {   // only one child at left
                T.left.parent = T.parent;
                T = T.left;                                 // bypass T
            }
            else {                                          // has two children, find successor
                String successorV = successor(v);
                T.key = successorV;                         // replace this key with the successor's key
                T.right = delete(T.right, successorV);      // delete the old successorV
            }
        }

        // For every node, if it is not deleted for good, do the rebalancing
        if (T != null) {
            updateHeight(T);
            updateSize(T);
            T = rebalance(T);
        }

        return T; // return the updated tree
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

    public int rank(String k) {
        return rank(root, k);
    }

    // Helper method for rank
    // Rank of k in a subtree of root T
    public int rank(Vertex T, String k) { // O(log N)
        if (T == null)
            return 0;
        if (T.key.compareTo(k) == 0)             // it's the root
            if (T.left != null)
                return T.left.size + 1;
            else
                return 1;
        else if (T.key.compareTo(k) > 0)         // k is somewhere in the left of the subtree
            return rank(T.left, k);
        else                        // k is somewhere in the right of the subtree
            if (T.left != null)
                return rank(T.right, k) + T.left.size + 1;
            else
                return rank(T.right, k) + 1; // similar to above
    }
}

public class BabyNames {
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();
        AVL male = new AVL();
        AVL female = new AVL();

        while (true) {
            int q = fio.nextInt();
            if (q == 0) {
                fio.close();
                return;
            }

            if (q == 1) {
                String name = fio.next();
                int gs = fio.nextInt();
                if (gs == 1)
                    male.insert(name);
                else
                    female.insert(name);
            } else if (q == 2) {
                String name = fio.next();
                male.delete(name);
                female.delete(name);
            } else { // q = 3
                String start = fio.next(), end = fio.next();
                int gs = fio.nextInt(), ans = 0;
                if (gs != 1)
                    ans += female.rank(end) - female.rank(start) - (female.search(end) == null ? 0 : 1);
                if (gs != 2)
                    ans += male.rank(end) - male.rank(start) - (male.search(end) == null ? 0 : 1);
                fio.println(ans);
            }
        }
    }
}

class FastIO extends PrintWriter { 
    BufferedReader br; 
    StringTokenizer st;

    public FastIO() { 
        super(new BufferedOutputStream(System.out)); 
        br = new BufferedReader(new InputStreamReader(System.in));
    } 

    String next() { 
        while (st == null || ! st.hasMoreElements()) { 
            try { st = new StringTokenizer(br.readLine()); } 
            catch (IOException  e) { e.printStackTrace(); } 
        } 
        return st.nextToken(); 
    } 

    int nextInt() { return Integer.parseInt(next()); } 
    long nextLong() { return Long.parseLong(next()); } 
    double nextDouble() { return Double.parseDouble(next()); } 

    String nextLine() { 
        String str = ""; 
        try { str = br.readLine(); } 
        catch (IOException e) { e.printStackTrace(); } 
        return str; 
    } 
}