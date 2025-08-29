// Arup Guha
// 8/12/2024
// Alternate Solution to 2024 UCF Qualification Problem: Weekend Gardening

import java.util.*;

public class weekend {

	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		long low = stdin.nextLong();
		long high = stdin.nextLong();
		
		// Get prices.
		long[] prices = new long[3];
		for (int i=0; i<3; i++)
			prices[i] = stdin.nextLong();
			
		// Quantities.
		int[] q = new int[3];
		for (int i=0; i<3; i++)
			q[i] = stdin.nextInt();
			
		// Set up DP, dp[i][j][k] is probability of having i cheap, j medium and k expensive
		// plants.
		double[][][] dp = new double[q[0]+1][q[1]+1][q[2]+1];
		
		// We mark end states here (where we are in range...)
		boolean[][][] end = new boolean[q[0]+1][q[1]+1][q[2]+1];
		
		// Initialize...
		dp[0][0][0] = 1;
		double res = 0;
		
		// i cheap plants, j mid plants, k expensive plants.
		for (int i=0; i<=q[0]; i++) {
			for (int j=0; j<=q[1]; j++) {
				for (int k=0; k<=q[2]; k++) {
					
					// We did this already.
					if (i==0 && j == 0 && k == 0) continue;
			
					long curCost = i*prices[0] + j*prices[1] + k*prices[2];
					
					// None of these states are worth reaching.
					if (curCost > high) break;
					
					// Mark this now.
					if (curCost >= low) end[i][j][k] = true;
					
					// Total plants left...
					int left = (q[0] - i) + (q[1] - j) + (q[2] - k) + 1;
					
					// Start at 0.
					dp[i][j][k] = 0;
					
					// Probability we pick up a cheap plant now.
					if (i>0 && !end[i-1][j][k]) dp[i][j][k] += 1.0*(q[0]-i+1)/left*dp[i-1][j][k];
					
					// Medium plant.
					if (j>0 && !end[i][j-1][k]) dp[i][j][k] += 1.0*(q[1]-j+1)/left*dp[i][j-1][k];
					
					// Expensive plant.
					if (k>0 && !end[i][j][k-1]) dp[i][j][k] += 1.0*(q[2]-k+1)/left*dp[i][j][k-1];
					
					// End state so add it.
					if (end[i][j][k]) res += dp[i][j][k];
				}
			}
		}
		
		// Ta da!
		System.out.printf("%.12f\n",res);
	}
}