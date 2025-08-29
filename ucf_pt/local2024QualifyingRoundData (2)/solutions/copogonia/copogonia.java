// Arup Guha
// 8/2/2024
// Solution to 2024 UCF Locals Qualifier Problem: Copogonia

import java.util.*;

public class copogonia {

	// Variables for points and max distance.
	public static int n;
	public static int[] x;
	public static int[] y;
	public static int maxD;
	public static double[][] origadj;
	
	// Variables for the roads to add.
	public static int numR;
	public static int[] costs;
	public static int[] u;
	public static int[] v;
	public static double[] rDist;
	
	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		n = stdin.nextInt();
		numR = stdin.nextInt();
		maxD = stdin.nextInt();

		// Get points.
		x = new int[n];
		y = new int[n];
		for (int i=0; i<n; i++) {
			x[i] = stdin.nextInt();
			y[i] = stdin.nextInt();
		}
		
		// Set up original adjacency matrix.
		origadj = new double[n][n];
		for (int i=0; i<n; i++) {
			Arrays.fill(origadj[i], 1000000000);
			origadj[i][i] = 0;
		}
		
		// Fill in each road cost.
		for (int i=0; i<n; i++) {
			double road = dist(i, (i+1)%n);
			origadj[i][(i+1)%n] = road;
			origadj[(i+1)%n][i] = road;
		}
		
		// Now we get all the new roads we could build.
		costs = new int[numR];
		u = new int[numR];
		v = new int[numR];
		rDist = new double[numR];
		for (int i=0; i<numR; i++) {
			u[i] = stdin.nextInt()-1;
			v[i] = stdin.nextInt()-1;
			costs[i] = stdin.nextInt();
			rDist[i] = dist(u[i], v[i]);
		}
		
		// Will store all costs here.
		int[] totalcosts = new int[1<<numR];
		int res = 2000000000;
		
		// Try building each subset of roads.
		for (int mask=0; mask<(1<<numR); mask++) {
		
			// Fill in cost of this mask.
			if (mask > 0) {
				
				// Find least significant bit on.
				int lsb = 0;
				while ((mask & (1<<lsb)) == 0) lsb++;
			
				// Cost for this subset.
				totalcosts[mask] = totalcosts[mask-(1<<lsb)] + costs[lsb];
			}
			
			// Create the adjacency matrix for this subset of roads.
			double[][] adj = getMat(mask);
			
			// Get all pairs shortest distances.
			floyd(adj);
			
			// Find max entry.
			double mymax = getMax(adj);
			
			// See if this is good enough, if so, update least cost if necessary.
			if (mymax <= maxD+1e-9)
				res = Math.min(res, totalcosts[mask]); 
		}
		
		// Ta da!
		System.out.println(res);
	}
	
	// Returns the distance between vertices i and j.
	public static double dist(int i, int j) {
		return Math.sqrt( (x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) );
	}
	
	// Returns the adjacency matrix corresponding to this mask.
	public static double[][] getMat(int mask) {
	
		// Just copy the old one.
		double[][] adj = new double[n][n];
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				adj[i][j] = origadj[i][j];
				
		// Add in these roads.
		for (int i=0; i<numR; i++) {
			if ((mask &(1<<i)) != 0) {
				adj[u[i]][v[i]] = rDist[i];
				adj[v[i]][u[i]] = rDist[i];
			}
		}
		
		return adj;
	}
	
	// Runs Floyd's on the graph with the adjacency matrix adj.
	public static void floyd(double[][] adj) {
		for (int k=0; k<adj.length; k++)
			for (int i=0; i<adj.length; i++)
				for (int j=0; j<adj.length; j++)
					adj[i][j] = Math.min(adj[i][j], adj[i][k]+adj[k][j]);
	}
	
	// Returns max entry in adj.
	public static double getMax(double[][] adj) {
		double res = 0;
		for (int i=0; i<adj.length; i++)
			for (int j=0; j<adj.length; j++)
					res = Math.max(res, adj[i][j]);
		return res;
	}
	
}