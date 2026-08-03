import java.util.*;
import java.io.*;

public class Main {
    static int N, Q;
    static int MAX_N = 1000000;
    static int[] point = new int[MAX_N+2];
    static int[][] range;
    static int[] preSum = new int[MAX_N+2];
    static int a, b;


    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());
        range = new int[Q][2];

        st = new StringTokenizer(br.readLine());
        for (int n=0; n<N; n++) {
            point[Integer.parseInt(st.nextToken())+1] = 1;
        }

        for (int q=0; q<Q; q++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            range[q][0] = a+1;
            range[q][1] = b+1;
        }

        for (int n=1; n<MAX_N; n++) {
            preSum[n] = preSum[n-1] + point[n];
        }
    }

    public static void main(String[] args) throws IOException {
        init();

        // System.out.println(Arrays.toString(preSum));
        int val;

        for (int[] q : range) {
            a = q[0]; b = q[1];

            val = preSum[b] - preSum[a-1];
            System.out.println(val);
        }
    }
}