package Java����������ƽṹ;

//import java.io.Console;
import java.util.Scanner;

public class �������
{
    public static void main(String[] args)
    {
        //��ȡ����
            //����һ�У����ǿ��ܰ����ո�
            Scanner in = new Scanner(System.in);
            System.out.println("What's your name?");
            String name = in.nextLine();
            System.out.println("Hello " + name + "!");

            //����һ�����ʣ��Կհ׷���Ϊ�ָ���
            System.out.println("What's your firstName?");
            String firstName = in.next();
            System.out.println("Your firstName is " + firstName + "!");

            //����һ������
            System.out.println("How old are you?");
            int age = in.nextInt();
            System.out.println("Your age is " + age + "!");

            //����һ��������
            System.out.println("What's your score?");
            double score = in.nextDouble();
            System.out.println("Your score is " + score + "!");

            //��������
            //Console cons = System.console();
            //String username = cons.readLine("User name: ");
            //char[] passwd = cons.readPassword("Password: ");
        //��ʽ�����
        System.out.printf("%s","hello");
    }
}
