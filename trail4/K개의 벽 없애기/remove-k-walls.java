import java.util.*;

class Pair {
    int x; int y; int k;

    public Pair(int x, int y, int k) {
        this.x = x;
        this.y = y;
        this.k = k;
    }
}

public class Main {
    static int N, K;
    static int[][] arr;
    static int[][][] v;
    static int si, sj, ei, ej;
    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};

    static void init() {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt(); K = sc.nextInt();

        arr = new int[N][N];
        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        v = new int[N][N][K+1];
        si = sc.nextInt()-1; sj = sc.nextInt()-1;
        ei = sc.nextInt()-1; ej = sc.nextInt()-1;

    }

    static boolean canGo_normal(int x, int y, int k) {
        return 0<=x && x<N && 0<=y && y<N && v[x][y][k]==0 && arr[x][y] == 0;
    }

    static boolean canGo_break(int x, int y, int k) {
        return 0<=x && x<N && 0<=y && y<N && v[x][y][k]==0 && arr[x][y] == 1;
    }

    static int BFS() {
        int ci, cj, ck, ni, nj, nk;
        Queue<Pair> q = new ArrayDeque<>();

        q.add(new Pair(si, sj, 0));
        v[si][sj][0] = 1;

        while (!q.isEmpty()) {
            Pair pos = q.poll();

            ci = pos.x; cj = pos.y; ck = pos.k;

            if (ci==ei && cj==ej) {
                return v[ci][cj][ck]-1;
            }

            for (int d=0; d<4; d++) {
                ni = ci+di[d]; nj = cj+dj[d];

                if (canGo_normal(ni, nj, ck)) {
                    q.add(new Pair(ni, nj, ck));
                    v[ni][nj][ck] = v[ci][cj][ck] + 1;
                }
            
                if (ck < K && canGo_break(ni, nj, ck+1)) {
                    q.add(new Pair(ni, nj, ck+1));
                    v[ni][nj][ck+1] = v[ci][cj][ck] + 1;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        init();

        int ans = BFS();

        System.out.print(ans);
    }
}