import java.util.ArrayList;

public class Building extends Housing {
    ArrayList<Housing>floors=new ArrayList<>();
    Building(String name){
        this.name=name;
    }

    int addFloors(Housing floor){
        this.floors.add(floor);
        return floors.size()-1;

    }
    
}
