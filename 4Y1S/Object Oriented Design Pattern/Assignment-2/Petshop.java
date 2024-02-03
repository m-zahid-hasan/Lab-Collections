

import java.util.ArrayList;
import java.util.Hashtable;



public class Petshop {
    
    ArrayList<Animal>peList=new ArrayList<>();
   
    String shopname;
    Petshop(String shopname){
        this.shopname=shopname;
    }

    void addPet(Animal pet){
       peList.add(pet);
        
    }

    void sellPet(String name){
        boolean check =false;int i=-1;

        for(Animal pet:peList){
            i++;
            if(pet.name.equals(name)){check=true;break;}
        }

        if(check){System.out.println(name+ " selt the pet"); peList.remove(i);}
        else System.out.println("Pet not found");
    
    }
 
}
