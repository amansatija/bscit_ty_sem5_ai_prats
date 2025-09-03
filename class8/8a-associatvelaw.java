
import java.util.Scanner;

public class associatelaw {

    public static void main(String[] args) {
        int a, b, c;
        System.out.println("Enter  number for digits");
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();

        b = sc.nextInt();
        c = sc.nextInt();
        System.out.println("Associate Law");
        System.out.println("A+(B+C) = " + (a + (b + c)));
        System.out.println("A+(B+C) = " + ((a + b) + c));
    }
}