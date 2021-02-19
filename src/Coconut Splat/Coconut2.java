// Alternative implementation with Deque

import java.io.*;
import java.util.*;

public class Coconut2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int s = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);

        Deque<Coco> coconuts = new ArrayDeque<Coco>();
        for (int i = 0; i < n; i++) {
            coconuts.offerLast(new Coco(i+1));
        }

        while (coconuts.size() != 1) {
            for (int i = 0; i < s-1; i++) {
                coconuts.offerLast(coconuts.pollFirst()); // remove front and put to the back
            }
            if (coconuts.getFirst().isFolded()) {
                coconuts.getFirst().life -= 1;
                coconuts.offerFirst(new Coco(coconuts.getFirst().id, coconuts.getFirst().life));
            } else if (coconuts.getFirst().isFist()) {
                coconuts.getFirst().life -= 1;
                coconuts.offerLast(coconuts.pollFirst()); // remove front and put to the back
            } else {
                coconuts.pollFirst();
            }
        }
        writer.print(coconuts.getFirst().id);
        writer.flush();
    }
}

class Coco {
    public int id;
    public int life;

    public Coco(int id) {
        this.id = id;
        this.life = 2;
    }
    public Coco(int id, int life) {
        this.id = id;
        this.life = life;
    }

    public boolean isFolded() { return life == 2; }
    public boolean isFist() { return life == 1; }

    public String toString() {
        return this.id+"-"+this.life;
    }
}