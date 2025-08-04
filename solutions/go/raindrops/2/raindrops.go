package raindrops

import "strconv"

// Convert takes in a number and turns it into rain language
func Convert(number int) string {
	var rain string
	if number%3 == 0 {
		rain += "Pling"
	}
	if number%5 == 0 {
		rain += "Plang"
	}
	if number%7 == 0 {
		rain += "Plong"
	}
	if rain != "" {
		return strconv.Itoa(number)
	}
	return rain
}
