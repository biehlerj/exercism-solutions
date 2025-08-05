public class SalaryCalculator {
    public double salaryMultiplier(int daysSkipped) {
        return daysSkipped < 5 ? 1.0 : 0.85;
    }

    public int bonusMultiplier(int productsSold) {
        return productsSold >= 20 ? 13 : 10;
    }

    public double bonusForProductsSold(int productsSold) {
        return bonusMultiplier(productsSold) == 13 ? productsSold * 13 : productsSold * 10;
    }

    public double finalSalary(int daysSkipped, int productsSold) {
        return (1000 + bonusForProductsSold(productsSold)) * salaryMultiplier(daysSkipped) <= 2000
                ? (1000 + bonusForProductsSold(productsSold)) * salaryMultiplier(daysSkipped)
                : 2000;
    }
}
