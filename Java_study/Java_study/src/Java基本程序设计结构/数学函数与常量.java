package Java基本程序设计结构;
import static java.lang.Math.*;
public class 数学函数与常量
{
    public static void main(String[] args)
    {
        double x = 4;
        double y = Math.sqrt(x);
        System.out.println(y);
        double a = 2;
        double z = Math.pow(x,a);
        System.out.println(z);
        System.out.println(Math.E);
        System.out.println(PI);
        /*
        其实，不必每次都要用Math.来引用方法或变量名，只需要在开头加上import static java.lang.Math.*就可以了
         */
    }
}
