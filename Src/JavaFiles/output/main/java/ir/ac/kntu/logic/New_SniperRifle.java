package ir . ac . kntu . logic ; import java . util . Random ; public class New_SniperRifle extends New_Rifle { private Random random = new Random ( ) ; public New_SniperRifle ( boolean New_caliber , boolean New_zoom ) { New_setZoom ( New_zoom ) ; New_setRifleType ( New_RifleType . New_SNIPER ) ; New_setRandCaliber ( New_caliber ) ; New_Caliber New_caliber1 = New_getCaliber ( ) ; New_setRandHit ( New_caliber1 , New_zoom ) ; New_setRandDamage ( New_caliber1 ) ; } public void New_setRandCaliber ( boolean New_caliber ) { if ( New_caliber ) { New_setCaliber ( New_Caliber . New_CALIBER_7 ) ; } else { New_setCaliber ( New_Caliber . New_CALIBER_5 ) ; } } public void New_setRandHit ( New_Caliber New_caliber , boolean New_zoom ) { int New_hitRate = 60 ; int New_zoomRate ; if ( New_caliber . equals ( New_Caliber . New_CALIBER_7 ) ) { New_hitRate -= 10 ; } else { New_hitRate += 15 ; } if ( New_zoom ) { New_zoomRate = random . nextInt ( 11 ) ; New_zoomRate += 5 ; New_hitRate += New_zoomRate ; } New_setHitRate ( New_hitRate ) ; } public void New_setRandDamage ( New_Caliber New_caliber ) { int New_damage = 20 ; if ( New_caliber . equals ( New_Caliber . New_CALIBER_7 ) ) { New_damage += 10 ; New_setDamageRate ( New_damage ) ; } New_setDamageRate ( New_damage ) ; } }