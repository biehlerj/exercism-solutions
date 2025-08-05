public class JedliksToyCar {
    public int battery = 100;
    public int meters = 0;

    public static JedliksToyCar buy() {
        return new JedliksToyCar();
    }

    public String distanceDisplay() {
        return "Driven " + this.meters + " meters";
    }

    public String batteryDisplay() {
        if (battery == 0)
            return "Battery empty";
        return "Battery at " + this.battery + "%";
    }

    public void drive() {
        if (this.battery == 0)
            return;
        this.battery--;
        this.meters += 20;
    }
}
