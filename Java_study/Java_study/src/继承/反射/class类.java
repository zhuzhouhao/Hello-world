package 继承.反射;

import 对象与类.Employee;

import java.lang.reflect.InvocationTargetException;

public class class类
{
  public static void main(String[] args)
  {
    //获得一个类的名字
    var e = new Employee();
    System.out.println(e.getClass().getName());

    //获得类名对应的Class对象
    String classname = "java.util.Random";
    Class cl;
    try
    {
      cl = Class.forName(classname);
    }
    catch (ClassNotFoundException ex)
    {
      throw new RuntimeException(ex);
    }

    //构造类的实例
    try
    {
      try
      {
        Object obj = cl.getConstructor().newInstance();
      }
      catch (InstantiationException ex)
      {
        throw new RuntimeException(ex);
      }
      catch (IllegalAccessException ex)
      {
        throw new RuntimeException(ex);
      }
      catch (InvocationTargetException ex)
      {
        throw new RuntimeException(ex);
      }
    }
    catch (NoSuchMethodException ex)
    {
      throw new RuntimeException(ex);
    }


  }
}
