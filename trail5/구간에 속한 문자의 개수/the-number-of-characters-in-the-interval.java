import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] preSumA = new int[N + 1][M + 1];
        int[][] preSumB = new int[N + 1][M + 1];
        int[][] preSumC = new int[N + 1][M + 1];

        // 1. 누적 합 배열 생성 (String 대신 char 원시 타입으로 즉시 처리)
        for (int i = 1; i <= N; i++) {
            String str = br.readLine();
            for (int j = 1; j <= M; j++) {
                char c = str.charAt(j - 1); // 객체 생성 없이 char 추출

                // 조건문 비교도 원시 타입 '==' 활용
                preSumA[i][j] = preSumA[i-1][j] + preSumA[i][j-1] - preSumA[i-1][j-1] + (c == 'a' ? 1 : 0);
                preSumB[i][j] = preSumB[i-1][j] + preSumB[i][j-1] - preSumB[i-1][j-1] + (c == 'b' ? 1 : 0);
                preSumC[i][j] = preSumC[i-1][j] + preSumC[i][j-1] - preSumC[i-1][j-1] + (c == 'c' ? 1 : 0);
            }
        }

        // 2. 출력 병목 해결을 위한 StringBuilder
        StringBuilder sb = new StringBuilder();

        // 3. 쿼리를 배열에 저장하지 않고 입력받는 즉시 처리
        for (int k = 0; k < K; k++) {
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            int valA = preSumA[r2][c2] - preSumA[r2][c1-1] - preSumA[r1-1][c2] + preSumA[r1-1][c1-1];
            int valB = preSumB[r2][c2] - preSumB[r2][c1-1] - preSumB[r1-1][c2] + preSumB[r1-1][c1-1];
            int valC = preSumC[r2][c2] - preSumC[r2][c1-1] - preSumC[r1-1][c2] + preSumC[r1-1][c1-1];
            
            // println 대신 버퍼에 기록
            sb.append(valA).append(" ").append(valB).append(" ").append(valC).append("\n");
        }
        
        // 마지막에 한 번만 출력
        System.out.print(sb);
    }
}