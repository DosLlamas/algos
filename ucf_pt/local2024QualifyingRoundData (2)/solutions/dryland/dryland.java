// Arup Guha
// 8/12/2024
// Alternate Solution to UCF 2024 Qualification Problem: Dryland

import java.util.*;

public class dryland {
	
	public static int[][] grid;

	public static void main(String[] args) {
	
		Scanner stdin = new Scanner(System.in);
		int r = stdin.nextInt();
		int c = stdin.nextInt();
		
		// Read in grid.
		grid = new int[r+1][c+1];
		for (int i=1; i<=r; i++) {
			String tmp = stdin.next();
			for (int j=1; j<=c; j++)
				grid[i][j] = tmp.charAt(j-1) - '0';
		}
		
		// Cumulative frequency by rows.
		for (int i=1; i<=r; i++)
			for (int j=1; j<=c; j++)
				grid[i][j] += grid[i][j-1];
				
		// Cumulative frequency by cols.
		for (int j=1; j<=c; j++)
			for (int i=1; i<=r; i++)
				grid[i][j] += grid[i-1][j];
				
		int res = 0;
		
		// (i,j) is potential starting top left.
		for (int i=1; i<=r; i++) {
			for (int j=1; j<=c; j++) {
			
				// Extend on this row while we have ones.
				int rJ = j;
				while (rJ <= c && rJ - j + 1 == area(i,j,i,rJ)) rJ++;
				rJ--;
				
				// We can skip checking if this square's 0.
				if (rJ < j) continue;
				
				// Rectangle on this row.
				res = Math.max(res, rJ-j+1);
				
				// Advance our row.
				for (int rI = i+1; rI<=r; rI++) {
					
					// Go back on this row until we have a full rectangle.
					while (rJ>=j && area(i,j,rI,rJ) != (rI-i+1)*(rJ-j+1)) rJ--;
					
					if (rJ < j) break;
				
					// Update if necessary.
					res = Math.max(res, (rI-i+1)*(rJ-j+1));
				}
			}
		}
		
		// Ta da!
		System.out.println(res);
	}
	
	// Returns the area of rectangle with top left corner (x1,y1) bottom right corner (x2,y2)
	// Coordinates are inclusive.
	public static int area(int x1, int y1, int x2, int y2) {
		return grid[x2][y2] - grid[x2][y1-1] - grid[x1-1][y2] + grid[x1-1][y1-1];
	}		
}