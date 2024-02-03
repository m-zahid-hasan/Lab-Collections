public class Main {
    public static void main(String args[]){

        String []product={"Soup","Chiken","tootpast","banana","jackfruth","mango"};

        Warehouse warehouse=new Warehouse();
        Item item;
        for(int i=0;i<product.length;i++){
            item=new Item(product[i], 100);
            warehouse.addItem(item);
        }
        
        Order order=new Order();
        for(int i=0;i<4;i++){
            item=new Item(product[i], 10);
            order.addItem(item);
        }

        Proxy proxy=new Proxy(warehouse);
        proxy.fullfilOrder(order);
        for(int i=0;i<warehouse.stocks.size();i++){
            System.out.println(warehouse.stocks.get(product));
        }



    }
    
}
