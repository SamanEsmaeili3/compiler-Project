package ir.ac.kntu.logic;
import ir.ac.kntu.logic.Rifle;


public class Soldier {
    private int health;
    private int damage;
    private Rifle rifle;

    public Soldier(int health, Rifle rifle){
        this.health = health;
        this.rifle = rifle;
        this.damage = rifle.getDamageRate();
    }

    public Soldier(int health, int damage){
        this.health = health;
        this.damage = damage;
    }

    public int getHealth(){
        return this.health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getDamage(){
        return this.damage;
    }

    public Rifle getRifle() {
        return rifle;
    }

    public int getHitRate(){
        return rifle.getHitRate();
    }
}
