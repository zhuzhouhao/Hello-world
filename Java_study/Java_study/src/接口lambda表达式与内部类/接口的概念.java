package 接口lambda表达式与内部类;

import 对象与类.Employee;

import java.util.Arrays;

public class 接口的概念
{
  public static void main(String[] args)
  {
    var staff = new Employee[3];

    staff[0] = new Employee("Harry Hacker", 35000);
    staff[1] = new Employee("Carl Cracker", 75000);
    staff[2] = new Employee("Tony Tester", 38000);

    Arrays.sort(staff);

    // print out information about all Employee objects
    for (Employee e : staff)
      System.out.println("name=" + e.getName() + ",salary=" + e.getSalary());
  }
}
