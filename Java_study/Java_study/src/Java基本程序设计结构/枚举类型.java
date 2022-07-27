package Java基本程序设计结构;
public class 枚举类型
{
    public static void main(String[] args)
    {
        enum Size {SMALL,MEDIUM,LARGE,EXTRA_LARGE};
        Size s = Size.MEDIUM;
        System.out.println(s);
    }
}