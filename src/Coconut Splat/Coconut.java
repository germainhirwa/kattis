import java.io.*;
import java.util.*;

public class Coconut {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int s = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);

        List<Coco> coconuts = new ArrayList<Coco>();
        for (int i = 0; i < n; i++) {
            coconuts.add(new Coco(i+1));
        }

        int splat = 0;
        while (coconuts.size() != 1) {
            splat = (splat + s - 1) % coconuts.size();
            if (coconuts.get(splat).isFolded()) {
                coconuts.get(splat).life -= 1;
                coconuts.add(splat,new Coco(coconuts.get(splat).id, coconuts.get(splat).life));
            } else if (coconuts.get(splat).isFist()) {
                coconuts.get(splat).life -= 1;
                splat += 1;
            } else {
                coconuts.remove(splat);
            }
        }
        writer.print(coconuts.get(0).id);
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