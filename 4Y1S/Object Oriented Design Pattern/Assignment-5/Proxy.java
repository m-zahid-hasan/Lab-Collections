import java.util.ArrayList;

public class Proxy implements Iorder {
    ArrayList<Iorder>warehouses=new ArrayList<Iorder>();

    Warehouse warehouse;

    Proxy(Iorder warehouse){
        this.warehouses.add(warehouse);
    }


    public void fullfilOrder(Order order){
        for(Iorder warehouse:warehouses){
            Warehouse warehouse1=(Warehouse)warehouse;
            boolean flag=true;
            for(Item item:order.items){
                if(item.count>warehouse1.getItemCount(item))flag=false;
            }
            if(true){
                warehouse1.fullfilOrder(order);break;
            }
        }
    }
    
}
