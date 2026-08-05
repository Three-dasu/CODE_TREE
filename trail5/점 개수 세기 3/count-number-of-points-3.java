import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int Q = sc.nextInt();
        int[] point = new int[N];
        int[][] range = new int[Q][2];
        Set<Integer> set = new TreeSet<>();
        Map<Integer, Integer> map = new HashMap<>();

        int idx = 1;
        for (int n=0; n<N; n++) {
            set.add(sc.nextInt());
        }

        for (int n : set) {
            map.put(n, idx);
            idx += 1;
        }

        // System.out.println(map);

        for (int q=0; q<Q; q++) {
            range[q][0] = sc.nextInt();
            range[q][1] = sc.nextInt();
        }

        for (int[] q : range) {
            System.out.println(map.get(q[1]) - map.get(q[0]) + 1);
        }
    }
}