// Arup Guha
// 7/30/2025
// Solution to 2025 UCF Locals Qualifying Question: Who Wants to be a Millionaire?

import java.util.*;

public class millionaire {

	public static void main(String[] args) {
	
		// Get basic input.
		Scanner stdin = new Scanner(System.in);
		int n = stdin.nextInt();
		int[] money = new int[n+1];
		for (int i=1; i<=n; i++)
			money[i] = stdin.nextInt();
			
		// My probabilities.
		double[] myProb = new double[n];
		for (int i=0; i<n; i++)
			myProb[i] = stdin.nextDouble();
			
		// The ones for the experts.
		double[] expertProb = new double[n];
		for (int i=0; i<n; i++)
			expertProb[i] = stdin.nextDouble();
			
		// Set up DP array.
		// dp[i][j] = expected money if we are currently
		// listening to question i and we have j "ask the expert"
		// options left.
		double[][] dp = new double[n+1][3];
		
		// This means we won...
		for (int i=0; i<3; i++)
			dp[n][i] = money[n];
			
		// We have to fill this out backwards.	
		for (int i=n-1; i>=0; i--) {
		
			// j is # of ask experts left.
			for (int j=0; j<3; j++) {
		
				// If I stop.
				double cur = money[i];
				
				// If I go but don't use the expert.
				double alt1 = myProb[i]*dp[i+1][j];
				
				// If I go and use the expert; I need to have that option left.
				double alt2 = j>0 ? expertProb[i]*dp[i+1][j-1] : 0;
				
				// Just take the best of the options.
				dp[i][j] = Math.max(cur, Math.max(alt1, alt2));
			}
		}
		
		// Ta da!
		System.out.printf("%.9f\n",dp[0][2]);
	}
}