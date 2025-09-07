//
// 2025 UCF Local Programming Contest (Qualifying Round) -- judge
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class judge
{
	public static int num_of_judges;
	public static int num_of_summer_days;
	
	public static int avail_judges_per_day[];

   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  // read the input
	  read_and_init(input);
	  
	  // print the number of days at least 3 judges are available
	  System.out.println( find_avail_day_count() );

   }// end of main()
   
   /* ********************************************************* */
   
   public static void read_and_init(Scanner input)
   {  
	   num_of_judges = input.nextInt();
	   
	   num_of_summer_days = input.nextInt();
	   avail_judges_per_day = new int[num_of_summer_days + 1]; // [0] not used
	   
	   // all judges are initially available every day
	   Arrays.fill(avail_judges_per_day, num_of_judges);
	   
	   // process the days each judge is not available
	   for (int j = 1;  j <= num_of_judges;  ++j)
	   {
		   process_one_judge(input);
	   }
	  
   }// end of read_and_init()
   
   /* ********************************************************* */
   
   public static void process_one_judge(Scanner input)
   {
	   // Process the days a judge is not available.
	   
	   int num_of_vacations = input.nextInt();
	   for (int v = 1;  v <= num_of_vacations;  ++v)
	   {
		   int start_day = input.nextInt();
		   int end_day   = input.nextInt();
		   for (int d = start_day;  d <= end_day;  ++d)
		   {
			   avail_judges_per_day[d] -= 1;
		   }
		   
	   }// end for (v)
	  
   }// end of process_one_judge()
   
   /* ********************************************************* */
   
   public static int find_avail_day_count()
   {
	   // Find the number of days at least 3 judges are available.
	   
	   int count = 0;
	   for (int d = 1;  d <= num_of_summer_days;  ++d)
	   {
		   if (avail_judges_per_day[d] >= 3)
		   {
			   ++count;
		   }
	   }
	   
	   return(count);

   }// end of find_avail_day_count()

   /* ********************************************************* */
 
}// end of class judge

   /* ********************************************************* */
