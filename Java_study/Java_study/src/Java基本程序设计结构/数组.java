package Java基本程序设计结构;

import java.util.Arrays;

public class 数组
{
    public static void main(String[] args)
    {
        //声明数组
        int[] a = new int[100];
        int[] smallPrimes = {2,3,4,5,7};
        var bigPrimes = new int[] {17,19};
        System.out.println(Arrays.toString(bigPrimes));

        //访问数组元素
        for (int i = 0;i<100;i++)
        {
            a[i] = i;
        }

        //获得数组的元素个数
        System.out.println(a.length);

        //for each循环，遍历的是数组中的每个元素，不是下标
        for (int element:a)
        {
            System.out.println(element);
        }

        //数组拷贝
        int[] copiedLuckyNumbers = Arrays.copyOf(smallPrimes,smallPrimes.length);
        System.out.println(Arrays.toString(copiedLuckyNumbers));
    }
}
