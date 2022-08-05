import java.util.Scanner;
public class demo
{
    public static void main(String[] args)
    {
        Scanner scanner = new Scanner(System.in);
        double height = scanner.nextDouble();
        double weight = scanner.nextDouble();

        //write your code here......
        enum STATUS {ÃçÌõ,Æ«Êİ,ÊÊÖĞ,Æ«ÅÖ};
        STATUS state;
        double IBM = weight / (Math.pow(height,2));
        if(IBM < 18.5)
        {
            state = STATUS.ÃçÌõ;
        }
        else if (IBM < 20.9)
        {
            state = STATUS.Æ«Êİ;
        }
        else if (IBM < 24.9)
        {
            state = STATUS.ÊÊÖĞ;
        }
        else
        {
            state = STATUS.Æ«ÅÖ;
        }
        System.out.println(state);
    }
}
