public class Chequing implements IAccount{

    private int accountNumber;
    private int balance;

    Chequing( int accountNumber,int ammount){
        this.accountNumber=accountNumber;
        this.balance=ammount;
    }

    public void deposit(int ammount){
        System.out.println("deposited ammount");
        balance+=ammount;
    }
    public void withdraw(int ammount){
        if(balance>=ammount){
            System.out.println("Withdraw successfull");
            balance-=ammount;
        }
        else {
            System.out.println("Insufficient balance");
        }
    }
    public void transfer(IAccount to,int ammount){
        if (balance>=ammount){
            balance-=ammount;
            to.deposit(ammount);
            System.out.println("Transfer Successful");
        }
        else {
            System.out.println("Insufficinet balance");
        }
    }

    public int getAccountNumber(){
        return accountNumber;
    }
}