public class main {
    public static void main(String[] args){
        System.out.println("Hello" + "World");
    }
    public void test(){
        int x = 5;
        if (x == 5){
            System.out.println("X is 5");
        }else if (x == 6){
            System.out.println("X is 6");
        }else{
            System.out.println("X is not 5 or 6");
        }
        for (int i = 0; i < x; i++){
            System.out.println(i);
        }
        int i = 0;
        while(i < x){
            System.out.println(i);
            i++;
        }
    }
}