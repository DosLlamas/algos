// Arup Guha
// 8/12/2024
// Alternate Solution to UCF 2024 Qualification Problem: Picture Caption

import java.util.*;

public class picap {

	public static int n;
	public static int k;
	public static int[] len;
	
	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		n = stdin.nextInt();
		k = stdin.nextInt();
		len = new int[n];
		
		// Read numbers.
		int tot = 0;
		for (int i=0; i<n; i++) {
			len[i] = stdin.nextInt();
			tot += len[i];
		}
			
		// Take all the letters and add n spaces, this is good enough for high.
		int low = 1, high = tot+n;
		
		// Run binary search on line length.
		while (low < high) {
		
			int mid = (low+high)/2;

			// We can do mid...
			if (canDo(mid))
				high = mid;
				
			// Can't do it, must try longer.
			else
				low = mid+1;
		}
		
		// Ta da!
		System.out.println(low);
	}
	
	// Returns true iff we can fit everything with maxCol # of columns.
	public static boolean canDo(int maxCol) {
	
		int lineNo = 0, idx = 0;
		
		// Go through each word.
		while (idx < n) {
		
			// Place the first word on this line.
			int curLen = len[idx++];
			if (curLen > maxCol) return false;
			
			// Now continue placing words as long as we can.
			while (idx<n && curLen + len[idx] < maxCol) {
				curLen += (1 + len[idx]);
				idx++;
			}
			
			// New line count.
			lineNo++;
			
			// If we've run out of lines, we can decide the answer.
			if (lineNo == k) return idx == n;
		}
		
		// If we get here, we can do it.
		return true;
	}
}