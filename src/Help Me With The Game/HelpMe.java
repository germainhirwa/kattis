import java.io.*;
import java.util.*;

public class HelpMe {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        Map<String, Character> hm = new HashMap<String, Character>();
        String[] alphabets = {"a", "b", "c", "d", "e", "f", "g", "h"};

        String firstLine = sc.readLine();
        for (int i = 8; i > 0; i--) {
            String[] line = sc.readLine().substring(1,32).split("\\|");
            for (int j = 0; j < 8; j++) {
                char check = line[j].charAt(1);
                if (!(check==':' || check=='.')) {
                    hm.put(alphabets[j]+i,check);
                }
            }
            // writer.println(Arrays.toString(line));
            String border = sc.readLine();
        }

        writer.print("White: ");
        List<String> coordinatesWhite = new ArrayList<String>();
        addCoordinates(coordinatesWhite,hm,'K');
        addCoordinates(coordinatesWhite,hm,'Q');
        addCoordinates(coordinatesWhite,hm,'R');
        addCoordinates(coordinatesWhite,hm,'B');
        addCoordinates(coordinatesWhite,hm,'N');
        addCoordinates(coordinatesWhite,hm,'P');
        for (int cw = 0; cw < coordinatesWhite.size()-1; cw++){
            writer.print(coordinatesWhite.get(cw));
            writer.print(',');
        }
        if (coordinatesWhite.size() > 0) {
            writer.println(coordinatesWhite.get(coordinatesWhite.size()-1));
        } else {
            writer.println();
        }
        
        writer.print("Black: ");
        List<String> coordinatesBlack = new ArrayList<String>();
        addCoordinates(coordinatesBlack,hm,'k');
        addCoordinates(coordinatesBlack,hm,'q');
        addCoordinates(coordinatesBlack,hm,'r');
        addCoordinates(coordinatesBlack,hm,'b');
        addCoordinates(coordinatesBlack,hm,'n');
        addCoordinates(coordinatesBlack,hm,'p');
        for (int cb = 0; cb < coordinatesBlack.size()-1; cb++){
            writer.print(coordinatesBlack.get(cb));
            writer.print(',');
        }
        if (coordinatesBlack.size() > 0) {
            writer.println(coordinatesBlack.get(coordinatesBlack.size()-1));
        } else {
            writer.println();
        }

        // writer.println(Arrays.asList(hm));
        writer.flush();
    }

    public static void addCoordinates(List<String> coordinates, Map<String, Character> map, Character value) {
        ConflictComparatorWhite ccw = new ConflictComparatorWhite();
        ConflictComparatorBlack ccb = new ConflictComparatorBlack();
        List<String> result = new ArrayList<String>();

        if (map.containsValue(value)) {
            for (String key : map.keySet()) {
                if (value.equals(map.get(key))) {
                    result.add(key);
                }
            }

            if (Character.toUpperCase(value) == value) { // white
                result.sort(ccw);
            } else {
                result.sort(ccb);
            }

            for (int k = 0; k < result.size(); k++) {
                if (Character.toUpperCase(value) != 'P') {
                    coordinates.add(Character.toUpperCase(value)+result.get(k));
                } else {
                    coordinates.add(result.get(k));
                }
            }
        }
    }
}

class ConflictComparatorWhite implements Comparator<String> {
    public int compare(String s1, String s2) { // Example a4, b5
        int col1 = (int) s1.charAt(0); // (int) 'a' = 97
        int col2 = (int) s2.charAt(0); // (int) 'b' = 98
        int row1 = Character.getNumericValue(s1.charAt(1)); // 4
        int row2 = Character.getNumericValue(s2.charAt(1)); // 5
        return (row1-row2)*31 + (col1-col2);
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}

class ConflictComparatorBlack implements Comparator<String> {
    public int compare(String s1, String s2) { // Example a4, b5
        int col1 = (int) s1.charAt(0); // (int) 'a' = 97
        int col2 = (int) s2.charAt(0); // (int) 'b' = 98
        int row1 = Character.getNumericValue(s1.charAt(1)); // 4
        int row2 = Character.getNumericValue(s2.charAt(1)); // 5
        return (row2-row1)*31 + (col1-col2);
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}