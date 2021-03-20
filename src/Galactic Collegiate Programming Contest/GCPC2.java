// Using Reader class

import java.io.*;
import java.util.*;

// Create a team class which stores the number of problems solved and the sum of its penalty
class Team {
    public int id;
    public int solved;
    public int penalty;

    // Constructor
    public Team(int i) {
        id = i;
        solved = 0;
        penalty = 0;
    }

    // The parameter for the AVL tree, given the current (solved,penalty) combination, I want to convert it to long like this
    //         _ _ _ _ _ _                      _ _ _ _ _ _ _ _ _                      _
    //  6 digit for solved problems        9 digit for total penalty     1/0 whether it's team 1 or not
    // Penalty is sorted in descending order, so I used (10^8 - penalty) for the second slot since total penalty <= 10^5 * 1000 = 10^8
    // Call the result the value of the team
    public long getValue() {
        // give priority for team 1 in case of both ties
        return (long) (solved*Math.pow(10,10)+10*(Math.pow(10,8)-penalty)+(id == 1 ? 1 : 0));
    }
}

class Vertex {
    public Vertex parent, left, right;
    public long key;
    public int height;
    public int size;
    public int count;

    // Constructor
    public Vertex(long v) { 
        key = v;
        parent = left = right = null;
        height = 0;
        size = 1;
        count = 1;
    }
}

// The AVL property holds based on the respective team values
class AVL {
    public Vertex root;

    // Constructor
    public AVL() {
        root = null;
    }

    public long search(long v) {
        Vertex res = search(root, v);
        return res == null ? -1 : res.key;
    }

    // Helper method for search
    public Vertex search(Vertex T, long v) {
        if (T == null)
            return null;                // not found
        else if (T.key == v)
            return T;                   // found
        else if (T.key < v)
            return search(T.right, v);  // search to the right
        else
            return search(T.left, v);   // search to the left
    }
    
    public long findMin() {
        return findMin(root);
    }

    // Helper method for findMin
    public long findMin(Vertex T) {
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

    public long findMax() {
        return findMax(root);
    }

    // Helper method for findMax
    public long findMax(Vertex T) {
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

    public long successor(long v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : successor(vPos);
    }

    // Helper method for successor
    public long successor(Vertex T) {
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

    public long predecessor(long v) {
        Vertex vPos = search(root, v);
        return vPos == null ? -1 : predecessor(vPos);
    }

    // Helper method for predecessor
    public long predecessor(Vertex T) {
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

    // Updates height recursively, will be used for insertion/deletion
    public void updateHeight(Vertex T) {
        if (T.left != null && T.right != null)  // have both L and R children
            T.height = Math.max(T.left.height,T.right.height) + 1;
        else if (T.left != null) // have only L children
            T.height = T.left.height + 1;
        else if (T.right != null) // have only R children
            T.height = T.right.height + 1;
        else // no children, is leaf
            T.height = 0;
    }

    // Updates size recursively, will be used for insertion/deletion
    // Since the AVL can have duplicate values, we store the frequency in the count attribute for each vertex
    public void updateSize(Vertex T) {
        // conditioning similar to updateHeight
        if (T.left != null && T.right != null)
            T.size = T.left.size + T.right.size + T.count;
        else if (T.left != null)
            T.size = T.left.size + T.count;
        else if (T.right != null)
            T.size = T.right.size + T.count;
        else // both are null
            T.size = T.count;
    }

    // Balance factor of a vertex T
    public int bf(Vertex T) {
        if (T.left != null && T.right != null)
            return T.left.height - T.right.height;
        else if (T.left != null)
            return T.left.height + 1;
        else if (T.right != null)
            return -1 - T.right.height;
        else
            return 0;
    }

    public void insert(long v) {
        root = insert(root, v);
    }

    // Helper method for insert
    public Vertex insert(Vertex T, long v) {
        if (T == null)
            return new Vertex(v);           // insertion point is found

        if (T.key < v) {                    // search to the right
            T.right = insert(T.right, v);
            T.right.parent = T;
        }
        else if (T.key > v) {               // search to the left
            T.left = insert(T.left, v);
            T.left.parent = T;
        }
        else // T.key == v, v exists!
            T.count++; // increment the frequency

        updateHeight(T);
        updateSize(T);
        T = rebalance(T);

        return T;                           // return the updated tree
    }  

    public void delete(long v) {
        root = delete(root, v);
    }

    // Helper method for delete
    public Vertex delete(Vertex T, long v) {
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
                    long successorV = successor(v);
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
        // Correct the pointers one by one without breaking the links between each node
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

        // Must return instead of void to update recursively
        return w;
    }

    public Vertex rightRotate(Vertex T) { // given T.left is not null
        // Mirrored version of leftRotate
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
            if (bf(T) == 2) { // T has a left child since bf > 0
                if (bf(T.left) == -1) { // LR case
                    T.left = leftRotate(T.left);
                }

                // Either LL or LR case, do this
                T = rightRotate(T);
            }
            else if (bf(T) == -2) { // T has a right child since bf < 0
                if (bf(T.right) == 1) { // RL case
                    T.right = rightRotate(T.right);
                }

                // Either RL or RR case, do this
                T = leftRotate(T);
            }
        }

        return T;
    }

    public int rank(long k) {
        return rank(root, k);
    }

    // Helper method for rank
    // Rank of k in a subtree of root T
    public int rank(Vertex T, long k) { // O(log N)
        if (T.key == k)             // it's the root
            if (T.left != null)
                return T.left.size + 1;
            else
                return 1;
        else if (T.key > k)         // k is somewhere in the left of the subtree
            return rank(T.left, k);
        else                        // k is somewhere in the right of the subtree
            if (T.left != null)
                return rank(T.right, k) + T.left.size + T.count; // it's not itself, so add T.count instead of 1
            else
                return rank(T.right, k) + T.count; // similar to above
    }
}

public class GCPC2 {
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
        
        // We assume that all teams have different team value since it is an AVL tree!
        AVL avl = new AVL(); // create new AVL tree
        List<Team> teams = new ArrayList<Team>(); // database for storing (solved,penalty) of each team
        for (int i = 0; i < n; i++) {
            teams.add(new Team(i+1)); // new team, insert to database
            avl.insert(teams.get(i).getValue()); // also insert the team value to AVL, which has handled duplicate values
        }

        // At this point, the AVL will contain only 2 nodes. The first node is the score for team 1, and the other is for the n-1 teams

        while (m-- > 0) {
            int t = sc.nextInt()-1;
            int p = sc.nextInt();
            long prev = teams.get(t).getValue(); // obtain the value of the team previously
            teams.get(t).solved++; // update number of solved problems
            teams.get(t).penalty += p; // update penalty score
            avl.delete(prev); // delete the previous score of team t+1;
            avl.insert(teams.get(t).getValue()); // insert the updated score;
            writer.println(n+1-avl.rank(teams.get(0).getValue())); // team 1, reverse order so n+1-rank
        }

        writer.flush();
    }
}