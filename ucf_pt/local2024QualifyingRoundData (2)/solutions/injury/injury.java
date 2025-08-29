//
// 2024 UCF Local Programming Contest (Qualifying Round) -- injury
// Ali Orooji
//

import java.util.*;
import java.lang.Math;

public class injury
{	
	public static int num_of_dict_words;
	public static String dictionary[];
	
   /* ********************************************************* */
	
   public static void main(String[] args)
   {
	  Scanner input = new Scanner(System.in);
	  
	  read_and_init(input);
	  process_queries(input);
	   
   }// end of main()

   /* ********************************************************* */
  
   public static void read_and_init(Scanner input)
   {
	   num_of_dict_words = input.nextInt();
	   dictionary = new String[num_of_dict_words + 1]; 
	                         // [0] not used to simplify the code
	   
	   for (int w = 1;  w <= num_of_dict_words;  ++w)
	   {
		   dictionary[w] = input.next();
		   // System.out.println(dictionary[w]);
		   
	   }// end for (w)
	  
   }// end of read_and_init()
  
   /* ********************************************************* */
	
   public static void process_queries(Scanner input)
   {
	  int num_of_typed_words = input.nextInt();
	  for (int w = 1;  w <= num_of_typed_words;  ++w)
	  {
		  String typed_word = input.next();
		  // System.out.println("typed_word = " + typed_word);
		  
		  System.out.println( check_typed_word(typed_word) );
		  
	  }// end for (w)
	   
   }// end of process_queries()

   /* ********************************************************* */
	
   public static int check_typed_word(String typed_word)
   {
	  // check to see if the typed_word is in the dictionary
	  for (int w = 1;  w <= num_of_dict_words;  ++w)
	  {
		  if (dictionary[w].compareTo(typed_word) == 0)
		  {
			  return(1);
		  }
	  }// end for (w)
		  
	  // check to see if the typed_word is a concatenation of two words
	  for (int w1 = 1;  w1 <= num_of_dict_words;  ++w1)
	  {
		  for (int w2 = 1;  w2 <= num_of_dict_words;  ++w2)
		  {
			  String concat_word = dictionary[w1].concat(dictionary[w2]);
			  if (concat_word.compareTo(typed_word) == 0)
			  {
				  return(2);
			  }
		  }// end for (w2)

	  }// end for (w1)
		  
	  // the typed_word is not in the dictionary and it is not a
	  // concatenation of two dictionary words either
	  return(0);
	   
   }// end of check_typed_word()

   /* ********************************************************* */
 
}// end of class injury

   /* ********************************************************* */
