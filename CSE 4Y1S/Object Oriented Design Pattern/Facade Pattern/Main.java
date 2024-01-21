public class Main {
    public static void main(String[] args) {
        
        Facade object=new Facade();

        // Create account 101
        int number=object.createAccount("Saving", 100, 101);
        System.out.println(number); 
        object.deposit(101, 500);


        // Create account 202
        int num2=object.createAccount("Investment", 500, 202);
        System.out.println(num2);
        object.deposit(202, 1000);


        object.withdraw(101, 700); // wtiht  from account 101

        object.transfer(202, 101, 500);   // Transfer ammount from account 202,to 101


    }    
}
