package Java����������ƽṹ;

public class �ַ���
{
    public static void main(String[] args)
    {
        //��ȡ�ַ���
        String greeting = "Hello";
        String s = greeting.substring(0,3);
        System.out.println(s);
        
        //ƴ���ַ���
        String expletive = "Expletive";
        String PG13 = "delete";
        String message = expletive + PG13;
        System.out.println(message);

        //������ַ�������һ��
        String all = String.join("/","S","M","L","XL");
        System.out.println(all);

        //repeat����
        String repeat = "Java".repeat(3);
        System.out.println(repeat);
        
        //�޸��ַ���
        greeting = greeting.substring(0,3) + "p!";
        System.out.println(greeting);
        
        //����ַ����Ƿ����
        boolean k = "Hello".equals(greeting);
        System.out.println(k);
        
        //���Դ�С�ļ���ַ����Ƿ����
        boolean judge = "hello".equalsIgnoreCase("Hello");
        System.out.println(judge);
        
        //�մ���Null��
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

        //�������뵥Ԫ
            //�õ������������ʵ�ʵĳ��ȣ����Ե���
            int n = greeting.codePointCount(0,greeting.length());
            System.out.println(n);

            //����λ��n�Ĵ��뵥Ԫ
            char first = greeting.charAt(0);
            char last = greeting.charAt(greeting.length() - 1);
            System.out.println(first + "," + last);

            //�õ���i�����
            int i = greeting.length()-1 ;
            int index = greeting.offsetByCodePoints(0,i);
            int cp = greeting.codePointAt(index);
            System.out.println(cp);

            //����һ���ַ���,ʹ��codePoints����������һ��intֵ�ġ�������ת����һ�����飬����ɱ���
           int[] codePoints = str.codePoints().toArray();

            //���������ת��Ϊһ���ַ���
            String str2 = new String(codePoints,0,codePoints.length);

        //String API
            //�Ƚ��ַ������ֵ�˳��
            String str3 = "prkeere";
            int compare = str3.compareTo("hello");
            System.out.println(compare);
            
        //�����ַ���,��Ҫ����һ���ַ���������
        StringBuilder builder = new StringBuilder();
        String ch = "he";
        String ch1 = "llo";
        builder.append(ch);
        builder.append(ch1);
        String completedString = builder.toString();
        System.out.println(completedString);
    }
}
