// Arup Guha
// 7/26/2205
// Solution to UCF Local Qualifying Contest Problem: Judge Meetings

import java.util.*;

public class judge {

	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		int nJudge = stdin.nextInt();
		int nDays = stdin.nextInt();
		
		// Assume everyone is there every day at first.
		int[] freq = new int[nDays];
		Arrays.fill(freq, nJudge);
		
		// Process vacations.
		for (int i=0; i<nJudge; i++) {
		
			// Process each vacation.
			int nVac = stdin.nextInt();
			for (int j=0; j<nVac; j++) {
			
				// Get start and end, make 0 based.
				int s = stdin.nextInt()-1;
				int e = stdin.nextInt()-1;
				
				// Subtract one judge from each of these days.
				for (int k=s; k<=e; k++)
					freq[k]--;
			} // end j
		} //end i - for judges.
		
		// Count all days with 3 or more judges.
		int res = 0;
		for (int i=0; i<freq.length; i++)
			if (freq[i] >= 3)
				res++;
				
		// Ta da!
		System.out.println(res);
	}
}