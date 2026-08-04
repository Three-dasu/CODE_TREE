import java.util.*;
import java.io.*;

public class Main {
    static int N, M, K;
    static List<String> slst = new ArrayList<>();
    static List<int[]> square = new ArrayList<>();
    static int[][] preSumA, preSumB, preSumC;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String str;
        int num;
        int[] tmp;

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        preSumA = new int[N+1][M+1];
        preSumB = new int[N+1][M+1];
        preSumC = new int[N+1][M+1];

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            str = st.nextToken();
            slst.add(str);
        }

        for (int k=0; k<K; k++) {
            tmp = new int[4];
            st = new StringTokenizer(br.readLine());
            
            for (int i=0; i<4; i++) {
                num = Integer.parseInt(st.nextToken());
                tmp[i] = num;
            }
            square.add(tmp);
        }
        String chr;
        for (int i=1; i<N+1; i++) {
            for (int j=1; j<M+1; j++) {
                chr = slst.get(i-1).charAt(j-1)+"";

                preSumA[i][j] = preSumA[i-1][j] + preSumA[i][j-1]
                                - preSumA[i-1][j-1] + ((chr.equals("a")) ? 1 : 0);
                preSumB[i][j] = preSumB[i-1][j] + preSumB[i][j-1]
                                - preSumB[i-1][j-1] + ((chr.equals("b")) ? 1 : 0);
                preSumC[i][j] = preSumC[i-1][j] + preSumC[i][j-1]
                                - preSumC[i-1][j-1] + ((chr.equals("c")) ? 1 : 0);
            }
        }
    }

    static void myp() {
        for (String tmpStr : slst) {
            System.out.println(tmpStr);
        }

        for (int[] tmpIntArr : square) {
            System.out.println(Arrays.toString(tmpIntArr));
        }

        for (int[] row : preSumA) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
        System.out.println();

        for (int[] row : preSumC) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
        System.out.println();

        for (int[] row : preSumC) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        init();

        // myp();

        int valA, valB, valC;
        for (int[] q : square) {
            valA = preSumA[q[2]][q[3]] - preSumA[q[2]][q[1]-1]
                    - preSumA[q[0]-1][q[3]] + preSumA[q[0]-1][q[1]-1];
            valB = preSumB[q[2]][q[3]] - preSumB[q[2]][q[1]-1]
                    - preSumB[q[0]-1][q[3]] + preSumB[q[0]-1][q[1]-1];
            valC = preSumC[q[2]][q[3]] - preSumC[q[2]][q[1]-1]
                    - preSumC[q[0]-1][q[3]] + preSumC[q[0]-1][q[1]-1];
            
            System.out.println(valA +" "+ valB +" "+ valC);
        }
    }
}