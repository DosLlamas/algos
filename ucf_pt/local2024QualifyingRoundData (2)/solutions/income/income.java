// Arup Guha
// 8/12/2024
// Alternate Solution to UCF 2024 Qualification Problem: Income Inequality

import java.util.*;

public class income {

	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		int n = stdin.nextInt();
		
		// Read numbers.
		ArrayList<Long> vals = new ArrayList<Long>();
		long tot = 0;
		for (int i=0; i<n; i++) {
			long tmp = stdin.nextLong();
			tot += tmp;
			vals.add(tmp);
		}
		
		// Sort in reverse order.
		Collections.sort(vals);
		Collections.reverse(vals);
		double res = 0;
		long curT = 0;
		
		// Try each split of the i+1 richest people.
		for (int i=0; i<n; i++) {
			curT += vals.get(i);
			double tmp = (double)curT/tot - 1.0*(i+1)/n;
			res = Math.max(res, 100*tmp);
		}
		
		// Ta da!
		System.out.println(res);
	}
}