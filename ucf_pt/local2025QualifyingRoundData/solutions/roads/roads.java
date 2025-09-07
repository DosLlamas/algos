// Arup Guha
// 7/29/2025
// Solution to 2025 UCF Locals Qualifying Problem: Country Roads

import java.util.*;
import java.io.*;

public class roads {

	public static void main(String[] args) throws Exception {
	
		// Get basic input.
		FastScanner stdin = new FastScanner(System.in);
		int n = stdin.nextInt();
		int numRoads = stdin.nextInt();
		int numAdd = stdin.nextInt();
		
		// Process current edges - merge sets...
		djset dj = new djset(n);
		for (int i=0; i<numRoads; i++) {
			int u = stdin.nextInt()-1;
			int v = stdin.nextInt()-1;
			dj.union(u, v);
		}
		
		// Read edges and sort.
		ArrayList<edge> edges = new ArrayList<edge>();
		for (int i=0; i<numAdd; i++) {
			int u = stdin.nextInt()-1;
			int v = stdin.nextInt()-1;
			int w = stdin.nextInt();
			edges.add(new edge(u,v,w));
		}
		Collections.sort(edges);
		
		// Decided not to pull the long trick...
		// Answer can't be more than 1 billion...
		int res = 0;
		
		// How many trees we have. Guaranteed to be at least 2.
		int curGroups = dj.numTrees;
		
		// Go through all the edges in order.
		for (int i=0; i<numAdd; i++) {
			
			// Try adding this one.
			edge cur = edges.get(i);
			boolean merged = dj.union(cur.u, cur.v);
			
			if (!merged) continue;
			
			// Add cost update groups.
			res += cur.w;
			curGroups--;
			
			// We're connected.
			if (curGroups == 1) break;
		}
		
		// Ta da!
		System.out.println(res);
	}
}

/*** Just to sort edges. ***/
class edge implements Comparable<edge> {
	
	public int u;
	public int v;
	public int w;
	
	public edge(int myu, int myv, int myw) {
		u = myu;
		v = myv;
		w = myw;
	}
	
	public int compareTo(edge other) {
		if (this.w != other.w)
			return this.w - other.w;
		if (this.u != other.u)
			return this.u - other.u;
		return this.v - other.v;
	}
}

/*** Disjoint Set Class with path compression. ***/
class djset {

	public int[] par;
	public int numTrees;
	
	public djset(int n) {
		par = new int[n];
		for (int i=0; i<n; i++)
			par[i] = i;
		numTrees = n;
	}
	
	public int find(int u) {
		if (par[u] == u) return u;
		return par[u] = find(par[u]);
	}
	
	public boolean union(int u, int v) {
		u = find(u);
		v = find(v);
		if (u == v) return false;
		par[v] = u;
		numTrees--;
		return true;
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