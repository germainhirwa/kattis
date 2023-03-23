// Uses HashMap, same running time

import java.io.*;
import java.util.*;

public class Amazing2 {
    static Map<Integer,Integer> exploredSet = new HashMap<Integer,Integer>();   // hashmap to contain the explored directed edges
    static String[] moves = {"left","up","right","down"};                       // moves
    static int[] xmoves = {-1,0,1,0};                                           // delta x
    static int[] ymoves = {0,1,0,-1};                                           // delta y

    // I/O
    static InputStreamReader inp = new InputStreamReader(System.in);
    static BufferedReader sc = new BufferedReader(inp);
    static PrintWriter writer = new PrintWriter(System.out);
    static String output;

    public static void main(String[] args) throws IOException {
        DFS(0,0,0); // Run DFS from (0,0) with any direction, I chose 0 here
    }

    public static void DFS (int i, int j, int dir) throws IOException {
        for (int m = 1; m <= 4; m++) {
            int k = (dir+m+2) % 4;                          // For every (unexplored) edges where the incoming side is the last iterated
            if (exploredSet.get(hash(i,j,k)) == null) {
                exploredSet.put(hash(i,j,k),1);             // Add edge to explored set
                writer.println(moves[k]);                   // Try to move
                writer.flush();
                output = sc.readLine();
                if (output.equals("solved"))                // Done
                    System.exit(0);
                else if (output.equals("wall"))             // Hit a wall, go on with the next iteration
                    continue;
                else if (output.equals("ok"))               // Recursively run DFS from the next point
                    DFS(i+xmoves[k],j+ymoves[k],k);         // dir is k since we want that side to be the last iterated, to avoid trivial cyclical moves
            }
        }

        // No way out since this statement is reached
        writer.println("no way out");
        writer.flush();
        System.exit(0);
    }

    public static int hash (int x, int y, int dir) { // hashes edges to integer
        return 1000*x + 10*y + dir;
    }
}