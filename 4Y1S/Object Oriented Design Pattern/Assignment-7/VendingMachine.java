public class VendingMachine {
    private int count;
    private State idlestate;
    private State hasonedolar;
    private State outofstock;
    private State currentstate;

    public VendingMachine(int count){
        this.count=count;
        idlestate=new IdleState();
        outofstock=new OutofStock();

        if(count>0){
            this.currentstate=idlestate;
        }
        else if(count==0) {
            this.currentstate=outofstock;
        }
    }



    public void setCount(int count){
        this.count=count;
    }

    public int getCount(){
        return this.count;
    }

    public void setState(State state){
        this.currentstate=state;
    }


     public void insertDollar() {
       currentstate.insertDollar(this);
    }
    public void ejectMoney() {
      currentstate.ejectMoney(this);
    }
    public void dispense() {
       currentstate.dispense(this);
    
}
}