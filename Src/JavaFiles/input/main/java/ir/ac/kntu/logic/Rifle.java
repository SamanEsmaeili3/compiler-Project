package ir.ac.kntu.logic;

public class Rifle {
    private int hitRate;
    private int damageRate;
    private Caliber caliber;
    private RifleType rifleType;
    private boolean zoom = false;

    public void setHitRate(int hitRate) {
        this.hitRate = hitRate;
    }

    public void setDamageRate(int damageRate) {
        this.damageRate = damageRate;
    }

    public void setCaliber(Caliber caliber) {
        this.caliber = caliber;
    }

    public void setRifleType(RifleType rifleType) {
        this.rifleType = rifleType;
    }

    public void setZoom(boolean zoom) {
        this.zoom = zoom;
    }

    public int getHitRate() {
        return hitRate;
    }

    public int getDamageRate() {
        return damageRate;
    }

    public Caliber getCaliber() {
        return caliber;
    }

    public RifleType getRifleType() {
        return rifleType;
    }

    public boolean getZoom(){
        return zoom;
    }
}
