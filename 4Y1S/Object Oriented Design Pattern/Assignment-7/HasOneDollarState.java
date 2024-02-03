public class HasOneDollarState implements State{

    public void insertDollar(VendingMachine vendingMachine){
        System.out.println("Has already dollar");
    }
    public void ejectMoney(VendingMachine vendingMachine){
        System.out.println("Returning money");
        State state=new IdleState();
        vendingMachine.setState(state);

    }

    public void dispense(VendingMachine vendingMachine){
        System.out.println("Dispense the product");

        if (vendingMachine.getCount()>1){
            State state=new IdleState();
            vendingMachine.setState(state);
            vendingMachine.setCount(vendingMachine.getCount()-1);
        }
        else {
            State state=new OutofStock();
            vendingMachine.setState(state);
            vendingMachine.setCount(0);
        }
    }
}