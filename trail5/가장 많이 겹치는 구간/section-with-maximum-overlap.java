import java.util.*;
import java.io.*;

class Point implements Comparable<Point> {
    int x, v;

    public Point(int x, int v) {
        this.x = x;
        this.v = v;
    }

    @Override
    public int compareTo(Point p) {
        if (this.x == p.x) {
            return this.v - p.v;
        }
        return this.x - p.x;
    }
}

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int x1, x2, N;
    static Point[] points;

    static void init() {
        N = sc.nextInt();

        points = new Point[2*N];
        for (int i=0; i<N; i++) {
            x1 = sc.nextInt(); x2 = sc.nextInt();

            points[2*i] = new Point(x1, 1);
            points[2*i+1] = new Point(x2, -1);
        }

        Arrays.sort(points);
    }


    public static void main(String[] args) {
        init();
        int tmp = 0;
        int ans = 0;

        for (Point p : points) {
            // System.out.println(p.x +" "+ p.v);
            tmp += p.v;

            ans = Math.max(ans, tmp);
        }

        System.out.println(ans);
    }
}