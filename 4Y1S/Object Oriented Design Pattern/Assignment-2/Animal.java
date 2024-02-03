abstract class Animal{
    String name,type;
    void eat(){
        System.out.println(this.name+"eating");
    }
    abstract void sound();

}