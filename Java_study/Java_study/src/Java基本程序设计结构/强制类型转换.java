package Java����������ƽṹ;
import static java.lang.Math.*;
public class ǿ������ת��
{
    public static void main(String[] args)
    {
        double x = 9.997;
        int nx = (int) x;
        System.out.println(nx);
        
        int mx = (int) round(x);//ʹ��roundʱ����Ҫʹ��int��ǿת��������ΪroundתΪ����long���ͣ����ܻᷢ����Ϣ�Ķ�ʧ��������ʽ��ǿ������ת�����ܹ���long����ת��Ϊint����
        System.out.println(mx);
    }
}
