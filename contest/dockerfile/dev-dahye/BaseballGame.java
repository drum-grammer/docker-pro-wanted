import java.util.Scanner;
class DuplicateException extends Exception{}
public class BaseballGame{
    public static int[] randomNumber(){
        int[] random_number = new int[3];
        for(int i=0; i<3; i++){
            int n = (int)(Math.random()*9);
            random_number[i] = n;
            for(int j=0; j<i; j++){
                if(random_number[i]==random_number[j]){
                    i--;
                    continue;
                } 
            }
        }
        return random_number;
    }
    public static int[] checkAnswer(int[] answer, int[] input) throws NumberFormatException{
        int sCnt = 0; //strike cnt, ball cnt
        int bCnt = 0;
        for(int i=0; i<3; i++){
            if(input[i]>9 || input[i]<0){
                throw new NumberFormatException();
            }
            for(int j=0; j<3; j++){
                if(input[i]==answer[j]){
                    if(i==j){
                        sCnt++;
                    }
                    else {
                        bCnt++;
                    }
                }
            }
        }
        int[] ballCnt = {sCnt,bCnt}; 
        return ballCnt;
    }

    public static void main(String[] args){
        System.out.println("\n\n");
        System.out.println("########BASEBALL GAME START########");
        System.out.println("    * 3-digit number 0 ~ 9/ duplicate X");

        int[] answer = randomNumber();

        System.out.println("    * If you want to end the game enter (q/Q)");
        System.out.println("    * Enter 3-digit number with spaces ");

        int tryCnt = 0;

        Scanner scan = new Scanner(System.in);
        while(true){
            try{
                System.out.print(": ");
                String numbers = scan.nextLine();
                tryCnt++;

                if(numbers.equals("q")||numbers.equals("Q")){
                    break;
                } 

                String[] number = numbers.split(" ");
                if(number.length!=3){
                    throw new Exception();
                }
                if(number[0].equals(number[1]) || number[0].equals(number[2]) || number[1].equals(number[2])){
                    throw new DuplicateException();
                }
                int[] intNumber = {Integer.parseInt(number[0]),Integer.parseInt(number[1]),Integer.parseInt(number[2])};
                int[] ballCnt = checkAnswer(answer,intNumber);
                if(ballCnt[0]==0 && ballCnt[1]==0){
                    System.out.println("Out " + tryCnt + " Round");
                }else{
                    System.out.println(ballCnt[0]+"S "+ballCnt[1]+"B   " + tryCnt + " Round");
                }

                if(tryCnt>=9){ //LOSE
                    System.out.println("\n\n    ### GAME OVER ;-( ");
                    System.out.println("ANSWER : " + answer[0] + " " + answer[1] + " " + answer[2]);
                    System.out.println("    * New game enter any key / End the game enter (q/Q)");
                    String key = scan.nextLine();
                    if(key.equals("q")||key.equals("Q")) {
                        break;
                    } else{
                        System.out.println("\n\n");
                        answer = randomNumber();
                        tryCnt = 0;
                        System.out.println("\n\n");
                        System.out.println("########BASEBALL GAME START########");
                        continue;
                    }
                }
                if(ballCnt[0]==3){//win
                    System.out.println("\n\n    ### YOU WIN~~!");
                    System.out.println("ANSWER : " + answer[0] + " " + answer[1] + " " + answer[2]);
                    System.out.println("YOUR TRY COUNT : " + tryCnt);
                    System.out.println("\n    * New game enter any key / End the game enter (q/Q)");
                    String key = scan.nextLine();
                    if(key.equals("q")||key.equals("Q")) {
                        break;
                    } else{
                        System.out.println("\n\n");
                        answer = randomNumber();
                        tryCnt = 0;
                        System.out.println("\n\n");
                        System.out.println("########BASEBALL GAME START########");
                        continue;
                    }
                }
            } catch(NumberFormatException e){ //not number
                System.out.println("    * only enter number 0~9");
                tryCnt--;
            } catch(DuplicateException e){ //not duplicate number 
                System.out.println("    * not duplicate number");
                tryCnt--;
            } catch(Exception e){ //not 3-digit number 
                System.out.println("    * only enter 3-digit number");
                tryCnt--;
            } 


        }

        System.out.println("\n\n");
        System.out.println("    * Good Bye~");
        System.out.println("########END OF GAME########");
    }
}