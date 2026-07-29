import java.util.*;
import java.io.*;

class Query {
    String cmd; int x;

    public Query(String cmd, int x) {
        this.cmd = cmd;
        this.x = x;
    }
}

public class Main {
    static int N;
    static Queue<Integer> pq = new PriorityQueue<>();
    static List<Query> qlst = new ArrayList<>();

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        String cmd;
        int x;

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());

            cmd = st.nextToken();
            if (st.hasMoreTokens()) {
                x = Integer.parseInt(st.nextToken());
            }
            else {
                x = 0;
            }

            qlst.add(new Query(cmd, x));
        }
    }

    public static void main(String[] args) throws IOException {
        int val;
        boolean bool;
        init();

        for (Query q : qlst) {
            if (q.cmd.equals("push")) {
                pq.add(-q.x);
            }

            else if (q.cmd.equals("pop")) {
                val = -pq.poll();
                System.out.println(val);
            }

            else if (q.cmd.equals("size")) {
                System.out.println(pq.size());
            }

            else if (q.cmd.equals("empty")) {
                bool = pq.isEmpty();
                if (bool) {
                    System.out.println("1");
                } else {
                    System.out.println(0);
                }
            }

            else {
                System.out.println(-pq.peek());
            }
        }
    }
}