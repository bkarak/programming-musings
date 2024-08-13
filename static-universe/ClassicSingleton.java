

public class ClassicSingleton {
    private static ClassicSingleton defaultInstance;

    private ClassicSingleton() {
        // do the math here
    }

    public static ClassicSingleton getInstance() {
        if (ClassicSingleton.defaultInstance == null) {
            ClassicSingleton.defaultInstance = new ClassicSingleton();
        }

        return ClassicSingleton.defaultInstance;
    }
}