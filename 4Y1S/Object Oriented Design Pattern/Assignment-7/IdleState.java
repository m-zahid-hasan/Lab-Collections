public class IdleState implements State{
    
    public void  insertDollar(VendingMachine vendingMachine){
        System.out.println("Dollar inserted");


       State state=new HasOneDollarState();
        vendingMachine.setState(state);
    }
    public void ejectMoney(VendingMachine vendingMachine){
        System.out.println("no money has to return");
    }

    public void dispense(VendingMachine vendingMachine){
        System.out.println("Required money");

    }

}