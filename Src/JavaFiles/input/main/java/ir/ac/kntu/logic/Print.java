package ir.ac.kntu.logic;

import java.util.ArrayList;

public class Print {

    private ArrayList<Soldier> a;
    private ArrayList<Soldier> b;
    /*public Print(ArrayList<Soldier> a, ArrayList<Soldier> b){
        this.a = new ArrayList<>(a);
        this.b = new ArrayList<>(b);
    }*/

    public void printTeams(ArrayList<Soldier> a, ArrayList<Soldier> b){
        System.out.println("Side A:");
        for (int i = 0; i < a.size(); i++){
            printSoldier(a.get(i), i+1);
        }
        line();
        System.out.println("Side B:");
        for (int i = 0; i < b.size(); i++){
            printSoldier(b.get(i), i+1);
        }
        line();
    }

    public void gameFinished(ArrayList<Soldier> a, ArrayList<Soldier> b){
        System.out.println("The Fight Is Finished...");
        if (a.size() !=  0){
            System.out.println("Result: Team A Won!!");
        }else {
            System.out.println("Result: Team B Won!!");
        }
    }

    public String rifleType(Soldier soldier){
        String type;
        if (soldier.getRifle().getRifleType().equals(RifleType.ASSAULT)){
            type = "Assault";
        }else {
            if (soldier.getRifle().getZoom()){
                type = "Sniper-scope";
            }else {
                type = "Sniper";
            }

        }
        return type;
    }

    public void printSoldier(Soldier soldier, int id){
        System.out.println("[ id: " + id + " | " + "HP: " + soldier.getHealth() + " | " +
                "Dmg: " + soldier.getDamage() + " | " + "Acc: " + soldier.getHitRate()+ "%" + " | "
                + "Gun: " + rifleType(soldier) + " | " + "Calibre: " + caliberType(soldier) + " ]");
    }

    public void line(){
        System.out.println("\n");
        System.out.println("---------------------------------------------------------------------------------");
        System.out.println("\n");
    }

    public void gameNotFinished(){
        System.out.println("The Game Is Not Finished Yet!");
    }

    public String caliberType(Soldier soldier){
        String type;
        if (soldier.getRifle().getCaliber().equals(Caliber.CALIBER_7)){
            type = "7mm";
        }else {
            type = "5mm";
        }
        return type;
    }
}
