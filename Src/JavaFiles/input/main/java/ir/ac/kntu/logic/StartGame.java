package ir.ac.kntu.logic;

import java.util.ArrayList;
import java.util.Random;

public class StartGame {
    Random random = new Random();
    private ArrayList<Soldier> a;
    private ArrayList<Soldier> b;
    private Print print = new Print();

    public StartGame(ArrayList<Soldier> a, ArrayList<Soldier> b){
        this.a = new ArrayList<>(a);
        this.b = new ArrayList<>(b);
    }

    public void shoot(Soldier a, Soldier b){
        int hit = random.nextInt(100) + 1;
        System.out.println("Fight:");
        System.out.println("Soldier A Attacks B");
        if (hit <= a.getHitRate()){
            b.setHealth(b.getHealth() - a.getDamage());
            System.out.println("The Shot Hit:              Dmg:" + a.getDamage());
        }else {
            System.out.println("The Shot Missed!");
        }
        hit = random.nextInt(100) + 1;
        System.out.println("Soldier B Attacks A");
        if (hit <= b.getHitRate()){
            a.setHealth(a.getHealth() - b.getDamage());
            System.out.println("The Shot Hit:              Dmg:" + b.getDamage());
        }else {
            System.out.println("The Shot Missed!");
        }
        print.line();
    }

    public void shoot2(){
        ArrayList<Integer> idA = new ArrayList<>();
        ArrayList<Integer> idB = new ArrayList<>();
        for (int i = 0; i < a.size(); i++){
            idA.add(i, i+1);
            idB.add(i, i+1);
        }
        while (a.size() != 0 && b.size() != 0){
            int randSoliderA = random.nextInt(a.size());
            int randSoliderB = random.nextInt(b.size());
            System.out.println("**ARENA**");
            System.out.println("Team A Solider: ");
            print.printSoldier(a.get(randSoliderA), randSoliderA + 1);
            System.out.println("Team B Solider: ");
            print.printSoldier(b.get(randSoliderB), randSoliderB + 1);
            print.line();
            shoot(a.get(randSoliderA), b.get(randSoliderB));
            if (a.get(randSoliderA).getHealth() < 0){
                System.out.println("Solider Of Side A Been Killed!             Id: " + idA.get(randSoliderA));
                a.remove(randSoliderA);
                idA.remove(randSoliderA);
            }
            if (b.get(randSoliderB).getHealth() < 0){
                System.out.println("Solider Of Side B Been Killed!             Id: " + idB.get(randSoliderB));
                b.remove(randSoliderB);
                idB.remove(randSoliderB);
            }
            if (a.size() != 0 && b.size() != 0){
                print.gameNotFinished();
                pressAnyKey();
            }
        }
        print.gameFinished(a, b);
    }

    public void pressAnyKey(){
        System.out.println("Press Any Key To Continue...");
        try {
            System.in.read();
            System.in.read();
        }
        catch (Exception e){

        }

    }
}
