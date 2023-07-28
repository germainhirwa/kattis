import java.io.*;

public class CardTrick2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        
        for (int i = 0; i < queries; i++) {
            int n = Integer.parseInt(sc.readLine());
            CardQueue q = new CardQueue(n);

            for (int j = 0; j < n; j++) {
                q.enqueue(j);
            }

            int[] result = new int[n];

            for (int k = 1; k <= n; k++) {
                for (int l = 0; l < k; l++) {
                    q.enqueue(q.dequeue());
                }
                result[q.dequeue()] = k;
            }

            for (int m = 0; m < n-1; m++) {
                writer.print(result[m]);
                writer.print(" ");
            }
            writer.println(result[n-1]);
        }

        writer.flush();
    }
}

class CardQueue {
	public int[] arr;
	public int front, back;
	public int capacity;

	public CardQueue(int c) {
		arr = new int[c+1];
		front = 0;
		back = 0;
		capacity = c+1;
	}

	public boolean empty() { 
		return (front == back); 
	}

	public Integer peek() {
		if (empty()) return null;
		else return arr[front];
	}

	public Integer dequeue() {
		if (empty()) return null;
		Integer item = arr[front];
		front = (front + 1) % capacity;
		return item;
	}

	public void enqueue(Integer item) {
		arr[back] = item;
		back = (back + 1) % capacity;
	}
}