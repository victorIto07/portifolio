import java.util.function.Function;

public class MyAction{
    public String name;
    public Function<Void,Integer> exec;

    MyAction(String name, Function<Void, Integer> f){
        this.name = name;
        this.exec = f;
    }

}