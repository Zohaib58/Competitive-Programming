import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class awkwardParty {
    public static void main(String[] args)  {
        Scanner sc = new Scanner(System.in);
        HashMap<Integer, Integer> map = new HashMap<>();
        int times = sc.nextInt();
        sc.nextLine();
        String[] inputLine = sc.nextLine().split(" ");
        
        int[] arr = new int[times];

        for (int i = 0; i < times; i++) {
            arr[i] = Integer.parseInt(inputLine[i]); // Parse each integer and store it in arr
        }

        int res = arr.length;

        for (int i = 0; i < times; i++)
        {
            if (map.containsKey(arr[i]))
            {
                res = Math.min(res, i - map.get(arr[i]));
            }
            else
            {
                map.put(arr[i], i); 
            }
        }

        System.out.println(res);
    }
}
