// Package space converts an age in seconds to age on other planets.
package space

// Age returns its argument seconds as years on the argument planet
func Age(seconds float64, planet string) float64 {
	var secondsConversion = []struct {
		planet Planet
		secs   float64
	}{
		{
			"Earth",
			365.25,
		},
		{
			"Mercury",
			0.2408467,
		},
		{
			"Venus",
			0.61519726,
		},
		{
			"Mars",
			1.8808158,
		},
		{
			"Jupiter",
			11.862615,
		},
		{
			"Saturn",
			29.447498,
		},
		{
			"Uranus",
			84.016846,
		},
		{
			"Neptune",
			164.79132,
		},
	}

	for _, secsConv := range secondsConversion {
		if secsConv.planet == planet {
			age := secsConv.secs * seconds
			return age
		}
	}
	return -1
}
