//
// 2025 UCF Local Programming Contest (Qualifying Round) -- tourney
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class tourney
{	
	public static int num_of_teams;

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the input
	  num_of_teams = input.nextInt();
	  
	  // print the preliminary count
	  System.out.println( find_prelim() );
	   
   }// end of main()

   /* ********************************************************* */
   
   public static int find_prelim()
   {
	   // Find the preliminary count.
	   
	   int count = 2;
	   while (true)
	   {
		   if (count == num_of_teams)
		   {
			   return(0);
		   }
		   
		   if ((count * 2) > num_of_teams)
		   {
			   return((num_of_teams - count) * 2);
		   }
		   
		   count *= 2;
		   
	   }// end while (true)

   }// end of find_prelim()

   /* ********************************************************* */
 
}// end of class tourney

   /* ********************************************************* */
