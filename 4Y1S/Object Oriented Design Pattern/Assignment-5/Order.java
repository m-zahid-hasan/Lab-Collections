import java.util.ArrayList;

public class Order {
  
    ArrayList<Item>items=new ArrayList<Item>();


    void addItem(Item item){
        this.items.add(item);
    }
    
}