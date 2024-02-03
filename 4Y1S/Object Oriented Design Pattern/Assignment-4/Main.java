

public class Main {
    public static void main(String[] args) {
        Building building=new Building("habibur hall");

        Floor floor1=new Floor("1st floor");
        Floor floor2=new Floor("2nd floor");


        Room r11=new Room("101");
        Room r12=new Room("102");
        Room r13=new Room("104");
        Room r21= new Room("201");
        Room r22=new Room("203");
        Room r23=new Room("205");


        int i11=floor1.addRoom(r11);
        int i12=floor1.addRoom(r12);
        int i13=floor1.addRoom(r13);
        int i21=floor2.addRoom(r21);
        int i22=floor2.addRoom(r22);
        int i23=floor2.addRoom(r23);

        int if1=building.addFloors(floor1);
        int if2=building.addFloors(floor2);

        building.enter();
        Floor floor=(Floor)(building.floors.get(if1));
        floor.enter();
        Room room=(Room)(floor.rooms.get(i11));
        room.enter();
        room.exit();


        

        
    }

    
}
