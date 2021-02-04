// longer when run than CardTrading.java, but is more intuitive for non-OOP users

import java.io.*;
import java.util.*;

public class CardTrading2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        BSComparator bsComp = new BSComparator();
        
        String[] ntk = sc.readLine().split(" ");
        // int n = Integer.parseInt(ntk[0]); // cardsLine.length, so no need to parse
        int t = Integer.parseInt(ntk[1]);
        int k = Integer.parseInt(ntk[2]);
        List<List<Integer>> cards = new ArrayList<List<Integer>>();

        for (int types = 0; types < t; types++) {
            List<Integer> typeList = new ArrayList<Integer>();
            typeList.add(0); // for qty
            cards.add(typeList); // index k is of card type k+1
        }

        String[] cardsLine = sc.readLine().split(" ");
        for (int i = 0; i < cardsLine.length; i++) {
            cards.get(Integer.parseInt(cardsLine[i])-1).set(0,cards.get(Integer.parseInt(cardsLine[i])-1).get(0)+1);
        }
        
        for (int j = 0; j < t; j++) {
            String[] buysell = sc.readLine().split(" ");
            cards.get(j).add((2-cards.get(j).get(0))*Integer.parseInt(buysell[0])); // set "buy" value based on qty
            cards.get(j).add(cards.get(j).get(0)*Integer.parseInt(buysell[1])); // set "sell" value based on qty
        }

        Long answer = 0L; // due to large value of input, we use Long

        cards.sort(bsComp); // idea : check how many can you buy/sell, check the range of B-S
        for (int combo = 0; combo < k; combo++) {
            answer -= cards.get(combo).get(1);
        }
        for (int sold = k; sold < t; sold++) {
            answer += cards.get(sold).get(2);
        }

        // Final answer
        writer.println(answer);
        writer.flush();
    }
}

class BSComparator implements Comparator<List<Integer>> {
    public int compare(List<Integer> l1, List<Integer> l2) {
        return l1.get(1)+l1.get(2)-l2.get(1)-l2.get(2);
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}