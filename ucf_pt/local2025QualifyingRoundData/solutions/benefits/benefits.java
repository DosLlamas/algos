//
// 2025 UCF Local Programming Contest (Qualifying Round) -- benefits
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class benefits
{
	public static int age1;
	public static int amount1;
	
	public static int age2;
	public static int amount2;
	
	public static int age3;

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the input
	  read_and_init(input);
	  // print the better option
	  System.out.println( find_better_option() );

   }// end of main()
   
   /* ********************************************************* */
   
   public static void read_and_init(Scanner input)
   {  
	   age1    = input.nextInt();
	   amount1 = input.nextInt();
	   
	   age2    = input.nextInt();
	   amount2 = input.nextInt();
	   
	   age3    = input.nextInt();
	  
   }// end of read_and_init()
   
   /* ********************************************************* */
   
   public static int find_better_option()
   {
	   // Find the better option.
	   
	   int total1 = (age3 - age1) * amount1;
	   int total2 = (age3 - age2) * amount2;
	   
	   if (total1 >= total2)
	   {
		   return(1);
	   }
	   else
	   {
		   return(2);
	   }

   }// end of find_better_option()

   /* ********************************************************* */
 
}// end of class benefits

   /* ********************************************************* */
