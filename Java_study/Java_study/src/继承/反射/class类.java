package �̳�.����;

import ��������.Employee;

import java.lang.reflect.InvocationTargetException;

public class class��
{
  public static void main(String[] args)
  {
    //���һ���������
    var e = new Employee();
    System.out.println(e.getClass().getName());

    //���������Ӧ��Class����
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

    //�������ʵ��
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
