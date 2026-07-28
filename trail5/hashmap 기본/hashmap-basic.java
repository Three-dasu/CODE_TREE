import java.util.*;

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

    static void init() {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();

        for (int n=0; n<N; n++) {
            String cmd = sc.next();
            if (cmd.equals("add")) {
                int a = sc.nextInt(); int b = sc.nextInt();
                qlst.add(new Query(cmd, a, b));
            }
            else {
                int a = sc.nextInt();
                qlst.add(new Query(cmd, a, 0));
            }
            
        }
    }


    public static void main(String[] args) {
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