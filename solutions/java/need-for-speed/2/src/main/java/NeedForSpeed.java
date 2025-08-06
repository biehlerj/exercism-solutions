class NeedForSpeed {
    int speed;
    int batteryDrain;
    int battery = 100;
    int mileage = 0;

    NeedForSpeed(int speed, int batteryDrain) {
        this.speed = speed;
        this.batteryDrain = batteryDrain;
    }

    public boolean batteryDrained() {
        return this.battery - this.batteryDrain < 0;
    }

    public int distanceDriven() {
        return this.mileage;
    }

    public void drive() {
        if (!this.batteryDrained()) {
            this.mileage += this.speed;
            this.battery -= this.batteryDrain;
        }
    }

    public static NeedForSpeed nitro() {
        return new NeedForSpeed(50, 4);
    }
}

class RaceTrack {
    int distance;

    RaceTrack(int distance) {
        this.distance = distance;
    }

    public boolean canFinishRace(NeedForSpeed car) {
        int batteryDrainedPerDrive = 100 / car.batteryDrain;
        return this.distance <= batteryDrainedPerDrive * car.speed;
    }
}
