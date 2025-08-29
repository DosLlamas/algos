//
// 2024 UCF Local Programming Contest (Qualifying Round) -- dozen
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class dozen
{
	public static int apples_per_bag;
	public static int num_of_bags;
	public static int price_per_dozen;
	
	public static int total_apple_count;
	public static int dozens_purchased;

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the shopping info and compute total apple count
	  apples_per_bag = input.nextInt();
	  num_of_bags    = input.nextInt();
	  total_apple_count = apples_per_bag * num_of_bags;
	  
	  // find how many dozens
	  if ( (total_apple_count % 12) == 0 )
		  dozens_purchased = total_apple_count / 12;
	  else
		  dozens_purchased = (total_apple_count / 12) + 1;
	  
	  /* Note: dozens_purchased can be computed without using the mod (%) 
	           operator as follows:
			   dozens_purchased = (total_apple_count + 11) / 12;
	  */
	  
	  // read price per dozen and print total cost
	  price_per_dozen = input.nextInt();
	  System.out.println( dozens_purchased * price_per_dozen );
	   
   }// end of main()

   /* ********************************************************* */
 
}// end of class dozen

   /* ********************************************************* */
