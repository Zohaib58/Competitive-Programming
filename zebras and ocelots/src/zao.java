import java.util.Scanner;

public class zao {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        long res = 0L;

        sc.nextLine();
        
        for (int i = count - 1; i >= 0; i--)
        {
            String input = sc.nextLine();
            if (input.equals("O"))
            {
                res += 1L << i;
            }
        }


        System.out.println(res);
    }
}
