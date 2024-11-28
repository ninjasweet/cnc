import java.util.*;
public class shortest_path{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int i, j;
        int distance[][] = {
            {0, 5, 7, 0, 0, 0}, 
            {5, 0, 2, 4, 0, 0},
            {7, 2, 0, 0, 5, 0},
            {0, 4, 0, 0, 1, 8},
            {0, 0, 5, 1, 0, 4}, 
            {0, 0, 0, 8, 4, 0}
        };
        int new_distance[][] = {
            {0, 5, 3, 0, 0, 0},  
            {5, 0, 0, 2, 0, 0},  
            {3, 0, 0, 1, 4, 0}, 
            {0, 2, 1, 0, 6, 0}, 
            {0, 0, 4, 6, 0, -2}, 
            {0, 0, 0, 0, 0, 0}  
        };
        int distances[][] = {
            {0, 5, -2, 0, 0, 0},   
            {5, 0, 0, -4, 0, 0},   
            {-2, 0, 0, -3, 0, 0},  
            {0, -4, -3, 0, 2, 0},  
            {0, 0, 0, 2, 0, 0},    
            {0, 0, 0, 0, 0, 0}     
        };

        int ans[] = Djkistra(distance);
        System.out.println("Using Djkistra Algorithm: ");
        for(i=0;i<6;i++){
            System.out.println("0 -> " + i + " = " + ans[i]);
        }
        System.out.println("\nUsing Bellman Ford Algorithm");
        int new_ans[] = BellManFord(new_distance);
        for(i=0;i<6;i++){
            System.out.println("0 -> " + i + " = " + new_ans[i]);
        }
        System.out.println("\nUsing Bellman Ford Algorithm");
        int final_ans[] = BellManFord(distances);
        for(i=0;i<6;i++){
            System.out.println("0 -> " + i + " = " + final_ans[i]);
        }
    }
    public static int cal_closest_node(int keys[], int visited[]){
        int min_values = 1000, min_node = 0, i;
        for(i=0;i<6;i++){
            if(keys[i]<min_values  && visited[i] == 0){
                min_values = keys[i];
                min_node = i;
            }
        }
        return min_node;
    }
    public static int[] Djkistra(int distance[][]){
        int i, j, min;
        int keys[] = new int[6];
        int visited[] = new int[6];
        for(i=0;i<6;i++){
            keys[i] = 1000; //inf
            visited[i] = 0;
        }
        keys[0] = 0; //start node
        for(i=0;i<6;i++){
            min = cal_closest_node(keys, visited);
            visited[min] = 1;
            for(j=0;j<6;j++){
                if(keys[min] + distance[min][j] < keys[j] && distance[min][j] != 0 && visited[j] == 0){
                    keys[j] = keys[min] + distance[min][j];
                }
            }
        }
        return keys;
    }
    public static int[] BellManFord(int distance[][]){
        int i, j, k;
        int keys[] = new int[6];
        int visited[] = new int[6];
        for(i=0;i<6;i++){
            keys[i] = 1000; 
        }
        keys[0] = 0;
        for(i=0;i<6-1;i++){
            for(j=0;j<6;j++){
                for(k=0;k<6;k++){
                    if(keys[j] + distance[j][k] < keys[k] && distance[j][k] != 0){
                        keys[k] = keys[j] + distance[j][k];
                    }
                }
            }
        }
        for(i=0;i<6;i++){
            for(j=0;j<6;j++){
                if(keys[i] + distance[i][j] < keys[j] && distance[i][j] != 0){
                    System.out.println("Cycle of Negative edges detected.\nThe algorithm fails");
                    System.exit(0);
                }
            }
        }
        return keys;
    }
}