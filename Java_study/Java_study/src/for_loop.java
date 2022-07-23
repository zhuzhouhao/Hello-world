import java.util.Scanner;

public class for_loop
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        System.out.println("请问你想循环多少次呢?");
        int times_loop = in.nextInt();
        for (int i = 1;i<times_loop;i++)
        {
            System.out.printf("The %02d is hello world\n",i);
        }
        System.out.printf("The %02d is hello world",times_loop);

    }
}