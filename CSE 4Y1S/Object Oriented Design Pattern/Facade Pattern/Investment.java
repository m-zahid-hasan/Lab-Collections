public class Investment implements IAccount{ 
    private int accountNumber;
    private int balance;

    Investment(int accountNumber,int ammount){
        this.accountNumber=accountNumber;
        this.balance=ammount;
    }

    public void deposit(int ammount){
        balance+=ammount;
        System.out.println("Deposited ammount");
        System.out.println("Total Amount "+balance);

    }
    public void withdraw(int ammount){
        if (balance>=ammount){
            accountNumber-=ammount;
            System.out.println("Withdraw successful");
        }
        else {
            System.out.println("Insuficient balance");
        }
    }
    public void transfer(IAccount to,int ammount){
        if(balance>=ammount){
            to.deposit(ammount);
            balance-=ammount;
            System.out.println("transfer successful");
        }
        else {
            System.out.println("Insufficient balance");
        }
    }
    public int getAccountNumber(){
        return accountNumber;
    }
}