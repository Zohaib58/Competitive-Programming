import java.util.Scanner;

public class cds {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);

        int score = sc.nextInt();

        boolean scoreFound = false;
        String[] arrScore = {"Single", "Double", "Triple"};
        String result = "";

        for (int i = 1; i <= 20; i++)
        {
            for (int j = 1; j <= 3; j++)
            {
                if (i * j == score)
                {
                    scoreFound = true;
                    result = arrScore[j - 1] + " " + i;
                    break;
                }
            }
            if (scoreFound)
            {
                break;
            }
        }

        
    }
}
