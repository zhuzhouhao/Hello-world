package 继承;

public class 参数数量可变的方法
{
  public static void main(String[] args)
  {
    //计算一个若干数量的数值中的最大值


    double m = max(3.1,40.4,-5);
    System.out.println(m);
  }


  public static double max(double ... values)
  {
    double largest = Double.NEGATIVE_INFINITY;
    for (double v:values)
    {
      if(v > largest)
      {
        largest = v;
      }
    }
    return largest;
  }
}
