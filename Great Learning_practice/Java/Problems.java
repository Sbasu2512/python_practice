package Java;

import java.util.ArrayList;
import java.util.Scanner;

public class Problems {
    public static int Problem5(){
        Scanner in = new Scanner(System.in);

        System.out.println("Please enter the numbers:");
        int num1 = in.nextInt();
        int num2 = in.nextInt();
        in.close();
        int sum = num1 + num2 ;
        return sum ;
    }

    public static void Problem6(float num1,float num2){
        float sum,multiply,subs,divide,mod ;

       sum = num1 + num2;
         multiply = num1 * num2;
        if(num1 < num2){
            subs = num2 - num1;
        } else {
            subs = num1 - num2;
        }
        divide = num1/num2;
        mod = num1 % num2;

        ArrayList<Float> result = new ArrayList<Float>();
        result.add(sum);
        result.add(subs);
        result.add(divide);
        result.add(mod);
        result.add(multiply);

        System.out.println(result);

    }

    public static void Problem7(){
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number:");
        int num = in.nextInt();
        in.close();
        int i;
        for(i=0; i<10; i++){
            System.out.println(num + "x" + (i+1) + "=" + num*(i+1));
        }
    }

    public static void main(String[] args) {
        // System.out.println(Problem5());    
        // Problem6(10,12);
        Problem7();
    }
}
