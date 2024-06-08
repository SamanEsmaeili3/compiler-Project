package ir.ac.kntu;

import ir.ac.kntu.logic.*;
import ir.ac.kntu.util.RandomHelper;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        GraphicsEngine engine = new ConsoleGraphicsEngine(); 
        Director director = new Director(engine);
        Scanner scanner = new Scanner(System.in);
        //TODO: Start your game from here
        System.out.println("Enter The Battle Field Length: ");
        int fieldLength = scanner.nextInt();
        ArrayList<Soldier> soldiersA = new ArrayList<>();
        ArrayList<Soldier> soldiersB = new ArrayList<>();
        for (int i = 0; i < fieldLength; i++){
            Soldier soldierA = new Soldier(RandomHelper.nextInt(90) + 10,setRifle());
            Soldier soldierB = new Soldier(RandomHelper.nextInt(90) + 10, setRifle());
            soldiersA.add(soldierA);
            soldiersB.add(soldierB);
        }
        Print print = new Print();
        StartGame startGame = new StartGame(soldiersA, soldiersB);
        print.printTeams(soldiersA, soldiersB);
        //System.out.println("Press Any Key To Start The Fight!");
        startGame.pressAnyKey();
        startGame.shoot2();

    }

    private static Rifle setRifle(){
        boolean isSniper = RandomHelper.nextBoolean();
        if (isSniper){
            Rifle rifle = new SniperRifle(RandomHelper.nextBoolean(), RandomHelper.nextBoolean());
            return rifle;
        }else {
            Rifle rifle = new AssaultRifle(RandomHelper.nextBoolean());
            return rifle;
        }
    }

    private static void shoot(Soldier a, Soldier b){

    }
}
