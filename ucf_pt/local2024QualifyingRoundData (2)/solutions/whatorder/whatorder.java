// Arup Guha
// 8/2/2024
// Solution to 2024 UCF Locals Qualifying Round Problem: What's the Order Anyway?

import java.util.*;

public class whatorder {

	public static int n;
	public static int nClues;
	public static int[] type;
	public static int[] first;
	public static int[] second;
	
	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		n = stdin.nextInt();
		nClues = stdin.nextInt();
		
		type = new int[nClues];
		first = new int[nClues];
		second = new int[nClues];
		
		// Read in clues.
		for (int i=0; i<nClues; i++) {
			type[i] = stdin.nextInt();
			first[i] = stdin.next().charAt(0) - 'A';
			second[i] = stdin.next().charAt(0) - 'A';
		}
		
		// Set up permutation and solve.
		int[] perm = new int[n];
		boolean[] used = new boolean[n];
		System.out.println(go(perm, used, 0));
	}
	
	public static int go(int[] perm, boolean[] used, int k) {
	
		// Done with the permutation, evaluate it.
		if (k == n) return eval(perm);
		
		int res = 0;
		
		// Try each valid option in slot k, add up all ways to solve it.
		for (int i=0; i<n; i++) {
			if (used[i]) continue;
			used[i] = true;
			perm[k] = i;
			res += go(perm, used, k+1);
			used[i] = false;
		}
		
		// Ta da!
		return res;
	}
	
	// Returns 1 if this permutation is consistent with the clues, false otherwise.
	// perm[i] represents the location of letter i in line. This meaning of perm
	// makes the clues easier to evaluate.
	public static int eval(int[] perm) {
	
		// Go through each clue.
		for (int i=0; i<nClues; i++) {
		
			// If act first[i] comes after second[i], this is invalid.
			if (type[i] == 1) {
				if (perm[first[i]] > perm[second[i]]) return 0;
			}
			// If act first[i] comes before second[i], this is invalid.
			else if (type[i] == 2) {
				if (perm[first[i]] < perm[second[i]]) return 0;
			}
			// Absolute value difference can't be one in placements of acts.
			else {
				if (Math.abs(perm[first[i]]-perm[second[i]]) <= 1) return 0;
			}
		}
		
		// If we make it here, we're good.
		return 1;
	}
}