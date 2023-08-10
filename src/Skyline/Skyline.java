import java.awt.*;
import java.awt.geom.*;
import java.io.*;
import java.util.*;

public class Skyline {
    public static double getArea(Area area) {
        PathIterator pathIterator = area.getPathIterator(null);
        double[] coords = new double[6];
        double areaSum = 0.0;
        double lastX = 0.0, lastY = 0.0;
        while (!pathIterator.isDone()) {
            int type = pathIterator.currentSegment(coords);
            switch (type) {
                case PathIterator.SEG_MOVETO:
                    lastX = coords[0];
                    lastY = coords[1];
                    break;
                case PathIterator.SEG_LINETO:
                    areaSum += (lastX + coords[0]) * (lastY - coords[1]);
                    lastX = coords[0];
                    lastY = coords[1];
                    break;
                case PathIterator.SEG_CLOSE:
                    break;
            }
            pathIterator.next();
        }
        return Math.abs(areaSum) * 0.5;
    }
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();
        int t = fio.nextInt();
        Area[] aa = new Area[t];
        while (t-- > 0) {
            Polygon p = new Polygon();
            int x1 = fio.nextInt();
            int y1 = fio.nextInt();
            int x2 = fio.nextInt();
            int y2 = fio.nextInt();
            p.addPoint(x1, 0);
            p.addPoint(x1, y1);
            p.addPoint(x2, y2);
            p.addPoint(x2, 0);
            aa[t] = new Area(p);
        }
        double[] ans = new double[aa.length];
        for (int i = 0; i < aa.length; i++) {
            Area a = (Area) aa[i].clone();
            for (int j = i+1; j < aa.length; j++) a.subtract(aa[j]);
            ans[aa.length-1-i] = getArea(a)/getArea(aa[i]);
        }
        for (double d : ans) {
            fio.println(d);
        }
        fio.close();
    }
}

class FastIO extends PrintWriter { 
    BufferedReader br; 
    StringTokenizer st;

    public FastIO() { 
        super(new BufferedOutputStream(System.out)); 
        br = new BufferedReader(new InputStreamReader(System.in));
    } 

    String next() { 
        while (st == null || ! st.hasMoreElements()) { 
            try { st = new StringTokenizer(br.readLine()); } 
            catch (IOException  e) { e.printStackTrace(); } 
        } 
        return st.nextToken(); 
    } 

    int nextInt() { return Integer.parseInt(next()); } 
    long nextLong() { return Long.parseLong(next()); } 
    double nextDouble() { return Double.parseDouble(next()); } 

    String nextLine() { 
        String str = ""; 
        try { str = br.readLine(); } 
        catch (IOException e) { e.printStackTrace(); } 
        return str; 
    } 
}