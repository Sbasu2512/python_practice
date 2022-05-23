package Java;

public class Area {
    public static double circleArea(int radius){
        final double pi = 3.14;
        double area = pi*(radius*radius);
        return area;
    }
    public static void main(String[] args){
        System.out.print(circleArea(5));; 
    }
}
