package ir.ac.kntu.logic;

import java.util.Random;

public class SniperRifle extends Rifle{
    private Random random = new Random();

    public SniperRifle(boolean caliber, boolean zoom){
        setZoom(zoom);
        setRifleType(RifleType.SNIPER);
        setRandCaliber(caliber);
        Caliber caliber1 = getCaliber();
        setRandHit(caliber1,zoom);
        setRandDamage(caliber1);
    }


    public void setRandCaliber(boolean caliber){
        if (caliber){
            setCaliber(Caliber.CALIBER_7);
        }else {
            setCaliber(Caliber.CALIBER_5);
        }
    }

    public void setRandHit(Caliber caliber, boolean zoom){
        int hitRate = 60;
        int zoomRate;
        if(caliber.equals(Caliber.CALIBER_7)){
            hitRate -= 10;
        }else {
            hitRate += 15;
        }

        if (zoom){
            zoomRate = random.nextInt(11);
            zoomRate += 5;
            hitRate += zoomRate;
        }
        setHitRate(hitRate);
    }

    public void setRandDamage(Caliber caliber){
        int damage = 20;
        if(caliber.equals(Caliber.CALIBER_7)){
            damage += 10;
            setDamageRate(damage);
        }
        setDamageRate(damage);
    }
}
