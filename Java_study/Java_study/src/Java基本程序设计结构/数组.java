package Java����������ƽṹ;

import java.util.Arrays;

public class ����
{
    public static void main(String[] args)
    {
        //��������
        int[] a = new int[100];
        int[] smallPrimes = {2,3,4,5,7};
        var bigPrimes = new int[] {17,19};
        System.out.println(Arrays.toString(bigPrimes));

        //��������Ԫ��
        for (int i = 0;i<100;i++)
        {
            a[i] = i;
        }

        //��������Ԫ�ظ���
        System.out.println(a.length);

        //for eachѭ�����������������е�ÿ��Ԫ�أ������±�
        for (int element:a)
        {
            System.out.println(element);
        }

        //���鿽��
        int[] copiedLuckyNumbers = Arrays.copyOf(smallPrimes,smallPrimes.length);
        System.out.println(Arrays.toString(copiedLuckyNumbers));
    }
}
