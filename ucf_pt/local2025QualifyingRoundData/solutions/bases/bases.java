//
// 2025 UCF Local Programming Contest (Qualifying Round) -- bases
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class bases
{	
	public static String num1_str;
	public static int num1;
	public static int base1;
	
	public static String num2_str;
	public static int num2;
	public static int base2;
	
	public static int sum;

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the input
	  num1_str = input.next();
	  num2_str = input.next();
	  sum = input.nextInt();
	  
	  // find the two bases
	  find_two_bases();
	  
	  System.out.println(base1 + " " + base2);
	   
   }// end of main()

   /* ********************************************************* */
   
   public static void find_two_bases()
   {
	   // Find the two bases.
	   
	   // find the minumum value for each base
	   int min_base1 = find_min_base(num1_str);
	   int min_base2 = find_min_base(num2_str);
	   
	   for (base1 = min_base1;  base1 <= 10;  ++base1)
	   {
		   num1 = Integer.parseInt(num1_str, base1);
		   for (base2 = min_base2;  base2 <= 10;  ++base2)
		   {
			   num2 = Integer.parseInt(num2_str, base2);
			   if (sum == (num1 + num2))
			   {
				   // found the two bases
				   return;
			   }
			   
		   }// end for (base2)
		   
	   }// end for (base1)
		   
	   System.out.println("*** find_two_bases: shouldn't get to here! ***");

   }// end of find_two_bases()

   /* ********************************************************* */
   
   public static int find_min_base(String num_str)
   {
	   // Find the largest digit in num_str; this determines the
	   // minimum a base can be.
	   
	   for (int k = 9;  k >= 0;  --k)
	   {
		   char ch = (char) (k + '0');
		   if (num_str.indexOf(ch) >= 0)
		   {
			   // num_str contains digit k
			   return(k + 1);
		   }
		   
	   }// end for (k)
		   
	   System.out.println("*** find_min_base: shouldn't get to here! ***");
	   return(-1);

   }// end of find_min_base()
 	 	 
   /* ********************************************************* */	
 
}// end of class bases

   /* ********************************************************* */
