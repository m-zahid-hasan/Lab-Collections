public class Saving implements IAccount{
    private int accountNumber;
    private int balance;

    Saving(int accountNumber,int ammount)
    {
        this.accountNumber=accountNumber;
        this.balance=ammount;
    }

    public void deposit(int ammount){
        balance+=ammount;
        System.out.println("Deposited successful");
        System.out.println("Total amount "+balance);
    }

    public void withdraw(int ammount){
        if(balance>=ammount){
            balance-=ammount;
            System.out.println("withdraw successful");
        }
        else {
            System.out.println("Insuffincient balance");
        }

    }

    public void transfer(IAccount to,int ammount){
        if(balance>=ammount){
            balance-=ammount;
            to.deposit(ammount);
            System.out.println("Transfer successful");
        }
        else {
            System.out.println("Insufficient balance");
        }
    }

    public int getAccountNumber(){
        return accountNumber;
    }
}