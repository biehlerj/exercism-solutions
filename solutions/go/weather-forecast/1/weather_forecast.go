// Package weather provides tools to gather the weather forecast for various cities
// in Goblinocus.
package weather

// CurrentCondition represents the current weather conditions in a location.
var CurrentCondition string

// CurrentLocation represents the current location where the weather is being checked.
var CurrentLocation string

// Forecast returns a string of the current weather in the given location.
func Forecast(city, condition string) string {
	CurrentLocation, CurrentCondition = city, condition
	return CurrentLocation + " - current weather condition: " + CurrentCondition
}
