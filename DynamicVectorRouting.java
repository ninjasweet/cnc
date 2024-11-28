import java.util.*;
public class DynamicVectorRouting{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int total[][] = new int[4][4];
        int cost[][] = {
            {0, 3, 0, 7},
            {3, 0, 2, 0},
            {0, 2, 0, 1},
            {7, 0, 1, 0}
        };
        int i, j;
        int ans[] = new int[4];
        for(i=0;i<4;i++){
            ans = BellManFord(cost, i);
            System.out.println("\nRouting table for "+i+"\n");
            for(j=0;j<4;j++){
                total[i][j] = ans[j];
                System.out.println(i+" -> "+j+" = "+ans[j]);
            }
        }
    }
    public static int[] BellManFord(int distance[][], int source){
        int keys[] = new int[4];
        int i, j, k;
        for(i=0;i<4;i++){
            keys[i] = 1000;
        }
        keys[source] = 0;
        for(i=0;i<3;i++){
            for(j=0;j<4;j++){
                for(k=0;k<4;k++){
                    if(distance[j][k] != 0 && keys[j] + distance[j][k]< keys[k]){
                        keys[k] = keys[j] + distance[j][k];
                    }
                }
            }
        }
        return keys;
    }
}