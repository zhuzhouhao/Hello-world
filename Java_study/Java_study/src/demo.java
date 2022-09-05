public class demo
{
  public static String name = "I";
  protected float hp;
  private static void BattleWin()
  {
    System.out.println("battle win");

  }

  //
  static class EnemyCrystal
  {
    int hp = 0;
    public void checkIfVictory()
    {
      if(hp == 0)
      {
        demo.BattleWin();
        System.out.println(name + " " + "win this game");

      }
    }
  }

  public static void main(String[] args)
  {
    demo.EnemyCrystal crystal = new demo.EnemyCrystal();
    crystal.checkIfVictory();
  }


}