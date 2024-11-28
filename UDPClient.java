import java.util.*;
import java.io.*;
import java.net.*;
public class UDPClient{
    public static void main(String args[]) throws IOException{
        DatagramSocket client = new DatagramSocket();
        InetAddress address = InetAddress.getByName("localhost");
        Scanner in = new Scanner(System.in);
        byte data[];
        System.out.println("Client connected");
        while(true){
            String msg = in.nextLine();
            data = msg.getBytes();
            DatagramPacket packet = new DatagramPacket(data, data.length, address, 1234);
            client.send(packet);
            System.out.println("Sent message: "+msg);
            if(msg.equals("0")){
                System.out.println("Closing connection");
                client.close();
            }
        }
    }   
}