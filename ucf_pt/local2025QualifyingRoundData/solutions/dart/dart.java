//
// 2025 UCF Local Programming Contest (Qualifying Round) -- dart
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class dart
{
	public static int grid_size;
	public static int dart_row;
	public static int dart_col;

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the input
	  grid_size = input.nextInt();
	  dart_row  = input.nextInt();
	  dart_col  = input.nextInt();
	  
	  int bulls_eye = (grid_size + 1) / 2;
	  
	  // find and print the score
	  // score is based on row and column
	  
	  int delta_row = Math.abs(bulls_eye - dart_row);
	  int delta_col = Math.abs(bulls_eye - dart_col);
	  
	  int distance = Math.max(delta_row, delta_col);
	  
	  int score = 100 - (10 * distance);
	  
	  System.out.println(score);
	   
   }// end of main()

   /* ********************************************************* */	
 
}// end of class dart

   /* ********************************************************* */
