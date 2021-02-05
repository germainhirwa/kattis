import java.io.*;
import java.util.*;

public class CardTrading {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        BSValueComparator bsvComp = new BSValueComparator();
        
        String[] ntk = sc.readLine().split(" ");
        int n = Integer.parseInt(ntk[0]); // cardsLine.length
        int t = Integer.parseInt(ntk[1]);
        int k = Integer.parseInt(ntk[2]);
        List<CardContainer> containers = new ArrayList<CardContainer>();

        for (int types = 0; types < t; types++) {
            CardContainer c = new CardContainer();
            containers.add(c); // index k is container of card type k+1
        }

        String[] cardsLine = sc.readLine().split(" ");
        for (int i = 0; i < cardsLine.length; i++) {
            containers.get(Integer.parseInt(cardsLine[i])-1).qty += 1; // add 1 to quantity
        }
        
        for (int j = 0; j < t; j++) {
            String[] buysell = sc.readLine().split(" ");
            containers.get(j).setBuy((2-containers.get(j).qty)*Integer.parseInt(buysell[0])); // set "buy" value based on qty
            containers.get(j).setSell(containers.get(j).qty*Integer.parseInt(buysell[1])); // set "sell" value based on qty
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