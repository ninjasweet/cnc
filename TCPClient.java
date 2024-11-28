import java.util.*;
import java.io.*;
import java.net.*;
public class TCPClient{
    public static void main(String[] args) throws IOException {
        Socket client = new Socket("localhost", 1234);
        Scanner reader = new Scanner(client.getInputStream());
        PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
        Scanner in = new Scanner(System.in);
        System.out.println("Client is connected");
        writer.println("Client connected\n");
        while(true){
            String msg = in.nextLine();
            writer.println(msg);
            System.out.println("Sent the message: "+msg);
            if(msg.equals("0")){
                writer.close();
                reader.close();
                client.close();
            }
            String response = reader.nextLine();
            System.out.println(response);
        }
    }
}