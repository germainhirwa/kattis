import java.io.*;
import java.util.*;

public class Classy {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        StatusComparator statusComp = new StatusComparator();
        
        String eq = "=";
        int tc = Integer.parseInt(sc.readLine());
        for (int t = 0; t < tc; t++) {
            List<Person> peopleList = new ArrayList<Person>();
            int n = Integer.parseInt(sc.readLine());
            for (int p = 0; p < n; p++) {
                String[] stats = sc.readLine().split(": ");
                peopleList.add(new Person(stats[0],stats[1].substring(0,stats[1].length()-6)));
            }

            peopleList.sort(statusComp);
            
            for (int k = 0; k < n; k++) {
                writer.println(peopleList.get(k).name);
            }
            for (int e = 0; e < 30; e++) {
                writer.print("=");
            }
            writer.println();
        }

        writer.flush();
    }
}

class Person {
    public String name;
    public String[] status;

    public Person (String name, String sts) {
        this.name = name;
        this.status = sts.split("-");
    }

    public String toString() {
        return this.name+"-"+Arrays.asList(this.status);
    }
}

class StatusComparator implements Comparator<Person> {
    public int compare(Person p1, Person p2) {
        int maxLength = Math.max(p1.status.length,p2.status.length);
        int minLength = Math.min(p1.status.length,p2.status.length);
        int p1Status = 0, p2Status = 0;
        for (int i = 0; i < minLength; i++) {
            switch (p1.status[p1.status.length-i-1]) {
                case "upper":
                    p1Status += 2*Math.pow(3,maxLength-i-1);
                    break;
                case "middle":
                    p1Status += Math.pow(3,maxLength-i-1);
                    break;
            }
            switch (p2.status[p2.status.length-i-1]) {
                case "upper":
                    p2Status += 2*Math.pow(3,maxLength-i-1);
                    break;
                case "middle":
                    p2Status += Math.pow(3,maxLength-i-1);
                    break;
            }
        }
        for (int j = minLength; j < maxLength; j++) {
            if (p1.status.length == minLength) {
                p1Status += Math.pow(3,maxLength-j-1);
            } else {
                switch (p1.status[p1.status.length-j-1]) {
                    case "upper":
                        p1Status += 2*Math.pow(3,maxLength-j-1);
                        break;
                    case "middle":
                        p1Status += Math.pow(3,maxLength-j-1);
                        break;
                }
            }
            if (p2.status.length == minLength) {
                p2Status += Math.pow(3,maxLength-j-1);
            } else {
                switch (p2.status[p2.status.length-j-1]) {
                    case "upper":
                        p2Status += 2*Math.pow(3,maxLength-j-1);
                        break;
                    case "middle":
                        p2Status += Math.pow(3,maxLength-j-1);
                        break;
                }
            }
        }
        if (p1Status == p2Status) {
            return p1.name.compareTo(p2.name);
        } else {
            return p2Status-p1Status;
        }
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}