public class OutofStock implements State{

    public void insertDollar(VendingMachine vendingMachine){
        System.out.println("out of stock");

    }

    public void ejectMoney(VendingMachine vendingMachine){
        System.out.println("Out of stock");
    }

    public void dispense(VendingMachine vendingMachine){
        System.out.println("out of stock");
    }
}