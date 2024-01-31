import java.util.Scanner;

public class lekitra {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.next();
        int length = word.length();

        // break
        String smallestWord = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz";
        for (int i = 0; i < length; i++)
        {
            for (int j = i + 1; j < length - 1; j++)
            {
                String part1 = word.substring(0, i + 1);
                String part2 = word.substring(i+1, j+1);
                String part3 = word.substring(j+1, length);
                
                String cS = changeString(part1, part2, part3);

                if (cS.compareTo(smallestWord) < 0)
                {
                    smallestWord = cS;
                }
            }
        }
        
        System.out.println(smallestWord);
    }

    public static String changeString(String part1, String part2, String part3)
    {
        String cPart1 = changePartString(part1);
        String cPart2 = changePartString(part2);
        String cPart3 = changePartString(part3);

        return cPart1 + cPart2 + cPart3;

    }

    public static String changePartString(String part)
    {
        int partLen = part.length();
        int partHLen = partLen % 2 == 0 ? partLen / 2 : partLen / 2 + 1;
        char[] partChar = part.toCharArray();

        for (int i = 0; i < partHLen; i++)
        {
            char temp = partChar[i];
            partChar[i] = partChar[partLen - i - 1];
            partChar[partLen - i - 1] = temp;
        }

        return new String(partChar);
    }
}
