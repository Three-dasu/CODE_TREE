import java.util.*;
import java.io.*;

public class Main {
    static int N, G;
    static int ans = 0;
    static Set<Integer> set;
    static int[] groupSize;
    static int[] curSize;
    static List<Set<Integer>> g2p = new ArrayList<>();
    static List<Set<Integer>> p2g = new ArrayList<>();
    static boolean[] v;


    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        G = Integer.parseInt(st.nextToken());
        v = new boolean[N];
        groupSize = new int[G];
        curSize = new int[G];

        for (int p=0; p<N; p++) {
            p2g.add(new HashSet<>());
        }

        for (int g=0; g<G; g++) {
            st = new StringTokenizer(br.readLine());

            int size = Integer.parseInt(st.nextToken());
            groupSize[g] = size;

            Set<Integer> g2pSet = new HashSet<>();
            int num;

            for (int s=0; s<size; s++) {
                num = Integer.parseInt(st.nextToken())-1;
                g2pSet.add(num);
                p2g.get(num).add(g);
            }
            g2p.add(g2pSet);
        }
    }

    static Set invite(int n) {
        Set<Integer> returnSet = new HashSet<>();
        if (v[n]) {
            // System.out.println(n +" already seen");
            return returnSet;
        }

        v[n] = true;
        ans += 1;
        
        for (int g : p2g.get(n)) {
            // System.out.println(g2p.get(g));
            // System.out.println(n +" in "+ g +"th set");

            curSize[g] += 1;
            g2p.get(g).remove(n);

            if (curSize[g] == groupSize[g]-1) {
                // 이미 group[g]라는 set에 하나만 있어야 함
                for (int num : g2p.get(g)) {
                    returnSet.add(num);
                    // System.out.println(num +" added to returnSet");
                }
            }
        }

        return returnSet;
    }

    public static void main(String[] args) throws IOException {
        
        init();

        Set<Integer> loopSet = new HashSet<>();
        Set<Integer> tmpSet;
        loopSet.add(0);

        while (loopSet.size() > 0) {
            tmpSet = new HashSet<>();
            for (int n : loopSet) {
                tmpSet.addAll(invite(n));
            }
            loopSet = tmpSet;
        }

        System.out.print(ans);
    }
}