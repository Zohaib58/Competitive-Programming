import java.util.Scanner;

public class bitbybit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num;

        do {
            num = sc.nextInt();
            sc.nextLine();  // Consume the newline character

            if (num != 0) {
                long[] arr = new long[32];
                int length = arr.length - 1;

                for (int i = 0; i < 32; i++) {
                    arr[i] = -1L;
                }

                for (int i = 0; i < num; i++) {
                    String input = sc.nextLine();
                    String[] data = input.split(" ");

                    String instruction = data[0];
                    int val = Integer.parseInt(data[1]);

                    int val2 = data.length > 2 ? Integer.parseInt(data[2]) : 0;

                    switch (instruction) {
                        case "SET":
                            arr[length - val] = 1L;
                            break;

                        case "CLEAR":
                            arr[length - val] = 0L;
                            break;

                        case "OR":
                            int a = val;
                            int b = val2;

                            long aVal = arr[length - a];
                            long bVal = arr[length - b];

                            if (aVal == 0L && bVal == 0L) {
                                arr[length - a] = 0L;
                            } else if (aVal == 1L || bVal == 1L) {
                                arr[length - a] = 1L;
                            } else {
                                arr[length - a] = -1L;
                            }
                            break;

                        case "AND":
                            a = val;
                            b = val2;

                            aVal = arr[length - a];
                            bVal = arr[length - b];

                            if (aVal == 1L && bVal == 1L) {
                                arr[length - a] = 1L;
                            } else if (aVal == 0L || bVal == 0L)
                            {
                                arr[length - a] = 0L;
                            } else {
                                arr[length - a] = -1L;
                            }
                            break;
                    }
                }

                for (int j = 0; j < 32; j++) {
                    System.out.print(arr[j] == -1L ? "?" : arr[j]);
                }
                System.out.println();
            }

        } while (num != 0);
    }
}

