package Java;

public class average {
    public static void main(String[] args){
        // find average of an array
        int [] arr = {20, 30, 25, 35, 16, 60, 100} ;
        int length = arr.length ;
        //find sum
        int sum = 0;
        for (int i=0; i<length; i++){
            sum = sum + arr[i];
        }
        double average = sum/length;
        System.out.println(average);
    }
}
