import  java.util.Hashtable;

public class Facade{
    private Hashtable<Integer,IAccount>bankAccount;

    Facade(){
        this.bankAccount=new Hashtable<Integer,IAccount>();
    }

    public int createAccount(String accountType,int initialAmmount,int accountNumber){
        IAccount account=null;
        
        switch (accountType) {
            case "Saving":
                account=new Saving(accountNumber, initialAmmount);
                break;
            case "Chequing":
                account=new Chequing(accountNumber, initialAmmount);
                break;
            case "Investment":
                 account=new Investment(accountNumber, initialAmmount);
                 break;
        
            default:
                break;
        }
        if(account!=null){
            bankAccount.put(accountNumber, account);
            return accountNumber;
        }


        return 0;
    }

    public void deposit(int accountNumber,int ammount){
       IAccount a= bankAccount.get(accountNumber);
       a.deposit(ammount);
    }

    public void withdraw(int accountNumber,int ammount){
        IAccount account=bankAccount.get(accountNumber);
        account.withdraw(ammount);
    }

    public void transfer(int from,int to,int amount){
        IAccount fromm=bankAccount.get(from);
        IAccount too=bankAccount.get(to);
        fromm.transfer(too, amount);
    }

}
