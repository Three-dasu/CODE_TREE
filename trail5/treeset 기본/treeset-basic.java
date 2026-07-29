import java.util.*;
import java.io.*;

class Query {
    String cmd;
    int x;

    public Query(String cmd, int x) {
        this.cmd = cmd;
        this.x = x;
    }
}

public class Main {
    static int N, x;
    static Integer ans;
    static String cmd;
    static List<Query> qlst = new ArrayList<>();
    static TreeSet<Integer> set = new TreeSet<>();

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        for (int q=0; q<N; q++) {
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
        init();

        for (Query q : qlst) {
            // System.out.println(set);

            if (q.cmd.equals("add")) {
                set.add(q.x);
            }

            else if (q.cmd.equals("remove")) {
                set.remove(q.x);
            }

            else if (q.cmd.equals("find")) {
                if (set.contains(q.x)) {
                    System.out.println("true");
                } else {
                    System.out.println("false");
                }
            }

            else if (q.cmd.equals("lower_bound")) {
                ans = set.ceiling(q.x);
                if (ans == null) {
                    System.out.println("None");
                } else {
                    System.out.println(ans);
                }
            }

            else if (q.cmd.equals("upper_bound")) {
                ans = set.higher(q.x);
                if (ans == null) {
                    System.out.println("None");
                } else {
                    System.out.println(ans);
                }
            }

            else if (q.cmd.equals("largest")) {
                if (set.size() == 0) {
                    System.out.println("None");
                    continue;
                }
                ans = set.last();
                System.out.println(ans);
            }

            else {
                if (set.size() == 0) {
                    System.out.println("None");
                    continue;
                }
                ans = set.first();
                System.out.println(ans);
            }
        }
    }
}