package Java;

public class triangle {
    public static void main(String[] args){
        int [][] arr = new int[5][5];
    for(int r=0; r<arr.length; r++){
        for(int c=0; c<r; c++){
            System.out.printf("%2d", arr[r][c]);
        }
        System.out.println();
    }
    }
}
