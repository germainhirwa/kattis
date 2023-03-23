import java.io.*;
import java.util.*;

public class DelimiterSoup {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        boolean balanced = true;
        
        int L = Integer.parseInt(sc.readLine());
        StackArr stack = new StackArr(L);
        String line = sc.readLine();
        for (int i = 0; i < L; i++) {
            if (line.charAt(i) == '(' || line.charAt(i) == '[' || line.charAt(i) == '{') {
                stack.push(line.charAt(i));
            } else if (!(line.charAt(i) == ' ')) {
                if (Math.round((stack.peek()+1)/2) != Math.round((line.charAt(i)+1)/2)-1) { // Opening and its respective brackets ASCII value differ either 1 or 2
                    writer.print(line.charAt(i));
                    writer.print(" ");
                    writer.print(i);
                    writer.flush();
                    return;
                } else {
                    stack.pop();
                }
            }
        }

        writer.print("ok so far");
        writer.flush();
    }
}

class StackArr {
	public char[] arr;
	public int top;
	public int capacity;

	public StackArr(int size) {
		arr = new char[size];
		top = -1;
		capacity = size;
	}

	public boolean empty() { 
		return (top < 0); 
	}

	public Character peek() {
		if (!empty()) 
		    return arr[top];
		return ' '; // ASCII 32, guarantees difference with other brackets
	}

	public Character pop() {
		Character item = peek();
		if (item != null)
		    top--;
		return item;
	}

	public void push(Character item) { // no need to enlarge
		top++;
		arr[top] = item;
	}
}
