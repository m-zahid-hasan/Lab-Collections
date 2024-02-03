import java.util.ArrayList;
import java.util.Hashtable;

public class Warehouse implements Iorder {
    Hashtable<String,Integer>stocks=new Hashtable<String,Integer>();

    void addItem(Item item){
        this.stocks.put(item.name,item.count);

    }
    


    int getItemCount(Item item){
        if(stocks.containsKey(item.name)){
            return stocks.get(item.name);
        }
        return 0;
    }
    public void fullfilOrder(Order order){
        for(Item item:order.items){
            int x=stocks.get(item.name);
            stocks.put(item.name,x-item.count);
        }
    }
}
