import java.util.ArrayList;

public class Floor extends Housing {

    ArrayList<Housing>rooms=new ArrayList<>();
    Floor(String name){
        this.name=name;
    }

    int addRoom(Housing room){
        this.rooms.add(room);
        return rooms.size()-1;
    }  
}
