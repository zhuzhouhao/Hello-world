package Java基本程序设计结构;
import java.util.Scanner;

public class while_loop
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int times = in.nextInt();
        int count = 0;
        date:
        if (count == times)
        {
            System.exit(0);
        }
        else
        {
            while (true)
            {
                if (count < times)
                {
                    System.out.println("Hello");
                    count++;
                }
                else {
                    break date;
                }
            }
        }
    }
}