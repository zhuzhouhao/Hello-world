package �̳�;

import ��������.Employee;

import java.util.*;

public class ArrayList��ʹ��
{
  public static void main(String[] args)
  {
    var staff = new ArrayList<Employee>(10);
    staff.add(new Employee("Zhang San",1000,2022,1,1));
    var sample = new Employee();
    sample = staff.get(0);
    System.out.println(sample.toString());
  }
}