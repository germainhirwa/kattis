import java.io.*;
import java.util.*;

public class BestRelayTeam {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int queries = Integer.parseInt(sc.readLine());
        List<Runner> runners = new ArrayList<Runner>();
        Leg2Comparator leg2Comp = new Leg2Comparator();
        
        // input and insert everything
        while (queries-- > 0) {
            String[] line = sc.readLine().split(" ");
            String name = line[0];
            double leg1 = Double.parseDouble(line[1]);
            double leg2 = Double.parseDouble(line[2]);
            runners.add(new Runner(name,leg1,leg2));
        }

        runners.sort(leg2Comp);
        List<Runner> top3Leg2 = new ArrayList<Runner>();
        List<String> top3Leg2Names = new ArrayList<String>(); // basically the name of the runners in top3Leg2
        for (int a = 0; a < 3; a++) {
            top3Leg2.add(runners.get(a));
            top3Leg2Names.add(runners.get(a).getName());
        }
        
        double minTime = 100000.0;
        List<Runner> chosenBest = new ArrayList<Runner>();
        for (int i = 0; i < runners.size(); i++) {
            Runner[] chosen = new Runner[4];
            if (!top3Leg2Names.contains(runners.get(i).getName())) { // find a runner that is not in top3Leg2
                chosen[0] = runners.get(i);
                String chosenName = chosen[0].getName();

                for (int k = 0; k < 3; k++) {
                    chosen[k+1] = top3Leg2.get(k);
                }

                // Until this point, chosen consist of top3Leg2 guys and one iterated runner.
                
                for (int j = 0; j < 4; j++) { // iterate for every runner who is the first leg runner
                    double time = 0;
                    for (int m = 0; m < 4; m++) {
                        if (m==j) {
                            time += chosen[m].getLeg1();
                        } else {
                            time += chosen[m].getLeg2();
                        }
                    }

                    if (time < minTime) { // we got a better a team!
                        chosenBest.clear();
                        chosenBest.add(chosen[j]);
                        for (int q = 0; q < 4; q++) {
                            if (q != j) {
                                chosenBest.add(chosen[q]); // configure chosenBest from chosen
                            }
                        }
                        minTime = time;
                    }
                }
            }
        }

        writer.println(minTime);
        for (int p = 0; p < 4; p++) {
            writer.println(chosenBest.get(p).getName());
        }

        writer.flush();
    }
}

class Runner {
    public String name;
    public double leg1;
    public double leg2;

    public Runner(String name, double leg1, double leg2) {
        this.name = name;
        this.leg1 = leg1;
        this.leg2 = leg2;
    }

    public String getName() {return name;}
    public double getLeg1() {return leg1;}
    public double getLeg2() {return leg2;}
}

class Leg2Comparator implements Comparator<Runner> {
    public int compare(Runner r1, Runner r2) {
        double param = 1000*(r1.getLeg2()-r2.getLeg2());
        return (int) param;
    }

    public boolean equals(Object obj) {
        return this == obj;
    }
}