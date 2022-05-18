package Java;

public class HelloWorld {
    public static void String(){
        String a = "Hello World!";

        System.out.println(a);
    }

    public static void Integers(){
        int a = 2 ;
        int b = 4 ;
    
        System.out.println(a);
        System.out.println(b);
    }
    
    public static void Float(){
        float a = (float)999.99 ;  
        
        System.out.println(a);
    }

    public static void character(){
        char a = 'a';

        System.out.println(a);
    }

    public static void Boolean(){
        boolean a = true;

        System.out.println(a);
    }

    public static void main(String[] args) {
        String();
        Integers();
        Float();
        character();
        Boolean();
    }
}