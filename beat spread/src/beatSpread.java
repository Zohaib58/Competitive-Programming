import java.util.Scanner;

public class beatSpread {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        

        int intValue = sc.nextInt();

        for (int i = 0; i < intValue; i++)
        {
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();

            if ((num1 < 0 || num2 < 0) || (num1 < num2) || ((num2 + num1) % 2 != 0))
            {
                System.out.println("impossible");
            }
            else
            {
                int y = (num1 + num2) / 2;
                int x = num1 - y;
                System.out.println(y > x ? y + " " + x : x + " " + y);
            }
        }

       

       
    }    
}
