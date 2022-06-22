package Java;

public class arrays1{

    public static void main(String[] args){
        // print the sum of elements of an given array
        int[] arr = {2,4,6,5,7,8,2};
        int sum = 0;
        for(int i=0; i<arr.length; i++){
            sum = sum + arr[i];
        }
        System.out.println(sum);
    }
}