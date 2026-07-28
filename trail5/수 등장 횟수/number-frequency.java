import java.util.*;
import java.io.*;

public class Main {
    static int N, M;
    static List<Integer> lst;
    static List<Integer> qlst;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        lst = new ArrayList<>();
        qlst = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int n=0; n<N; n++) {
            lst.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        for (int m=0; m<M; m++) {
            qlst.add(Integer.parseInt(st.nextToken()));
        }

        // System.out.println(lst);
        // System.out.println(qlst);
    }

    public static void main(String[] args) throws IOException {
        init();

        HashMap<Integer, Integer> dict = new HashMap<>();

        for (int n : lst) {
            if (dict.containsKey(n)) {
                dict.put(n, dict.get(n)+1);
            }
            else {
                dict.put(n, 1);
            }
        }

        for (int m=0; m<M; m++) {
            int num = qlst.get(m);
            if (dict.containsKey(num)) {
                System.out.print(dict.get(qlst.get(m)) + " ");
            }
            else {
                System.out.print(0 + " ");
            }
            
        }
    }
}