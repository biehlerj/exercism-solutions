package cars

// CalculateWorkingCarsPerHour calculates how many working cars are
// produced by the assembly line every hour.
func CalculateWorkingCarsPerHour(productionRate int, successRate float64) float64 {
	successRateAsDecimal := successRate / 100.0

	return float64(productionRate) * successRateAsDecimal
}

// CalculateWorkingCarsPerMinute calculates how many working cars are
// produced by the assembly line every minute.
func CalculateWorkingCarsPerMinute(productionRate int, successRate float64) int {
	return int(CalculateWorkingCarsPerHour(productionRate, successRate)) / 60
}

// CalculateCost works out the cost of producing the given number of cars.
func CalculateCost(carsCount int) uint {
	carsBy10 := carsCount / 10
	carsRemaining := carsCount % 10
	carsBy10Cost := carsBy10 * 95000
	carsRemainingCost := carsRemaining * 10000

	return uint(carsBy10Cost) + uint(carsRemainingCost)
}
