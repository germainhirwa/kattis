import java.io.*;
import java.util.*;

public class IntervalScheduling {
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
        
        List<Interval> ints = new ArrayList<Interval>();
        List<Interval> comints = new ArrayList<Interval>();
        int n = sc.nextInt();

        while (n-- > 0) {
            ints.add(new Interval(sc.nextInt(), sc.nextInt()));
        }
        ints.sort((x, y) -> x.compareTo(y));

        for (Interval in : ints) {
            if (comints.size() == 0 || comints.get(comints.size() - 1).leaveTime <= in.arrTime) {
                comints.add(in);
            }
        }

        writer.println(comints.size());
        writer.flush();
    }
}

class Interval {
    public int arrTime;
    public int leaveTime;
    public int group;

    public Interval(int a, int s) {
        arrTime = a;
        leaveTime = s;
    }

    public int compareTo(Interval another) {
        return this.leaveTime - another.leaveTime;
    }
}