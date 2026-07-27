import java.util.*;


public class Main {
    static int N;
    

    static int BFS() {
        int cn, cf;

        Queue<int[]> q = new ArrayDeque<>();
        Set<String> v = new HashSet<>();

        q.add(new int[] {N, 0});
        v.add(N +","+ 0);

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            cn = pos[0]; cf = pos[1];

            if (cn==1) {
                return cf;
            }

            // -1
            if (!v.contains(cn-1 +","+ cf+1)) {
                q.add(new int[] {cn-1, cf+1});
                v.add(cn-1 +","+ cf+1);
            }

            // +1
            if (!v.contains(cn+1 +","+ cf+1)) {
                q.add(new int[] {cn+1, cf+1});
                v.add(cn+1 +","+ cf+1);
            }
            
            // /2
            if (cn%2==0 && !v.contains(cn/2 +","+ cf+1)) {
                q.add(new int[] {cn/2, cf+1});
                v.add(cn/2 +","+ cf+1);
            }

            // /3
            if (cn%3==0 && !v.contains(cn/3 +","+ cf+1)) {
                q.add(new int[] {cn/3, cf+1});
                v.add(cn/3 +","+ cf+1);
            }
        }
        return -1;
    }

    static void init() {
        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
    }

    public static void main(String[] args) {
        init();

        int ans = BFS();

        System.out.print(ans);
    }
}