package ir.ac.kntu.logic;




public class AssaultRifle extends Rifle{


    public AssaultRifle(boolean caliber){
        setRifleType(RifleType.ASSAULT);
        setRandCaliber(caliber);
        Caliber caliber1 = getCaliber();
        setRandHit(caliber1);
        setRandDamage(caliber1);
    }

    public void setRandCaliber(boolean caliber){
        if (caliber){
            setCaliber(Caliber.CALIBER_7);
        }else {
            setCaliber(Caliber.CALIBER_5);
        }
    }

    public void setRandHit(Caliber caliber){
        int hitRate = 50;
        if(caliber.equals(Caliber.CALIBER_7)){
            hitRate -= 10;
        }else {
            hitRate += 15;
        }
        setHitRate(hitRate);
    }

    public void setRandDamage(Caliber caliber){
        int damage = 10;
        if(caliber.equals(Caliber.CALIBER_7)){
            damage += 10;
            setDamageRate(damage);
        }
        setDamageRate(damage);
    }
}
