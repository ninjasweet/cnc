import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
//import java.util.*;
//import java.io.*;
//import java.net.*;
public class UDPServer{
    public static void main(String[] args) throws IOException{
        DatagramSocket server = new DatagramSocket(1234);
        byte buffer[] = new byte[1024];
        System.out.println("Server is up\n");
        while(true){
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            server.receive(packet);
            String msg = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received message: " + msg);
            if(msg.equals("0")){
                System.out.println("Closing the server");
                server.close();
            }
        }
    }
}