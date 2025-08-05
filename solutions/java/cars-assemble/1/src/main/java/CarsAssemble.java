public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        double productionRate = 221;
        double productionRate90 = productionRate * 0.9;
        double productionRate80 = productionRate * 0.8;
        double productionRate77 = productionRate * 0.77;

        if (speed >= 1 && speed <= 4) {
            return productionRate * speed;
        } else if (speed >= 5 && speed <= 8) {
            return productionRate90 * speed;
        } else if (speed == 9) {
            return productionRate80 * speed;
        } else if (speed == 10) {
            return productionRate77 * speed;
        }
        return 0;
    }

    public int workingItemsPerMinute(int speed) {
        double productPerHour = productionRatePerHour(speed);
        return (int) (productPerHour / 60);
    }
}
