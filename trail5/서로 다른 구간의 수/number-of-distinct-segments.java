import java.util.*;
import java.io.*;

class Pos implements Comparable<Pos> {
    int x, v;

    public Pos(int x, int v) {
        this.x = x;
        this.v = v;
    }

    @Override
    public int compareTo(Pos p) {
        if (this.x==p.x) {
            return this.v-p.v;
        }
        return this.x-p.x;
    }
}

public class Main {
    static int a, b, N;
    static List<Pos> point = new ArrayList<>();

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            point.add(new Pos(a, 1));
            point.add(new Pos(b, -1));
        }

        Collections.sort(point);
    }

    public static void main(String[] args) throws IOException {
        init();
        int tmp = 0;
        int cnt = 0;

        for (Pos p : point) {
            tmp += p.v;

            if (tmp==0) {
                cnt += 1;
            }
        }

        System.out.println(cnt);
    }
}