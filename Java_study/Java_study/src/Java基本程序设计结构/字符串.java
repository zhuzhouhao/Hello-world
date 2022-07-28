package Java基本程序设计结构;

public class 字符串
{
    public static void main(String[] args)
    {
        //提取字符串
        String greeting = "Hello";
        String s = greeting.substring(0,3);
        System.out.println(s);
        
        //拼接字符串
        String expletive = "Expletive";
        String PG13 = "delete";
        String message = expletive + PG13;
        System.out.println(message);

        //将多个字符串放在一起
        String all = String.join("/","S","M","L","XL");
        System.out.println(all);

        //repeat方法
        String repeat = "Java".repeat(3);
        System.out.println(repeat);
        
        //修改字符串
        greeting = greeting.substring(0,3) + "p!";
        System.out.println(greeting);
        
        //检测字符串是否相等
        boolean k = "Hello".equals(greeting);
        System.out.println(k);
        
        //忽略大小的检测字符串是否相等
        boolean judge = "hello".equalsIgnoreCase("Hello");
        System.out.println(judge);
        
        //空串与Null串
        String str = "";
        if(str.length() == 0)
        {
            System.out.println(true);

        }
        if (str.equals(""))
        {
            System.out.println(true);
        }
        if(str.length() != 0 && str != null)
        {
            System.out.println(true);
        }

        //码点与代码单元
            //得到码点数量，即实际的长度，可以调用
            int n = greeting.codePointCount(0,greeting.length());
            System.out.println(n);

            //返回位置n的代码单元
            char first = greeting.charAt(0);
            char last = greeting.charAt(greeting.length() - 1);
            System.out.println(first + "," + last);

            //得到第i个码点
            int i = greeting.length()-1 ;
            int index = greeting.offsetByCodePoints(0,i);
            int cp = greeting.codePointAt(index);
            System.out.println(cp);

            //遍历一个字符串,使用codePoints方法，生成一个int值的“流”，转换成一个数组，再完成遍历
           int[] codePoints = str.codePoints().toArray();

            //将码点数组转换为一个字符串
            String str2 = new String(codePoints,0,codePoints.length);

        //String API
            //比较字符串的字典顺序
            String str3 = "prkeere";
            int compare = str3.compareTo("hello");
            System.out.println(compare);
            
        //构建字符串,需要构建一个字符串构建器
        StringBuilder builder = new StringBuilder();
        String ch = "he";
        String ch1 = "llo";
        builder.append(ch);
        builder.append(ch1);
        String completedString = builder.toString();
        System.out.println(completedString);
    }
}
