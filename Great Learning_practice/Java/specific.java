package Java;

public class specific {
    public static void contains(int[] arr, int target){
        for(int i =0; i<arr.length; i++){
            if(arr[i] == target){
                System.out.println("Element found at index: " + i);
                return;
            } 
        }
        System.out.println("Element not found");
    }
    public static void main(String[] args){
        //Write a Java program to test if an array contains a specific value
        // return ;
        int[] arr = {
            1789, 2035, 1899, 1456, 2013, 
            1458, 2458, 1254, 1472, 2365, 
            1456, 2265, 1457, 2456};
        contains(arr, 1254);
        contains(arr, 3082);
    }
}
