/** Nylah Belk **/
import java.util.Scanner;

public class CMSC401_A0{
    public static void main(String[] args){
        // import scanner
        Scanner sc = new Scanner(System.in);
         // read in the value associated with line numbers
        String count = sc.nextLine();
        // trim any leading or trailing spaces
        count = count.trim();
        
        try {
            // convert count value to an integer
            int c = Integer.valueOf(count);
            // an empty array to store the sums, with the length of c
            int[] sums = new int[c];
            // a for loop to read in each line
            for (int i = 0; i < c; i++){
                String line = sc.nextLine();
                // split the read in line by space(s)
                String[] numbers = line.trim().split("\\s+");
                // an empty array to store numercial forms of numbers string
                int[] num = new int[numbers.length];
                // convert the numbers array to integers
                for (int j = 0; j < numbers.length; j++){
                    num[j] = Integer.valueOf(numbers[j]);
                }
                // identify the x,y values for the array positions to be summed
                int first = num[num.length - 2];
                int second = num[num.length - 1];
                // sum the values in the x, y positions
                int sum = num[first] + num[second];
                // add each sum to the array at their given line
                sums[i] = sum;
            }
            // print each sum value in order, separated by a line
            for (int i = 0; i < sums.length; i++){
                System.out.println(sums[i]);
            }
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter integers only.");
        }    sc.close();
    }
}