import java.util.*;
import java.io.*;


class Query {
    String cmd;
    int a, b;
    public Query(String cmd, int a, int b) {
        this.cmd = cmd;
        this.a = a;
        this.b = b;
    }
}
public class Main {

    static int N;
    static List<Query> qlst = new ArrayList<>();
    static HashMap<Integer, Integer> dict = new HashMap<>();

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // N 읽기
        N = Integer.parseInt(br.readLine().trim());

        for (int n = 0; n < N; n++) {
            // 1. 한 줄을 통째로 읽어서 공백 기준으로 쪼갤 준비
            StringTokenizer st = new StringTokenizer(br.readLine());

            String cmd = st.nextToken();
            int a = Integer.parseInt(st.nextToken());
            int b = 0; // 기본값

            // 2. 이 줄에 더 쪼갤 데이터(b)가 남아있다면 읽기!
            if (st.hasMoreTokens()) { 
                b = Integer.parseInt(st.nextToken());
            }

            qlst.add(new Query(cmd, a, b));
        }
    }


    public static void main(String[] args) throws IOException {
        init();

        for (Query q : qlst) {
            // System.out.println(q);

            if (q.cmd.equals("add")) {
                dict.put(q.a, q.b);
            }

            else if (q.cmd.equals("remove")) {
                dict.remove(q.a);
            }

            else {
                if (dict.containsKey(q.a)) {
                    System.out.println(dict.get(q.a));
                }
                else {
                    System.out.println("None");
                }
                
            }
        }
    }
}