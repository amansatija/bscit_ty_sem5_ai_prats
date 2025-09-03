import java.util.Scanner;

public class distributive {

    public static void main(String[] args) {
        int a, b, c;
        System.out.println("Enter  number for digits");
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        System.out.println("Distributive Law");
        System.out.println("A*(B*C) = " + (a * (b * c)));
        System.out.println("(A*B)*C) = " + ((a * b) * c));
    }
}