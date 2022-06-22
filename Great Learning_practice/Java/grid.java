package Java;

public class grid {
    public static void main(String[] args){
        int [][] a = new int[10][10];
        //print a grid - w3 reasource Q3.
        for(int r=0; r<10; r++)
        {
            // System.out.print("-");
            for(int c=0; c<10; c++){
                System.out.printf("%2d",a[r][c]);
            }
            System.out.println();
        }
    }
}
