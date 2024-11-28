import java.util.*;
import java.io.IOException;
import java.net.*;
public class user{
    public static void main(String[] args) throws IOException{
        DatagramSocket server = new DatagramSocket(1234);
        byte buffer[] = new byte[1024];
        System.out.println("server is up");
        while(true){
            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            server.receive(packet);
            String msg = new String(packet.getData(), 0, packet.getLength());
            System.out.println(msg);
            if(msg.equals(0)){
                server.close();
            }
        }
    }
}