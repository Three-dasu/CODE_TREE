import java.util.*;
import java.io.*;

public class Main {
    static int N, Q;
    static int[] stoneList;
    static int[][] rangeList;
    static int[][] preSum;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        Q = Integer.parseInt(st.nextToken());

        stoneList = new int[N];
        rangeList = new int[Q][2];
        preSum = new int[3][N+1];

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            stoneList[i] = Integer.parseInt(st.nextToken());
        }

        for (int i=0; i<Q; i++) {
            st = new StringTokenizer(br.readLine());
            rangeList[i][0] = Integer.parseInt(st.nextToken());
            rangeList[i][1] = Integer.parseInt(st.nextToken());
        }

        for (int i=1; i<N+1; i++) {
            preSum[0][i] = preSum[0][i-1] + ((stoneList[i-1]==1) ? 1:0);
            preSum[1][i] = preSum[1][i-1] + ((stoneList[i-1]==2) ? 1:0);
            preSum[2][i] = preSum[2][i-1] + ((stoneList[i-1]==3) ? 1:0);
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        // System.out.println(Arrays.toString(preSum[0]));
        
        StringBuilder sb = new StringBuilder();

        for (int[] q : rangeList) {
            int a = q[0]; int b = q[1];
            for (int i=0; i<3; i++) {
                int val = preSum[i][b] - preSum[i][a-1];
                sb.append(val).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}