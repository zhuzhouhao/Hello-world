import java.util.Scanner;
public class demo
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        double height = scanner.nextDouble();
        double weight = scanner.nextDouble();

        //write your code here......
        enum STATUS {����,ƫ��,����,ƫ��};
        STATUS state;
        double IBM = weight / (Math.pow(height,2));
        if(IBM < 18.5)
        {
            state = STATUS.����;
        }
        else if (IBM < 20.9)
        {
            state = STATUS.ƫ��;
        }
        else if (IBM < 24.9)
        {
            state = STATUS.����;
        }
        else
        {
            state = STATUS.ƫ��;
        }
        System.out.println(state);
    }
}
