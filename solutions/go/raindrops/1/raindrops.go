package raindrops

import "strconv"

// Convert takes in a number and turns it into rain language
func Convert(number int) string {
	strings := []string{
		"Pling",
		"Plang",
		"Plong",
	}
	var rain string
	if number%3 == 0 {
		rain += strings[0]
	}
	if number%5 == 0 {
		rain += strings[1]
	}
	if number%7 == 0 {
		rain += strings[2]
	}
	if rain != "" {
		return rain
	}
	rain = strconv.Itoa(number)
	return rain
}
