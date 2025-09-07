// Arup Guha
// 8/1/2025
// Solution to 2025 UCF Locals Qualifying Problem: World Population

import java.util.*;
import java.io.*;

public class people {

	public static void main(String[] args) throws Exception {
	
		// Get basic input.
		FastScanner stdin = new FastScanner(System.in);
		int n = stdin.nextInt();
		
		// Set up bit with initial values.
		bit mine = new bit(n);
		for (int i=1; i<=n; i++) {
			long tmp = stdin.nextLong();
			mine.add(i, tmp);
		}
		
		StringBuffer sb = new StringBuffer();
		int nQ = stdin.nextInt();
		
		// Process queries.
		for (int i=0; i<nQ; i++) {
		
			// Get command.
			char cmd = stdin.next().charAt(0);
			
			// Query.
			if (cmd == 'R') {
				int lo = stdin.nextInt();
				int hi = stdin.nextInt();
				sb.append(mine.sum(lo,hi)+"\n");
			}
			
			// Update.
			else {
				int idx = stdin.nextInt();
				long v = stdin.nextLong();
				mine.add(idx, v);
			}
		}
		
		// Ta da!
		System.out.print(sb);
	}
}

/*** Binary Index Tree ***/
class bit {

	public long[] val;
	
	public bit(int n) {
		val = new long[n+1];
	}
	
	public void add(int idx, long v) {
		while (idx < val.length) {
			val[idx] += v;
			idx += ((-idx)&idx);
		}
	}
	
	public long sum(int x) {
		long res = 0;
		while (x > 0) {
			res += val[x];
			x -= (x&(-x));
		}
		return res;
	}
	
	public long sum(int lo, int hi) {
		return sum(hi) - sum(lo-1);
	}
}

/*** To speed up reading input. ***/
class FastScanner {
	BufferedReader br;
	StringTokenizer st;
	public FastScanner(InputStream i){
		br = new BufferedReader(new InputStreamReader(i));
		st = new StringTokenizer("");
	}
	public String next() throws IOException{
		if(st.hasMoreTokens())
			return st.nextToken();
		else
			st = new StringTokenizer(br.readLine());
		return next();
	}
	public int nextInt() throws IOException{
		return Integer.parseInt(next());
	}
	public long nextLong() throws IOException{
		return Long.parseLong(next());
	}
	public double nextDouble() throws IOException{
		return Double.parseDouble(next());
	}
}