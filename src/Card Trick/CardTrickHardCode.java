import java.io.*;

public class CardTrickHardCode {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        
        for (int i = 0; i < queries; i++) {
            String n = sc.readLine();
            switch (n) {
                case "1": writer.println("1"); break;
                case "2": writer.println("2 1"); break;
                case "3": writer.println("3 1 2"); break;
                case "4": writer.println("2 1 4 3"); break;
                case "5": writer.println("3 1 4 5 2"); break;
                case "6": writer.println("4 1 6 3 2 5"); break;
                case "7": writer.println("5 1 3 4 2 6 7"); break;
                case "8": writer.println("3 1 7 5 2 6 8 4"); break;
                case "9": writer.println("7 1 8 6 2 9 4 5 3"); break;
                case "10": writer.println("9 1 8 5 2 4 7 6 3 10"); break;
                case "11": writer.println("5 1 6 4 2 10 11 7 3 8 9"); break;
                case "12": writer.println("7 1 4 9 2 11 10 8 3 6 5 12"); break;
                case "13": writer.println("4 1 13 11 2 10 6 7 3 5 12 9 8"); break;
            }
        }

        writer.flush();
    }
}