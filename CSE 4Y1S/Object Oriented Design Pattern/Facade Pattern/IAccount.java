public interface IAccount{
    public void  deposit(int ammount);
    public void withdraw(int ammount);
    public void transfer(IAccount to,int ammount);
    public int getAccountNumber();
}