import java.util.*;
import java.io.*;

public class Main {
    static int N, Q;
    static int[] point, lst;
    static Set<Integer> tSet = new TreeSet<>();
    
    static int bisectLeft(int[] lst, int x) {
        int left = 0; int right = lst.length;
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
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        point = new int[N];
        for (int i=0; i<N; i++) {
            point[i] = Integer.parseInt(st.nextToken());
        }

        compress();
        
        // System.out.println(lst);


        for (int q=0; q<Q; q++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            // q[0]값을 bisectLeft로 point에서 찾아야 함?
            int li = bisectLeft(lst, a);
            int ri = bisectRight(lst, b);

            int ans = ri - li;

            // int ans = hMap.get(lst[ri]) - hMap.get(lst[li]) + 1;

            sb.append(ans).append("\n");
        }

        System.out.print(sb);
    }

}