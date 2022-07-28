package Java基本程序设计结构;

public class 位运算符
{
    public static void main(String[] args)
    {
        int a = 15;
        int fourthBitFromRight = (a & 0b1000) /0b1000;
        System.out.println(fourthBitFromRight);
        
        int fourthBitFromRight2 = (a & 1 << 3) >> 3;
        System.out.println(fourthBitFromRight2);
    }
}