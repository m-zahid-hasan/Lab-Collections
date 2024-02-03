

public class Main {
    public static void main(String[] args) {
        Petshop petShop=new Petshop("Animal house");
        Dog dog;
        Cat cat;

        String [] dogs={"Dog1","Dog2","Dog3","Dog4"};
        String [] cats={"Cat1","Cat2","Cat3","Cat4"};
        for(int i=0;i<dogs.length;i++){
            dog=new Dog(dogs[i],"deshi");
            cat=new Cat(dogs[i],"bidesi");

            petShop.addPet(cat);
            petShop.addPet(dog);
        }

        for(Animal animal:petShop.peList){
            System.out.println(animal.name);
        }

        petShop.sellPet("Dog1");
        petShop.sellPet("dog5");
        petShop.sellPet("cat3");
        petShop.sellPet("cat5");

    }
    
}
