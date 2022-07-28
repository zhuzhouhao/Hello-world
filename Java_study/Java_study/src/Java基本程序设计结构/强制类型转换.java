package Java基本程序设计结构;
import static java.lang.Math.*;
public class 强制类型转换
{
    public static void main(String[] args)
    {
        double x = 9.997;
        int nx = (int) x;
        System.out.println(nx);
        
        int mx = (int) round(x);//使用round时还需要使用int来强转，否则因为round转为的是long类型，可能会发生信息的丢失，必须显式地强制类型转换才能够将long类型转换为int类型
        System.out.println(mx);
    }
}
