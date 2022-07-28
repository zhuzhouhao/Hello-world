package Java基本程序设计结构;

//import java.io.Console;
import java.util.Scanner;

public class 输入输出
{
    public static void main(String[] args)
    {
        //读取输入
            //输入一行，考虑可能包含空格
            Scanner in = new Scanner(System.in);
            System.out.println("What's your name?");
            String name = in.nextLine();
            System.out.println("Hello " + name + "!");

            //输入一个单词，以空白符作为分隔符
            System.out.println("What's your firstName?");
            String firstName = in.next();
            System.out.println("Your firstName is " + firstName + "!");

            //输入一个整数
            System.out.println("How old are you?");
            int age = in.nextInt();
            System.out.println("Your age is " + age + "!");

            //读入一个浮点数
            System.out.println("What's your score?");
            double score = in.nextDouble();
            System.out.println("Your score is " + score + "!");

            //读入密码
            //Console cons = System.console();
            //String username = cons.readLine("User name: ");
            //char[] passwd = cons.readPassword("Password: ");
        //格式化输出
        System.out.printf("%s","hello");
    }
}
