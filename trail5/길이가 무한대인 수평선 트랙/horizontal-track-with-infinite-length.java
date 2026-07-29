import java.util.*;
import java.io.*;

public class Main {
    static int N, T;
    static long s, v;
    static List<long[]> lst = new ArrayList<>();
    static long[] finalPos;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            s = Long.parseLong(st.nextToken());
            v = Long.parseLong(st.nextToken());

            lst.add(new long[] {s, v});
        }
    }

    static void getFinalPos() {
        finalPos = new long[N];

        for (int i=0; i<N; i++) {
            s = lst.get(i)[0]; v = lst.get(i)[1];
            finalPos[i] = s + v*T;
            // System.out.println(finalPos[i]);
        }
    }

    static int getGroups() {
        int cnt = 0;
        long curPos = Long.MAX_VALUE;

        for (int i=N-1; i>=0; i--) {
            if (finalPos[i] < curPos) {
                curPos = finalPos[i];
                cnt += 1;
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {
        init();

        getFinalPos();

        int ans = getGroups();

        System.out.println(ans);
    }
}