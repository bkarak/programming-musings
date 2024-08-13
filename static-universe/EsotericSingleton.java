

public class EsotericSingleton {
    private static EsotericSingleton defaultInstance;

    static {
        defaultInstance = new EsotericSingleton();
    }

    private EsotericSingleton() {

    }

    public static EsotericSingleton getInstance() {
        return defaultInstance;
    }
}
