package Java����������ƽṹ;

import java.math.*;
public class ����
{
    public static void main(String[] args)
    {
        BigInteger a = BigInteger.valueOf(100);
        System.out.println(a);
        
        BigInteger reallybig = new BigInteger("22332322356789065678998765456789029387");
        System.out.println(reallybig);
        
        BigInteger b = BigInteger.valueOf(1003456345);
        BigInteger c = a.add(b);
        System.out.println(c);
    }
}
