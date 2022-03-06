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

    public int search(int v) {
        Vertex res = search(root, v);
        return res == null ? -1 : res.key;
    }

    // Helper method for search
    public Vertex search(Vertex T, int v) {
        if (T == null)
            return null;                // not found
        else if (T.key == v)
            return T;                   // found
        else if (T.key < v)
            return search(T.right, v);  // search to the right
        else
            return search(T.left, v);   // search to the left
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

    public int findMin() {
        return findMin(root);
    }

    // Helper method for findMin
    public int findMin(Vertex T) {
        // Empty tree
        if (T == null) {
            return -1;
        }

        // Non-empty tree
        if (T.left == null)
            return T.key;               // this is the min
        else
            return findMin(T.left);     // go to the left
    }

    public int findMax() {
        return findMax(root);
    }

    // Helper method for findMax
    public int findMax(Vertex T) {
        // Empty tree
        if (T == null) {
            return -1;
        }

        // Non-empty tree
        if (T.right == null)
            return T.key;               // this is the max
        else
            return findMax(T.right);    // go to the right
    }

    public int successor(int v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : successor(vPos);
    }

    // Helper method for successor
    public int successor(Vertex T) {
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
            return par == null ? -1 : par.key;  // this is the successor of T
        }
    }

    public int predecessor(int v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : predecessor(vPos);
    }

    // Helper method for predecessor
    public int predecessor(Vertex T) {
        if (T.left != null)                     // this subtree has a left subtree
            return findMax(T.left);             // the successor is the maximum of left subtree
        else {
            Vertex par = T.parent;
            Vertex cur = T;
            // if par(ent) is not root and cur(rent) is its left children
            while ((par != null) && (cur == par.left)) {
                cur = par;                      // continue moving up
                par = cur.parent;
            }
            return par == null ? -1 : par.key;  // this is the predecessor of T
        }
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
    
    public void delete(int v) {
        root = delete(root, v);
    }

    // Helper method for delete
    public Vertex delete(Vertex T, int v) {
        if (T == null)
            return T;                                       // cannot find the item to be deleted

        if (T.key < v)                                      // search to the right
            T.right = delete(T.right, v);
        else if (T.key > v)                                 // search to the left
            T.left = delete(T.left, v);
        else {                                              // this is the node to be deleted
            if (T.count == 1) {
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
                    int successorV = successor(v);
                    T.key = successorV;                         // replace this key with the successor's key
                    T.right = delete(T.right, successorV);      // delete the old successorV
                }
            } else  // no need to delete key from the tree, decrement frequency
                T.count--;
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

    // Selects the node with rank k
    public Vertex select(int k) {
        return select(root, k);
    }

    // Helper method for select
    public Vertex select(Vertex T, int k) { // O(log N)
        if ((T.left == null && 1 <= k && k <= T.count) || (T.left != null && T.left.size + 1 <= k && k <= T.left.size + T.count))
            return T;
        else if ((T.left == null && k > T.count) || (T.left != null && k > T.left.size + T.count)) // T is somewhere in the right of the subtree
            return T.left == null ? select(T.right, k-T.count) : select(T.right, k-T.left.size-T.count);
        else // T is somewhere in the left of the subtree
            return select(T.left, k);
    }
}

public class CookieSelection {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        AVL avl = new AVL();
        int size = 0;
        while (true) {
            try {
                String m = sc.readLine();
                if (m.equals("#")) {
                    int k = avl.select(size / 2 + 1).key;
                    writer.println(k);
                    avl.delete(k);
                    size--;
                } else {
                    avl.insert(Integer.parseInt(m));
                    size++;
                }
            } catch (Exception e) {
                break;
            }
        }

        writer.flush();
    }
}