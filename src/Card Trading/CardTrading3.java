// Using Reader class to further improve I/O runtime

import java.io.*;
import java.util.*;

public class CardTrading3 {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
 
        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public int nextInt() throws IOException
        {
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
 
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }
 
        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);

        BSValueComparator bsvComp = new BSValueComparator();
        
        int n = sc.nextInt(); // cardsLine.length
        int t = sc.nextInt();
        int k = sc.nextInt();
        List<CardContainer> containers = new ArrayList<CardContainer>();

        for (int types = 0; types < t; types++) {
            CardContainer c = new CardContainer();
            containers.add(c); // index k is container of card type k+1
        }

        for (int i = 0; i < n; i++) {
            containers.get(sc.nextInt()-1).qty += 1; // add 1 to quantity
        }
        
        for (int j = 0; j < t; j++) {
            containers.get(j).setBuy((2-containers.get(j).qty)*sc.nextInt()); // set "buy" value based on qty
            containers.get(j).setSell(containers.get(j).qty*sc.nextInt()); // set "sell" value based on qty
        }

        Long answer = 0L; // due to large value of input, we use Long

        containers.sort(bsvComp); // idea : check how many can you buy/sell, check the range of B-S
        for (int combo = 0; combo < k; combo++) {
            answer -= containers.get(combo).buy;
        }
        for (int sold = k; sold < t; sold++) {
            answer += containers.get(sold).sell;
        }

        // Final answer
        writer.println(answer);
        writer.flush();
    }
}

class CardContainer {
    public int qty;
    public int buy;
    public int sell;

    public CardContainer() {
        this.qty = 0;
        this.buy = 0;
        this.sell = 0;
    }
    
    public void setBuy(int buy) {this.buy = buy;}
    public void setSell(int sell) {this.sell = sell;}

    // Visualizer, if needed
    // public String toString() {return this.type + " & buy " + this.buy + " & sell " + this.sell + " & value " + (this.buy+this.sell);}
}

class BSValueComparator implements Comparator<CardContainer> {
    public int compare(CardContainer c1, CardContainer c2) {
        return (c1.buy+c1.sell)-(c2.buy+c2.sell);
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}