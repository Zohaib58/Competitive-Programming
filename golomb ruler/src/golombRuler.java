import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class golombRuler {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            String[] arr = line.split(" ");
            int length = arr.length;
            int[] intArr = new int[length];

            int max = -1;

            for (int j = 0; j < intArr.length; j++) {
                intArr[j] = Integer.parseInt(arr[j]);
                max = Math.max(max, intArr[j]);
            }

            boolean[] rec = new boolean[max * 2 + 1];
            boolean output = false;

            for (int i = 0; i < intArr.length; i++) {
                for (int j = i + 1; j < intArr.length; j++) {
                    int diff = Math.abs(intArr[j] - intArr[i]);
                    if (rec[diff]) {
                        System.out.println("not a ruler");
                        output = true;
                        break;
                    } else {
                        rec[diff] = true;
                    }
                }
                if (output) {
                    break;
                }
            }

            if (!output) {
                boolean perfect = true;
                StringBuilder missing = new StringBuilder("missing ");
                for (int i = 1; i <= max; i++) {
                    if (!rec[i]) {
                        perfect = false;
                        missing.append(i).append(" ");
                    }
                }

                if (!perfect) {
                    System.out.println(missing.toString().trim());
                } else {
                    System.out.println("perfect");
                }
            }
        }
    }
}
