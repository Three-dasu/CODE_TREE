import java.util.*;
import java.io.*;

public class Main {
    static int N;
    static String str;
    static HashMap<String, Integer> dict = new HashMap<>();


    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());

        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            str = st.nextToken();
            if (dict.containsKey(str)) {
                dict.put(str, dict.get(str)+1);
            }
            else {
                dict.put(str, 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int ans = 0;

        init();

        for (Map.Entry<String, Integer> entry : dict.entrySet()) {
            String key = entry.getKey();
            int val = entry.getValue();
            if (val > ans) {
                ans = val;
            }
        }

        System.out.print(ans);
    }
}