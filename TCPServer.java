import java.util.*;
import java.io.*;
import java.net.*;
public class TCPServer{
    public static void main(String args[]) throws IOException{
        ServerSocket server = new ServerSocket(1234);
        System.out.println("The server is up");
        System.out.println("Waiting for client to connect\n");
        Socket client = server.accept();
        Scanner reader = new Scanner(client.getInputStream());
        PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
        while(reader.hasNextLine()){
            String msg = reader.nextLine();
            System.out.println(msg);
            writer.println("The server has recieved the message: "+msg);
            if(msg.equals("0")){
                writer.println("The Client has closed the connection.");
                writer.close();
                reader.close();
                client.close();
                server.close();
            }
        }
    }
}