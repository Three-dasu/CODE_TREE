import java.util.*;
import java.io.*;

public class Main {
    static int N, Q;
    static int[] point, lst;
    static Set<Integer> tSet = new TreeSet<>();
    
    static int bisectLeft(int[] lst, int x) {
        int left = 0;int right = lst.length;
        int mid;

        while (left < right) {
            mid = (left + right) / 2;

            if (lst[mid] < x) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return left;
    }

        static int bisectRight(int[] lst, int x) {
        int left = 0; int right = lst.length;
        int mid;

        while (left < right) {
            mid = (left + right) / 2;

            if (lst[mid] <= x) {
                left = mid + 1;
            }
            else {
                right = mid;
            }
        }
        return left;
    }

    static void compress() {
        for (int n : point) {
            tSet.add(n);
        }

        lst = new int[tSet.size()];
        int idx = 0;

        for (int n : tSet) {
            lst[idx++] = n;
        }
    }

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); Q = sc.nextInt();

        point = new int[N];
        for (int i=0; i<N; i++) {
            point[i] = sc.nextInt();
        }

        compress();
        
        // System.out.println(lst);


        for (int q=0; q<Q; q++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            // q[0]값을 bisectLeft로 point에서 찾아야 함?
            int li = bisectLeft(lst, a);
            int ri = bisectRight(lst, b);

            int ans = ri - li;

            // int ans = hMap.get(lst[ri]) - hMap.get(lst[li]) + 1;

            System.out.println(ans);
        }
    }
}