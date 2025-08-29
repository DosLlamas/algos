//
// 2024 UCF Local Programming Contest (Qualifying Round) -- basket
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class basket
{	
	public static int one_pointer;
	public static int two_pointer;
	public static int three_pointer;
	
	public static int score1;
	public static int score2;
	
   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  score1 = read_stat_compute_score(input);
	  score2 = read_stat_compute_score(input);
	  
	  System.out.println( find_result() );
	   
   }// end of main()

   /* ********************************************************* */
  
   public static int read_stat_compute_score(Scanner input)
   {
	   one_pointer   = input.nextInt();
	   two_pointer   = input.nextInt();
	   three_pointer = input.nextInt();
	   
	   int total = (1 * one_pointer) + (2 * two_pointer) + (3 * three_pointer);
	   
	   return(total);
	  
   }// end of read_stat_compute_score()
  
   /* ********************************************************* */
	
   public static int find_result()
   {
	  if (score1 > score2)
		  return(1);
	  
	  if (score2 > score1)
		  return(2);
	  
	  // neither team won
	  return(0);

   }// end of find_result()

   /* ********************************************************* */
 
}// end of class basket

   /* ********************************************************* */
