package ir . ac . kntu . logic ; import java . util . ArrayList ; import java . util . Random ; public class New_StartGame { Random random = new Random ( ) ; private ArrayList < New_Soldier > New_a ; private ArrayList < New_Soldier > New_b ; private New_Print New_print = new New_Print ( ) ; public New_StartGame ( ArrayList < New_Soldier > New_a , ArrayList < New_Soldier > New_b ) { this . New_a = new ArrayList < > ( New_a ) ; this . New_b = new ArrayList < > ( New_b ) ; } public void New_shoot ( New_Soldier New_a , New_Soldier New_b ) { int hit = random . nextInt ( 100 ) + 1 ; System . out . println ( "Fight:" ) ; System . out . println ( "Soldier A Attacks B" ) ; if ( hit <= New_a . New_getHitRate ( ) ) { New_b . New_setHealth ( New_b . New_getHealth ( ) - New_a . New_getDamage ( ) ) ; System . out . println ( "The Shot Hit:              Dmg:" + New_a . New_getDamage ( ) ) ; } else { System . out . println ( "The Shot Missed!" ) ; } hit = random . nextInt ( 100 ) + 1 ; System . out . println ( "Soldier B Attacks A" ) ; if ( hit <= New_b . New_getHitRate ( ) ) { New_a . New_setHealth ( New_a . New_getHealth ( ) - New_b . New_getDamage ( ) ) ; System . out . println ( "The Shot Hit:              Dmg:" + New_b . New_getDamage ( ) ) ; } else { System . out . println ( "The Shot Missed!" ) ; } New_print . New_line ( ) ; } public void New_shoot2 ( ) { ArrayList < Integer > New_idA = new ArrayList < > ( ) ; ArrayList < Integer > New_idB = new ArrayList < > ( ) ; for ( int New_i = 0 ; New_i < New_a . size ( ) ; New_i ++ ) { New_idA . add ( New_i , New_i + 1 ) ; New_idB . add ( New_i , New_i + 1 ) ; } while ( New_a . size ( ) != 0 && New_b . size ( ) != 0 ) { int New_randSoliderA = random . nextInt ( New_a . size ( ) ) ; int New_randSoliderB = random . nextInt ( New_b . size ( ) ) ; System . out . println ( "**ARENA**" ) ; System . out . println ( "Team A Solider: " ) ; New_print . New_printSoldier ( New_a . get ( New_randSoliderA ) , New_randSoliderA + 1 ) ; System . out . println ( "Team B Solider: " ) ; New_print . New_printSoldier ( New_b . get ( New_randSoliderB ) , New_randSoliderB + 1 ) ; New_print . New_line ( ) ; New_shoot ( New_a . get ( New_randSoliderA ) , New_b . get ( New_randSoliderB ) ) ; if ( New_a . get ( New_randSoliderA ) . New_getHealth ( ) < 0 ) { System . out . println ( "Solider Of Side A Been Killed!             Id: " + New_idA . get ( New_randSoliderA ) ) ; New_a . remove ( New_randSoliderA ) ; New_idA . remove ( New_randSoliderA ) ; } if ( New_b . get ( New_randSoliderB ) . New_getHealth ( ) < 0 ) { System . out . println ( "Solider Of Side B Been Killed!             Id: " + New_idB . get ( New_randSoliderB ) ) ; New_b . remove ( New_randSoliderB ) ; New_idB . remove ( New_randSoliderB ) ; } if ( New_a . size ( ) != 0 && New_b . size ( ) != 0 ) { New_print . New_gameNotFinished ( ) ; New_pressAnyKey ( ) ; } } New_print . New_gameFinished ( New_a , New_b ) ; } public void New_pressAnyKey ( ) { System . out . println ( "Press Any Key To Continue..." ) ; try { System . in . read ( ) ; System . in . read ( ) ; } catch ( Exception e ) { } } }