package ºÃ≥–;
public class ≥ÈœÛ¿‡
{
    public static void main(String[] args)
    {
      var stu1 = new Student("zhang san","computer science");
      System.out.println(stu1.getDescription());
    }
    public static abstract class Person
    {
      private String name;
      public Person(String name)
      {
        this.name = name;
      }
      public abstract String getDescription();
      public String getName()
      {
        return name;
      }
      
    }
    public static class Student extends Person
    {
      private String major;
      public Student(String name,String major)
      {
        super(name);
        this.major = major;
      }
      public String getDescription()
      {
        return "a student major in " + major + ",his/her name is " + this.getName();
      }
    }
}