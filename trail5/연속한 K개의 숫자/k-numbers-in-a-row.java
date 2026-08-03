import java.util.*;
import java.io.*;

public class Main {
    static int N, K, B;
    static int[] lst;
    static Set<Integer> bset;
    static int[] preSum;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        int num;

        lst = new int[N];
        preSum = new int[N+1];
        bset = new HashSet<>();

        for (int b=0; b<B; b++) {
            st = new StringTokenizer(br.readLine());
            num = Integer.parseInt(st.nextToken())-1;
            bset.add(num);
        }

        for (int n=0; n<N; n++) {
            if (bset.contains(n)) {
                lst[n] = 0;
            }
            else {
                lst[n] = 1;
            }
        }

        for (int n=1; n<N; n++) {
            preSum[n] = preSum[n-1] + lst[n];
        }
    }

    /*
    현재 B개 숫자가 없는데,
    연속한 K개 숫자들이 최소 한세트는 있어야 함
    숫자를 최소 몇개나 추가해야 할까

    일단 prefix sum이니까 무슨 sum을 미리 계산해야 하는지 생각해보면
    그냥 있는 거 1 없는 거 0 해놓고
    길이 K인 구간에서 합이 K가 되게 하는 경우들 보면 되는구나
    */

    public static void main(String[] args) throws IOException {
        int val = Integer.MAX_VALUE;
        init();

        // System.out.println(Arrays.toString(lst));
        // System.out.println(bset);
        // System.out.println(Arrays.toString(preSum));

        for (int i=K; i<N; i++) {
            val = Math.min(val, K - (preSum[i] - preSum[i-K]));
        }
        System.out.println(val);

    }
}