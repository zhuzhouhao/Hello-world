package 对象与类;

import java.time.LocalDate;

public class Employee implements Comparable<Employee>{
  private String name;
  private double salary;
  private LocalDate hireDay;

  public Employee(String n, double s, int year, int month, int day) {
    name = n;
    salary = s;
    hireDay = LocalDate.of(year, month, day);
  }

  public Employee(){}

  public Employee(String name,double salary)
  {
    this.name = name;
    this.salary = salary;
  }

  public String getName() {
    return name;
  }

  public double getSalary() {
    return salary;
  }

  public LocalDate getHireDay() {
    return hireDay;
  }

  public void raiseSalary(double byPercent) {
    double raise = salary * byPercent / 100;
    salary += raise;
  }

  public String toString()
  {
    return getClass().getName() + "[name = " + this.getName() + ",he/she was employed at " + hireDay +  ",his salary is "+ salary + "]";
  }

  /**
   * Compares employees by salary
   * @param other another Employee object
   * @return a negative value if this employee has a lower salary than
   * otherObject, 0 if the salaries are the same, a positive value otherwise
   */
  public int compareTo(Employee other)
  {
    return Double.compare(salary, other.salary);
  }

}
