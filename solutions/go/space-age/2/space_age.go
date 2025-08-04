// Package space converts an age in seconds to age on other planets.
package space

type Planet string

const (
	Earth       Planet  = "Earth"
	Mercury     Planet  = "Mercury"
	Venus       Planet  = "Venus"
	Mars        Planet  = "Mars"
	Jupiter     Planet  = "Jupiter"
	Saturn      Planet  = "Saturn"
	Uranus      Planet  = "Uranus"
	Neptune     Planet  = "Neptune"
	EarthConv   float64 = 31557600
	MercuryConv float64 = 0.2408467
	VenusConv   float64 = 0.61519726
	MarsConv    float64 = 1.8808158
	JupiterConv float64 = 11.862615
	SaturnConv  float64 = 29.447498
	UranusConv  float64 = 84.016846
	NeptuneConv float64 = 164.79132
)

// Age returns its argument seconds as years on the argument planet
func Age(seconds float64, planet Planet) float64 {
	switch planet {
	case Mercury:
		return seconds / EarthConv / MercuryConv
	case Venus:
		return seconds / EarthConv / VenusConv
	case Mars:
		return seconds / EarthConv / MarsConv
	case Jupiter:
		return seconds / EarthConv / JupiterConv
	case Saturn:
		return seconds / EarthConv / SaturnConv
	case Uranus:
		return seconds / EarthConv / UranusConv
	case Neptune:
		return seconds / EarthConv / NeptuneConv
	default:
		return seconds / EarthConv
	}
}
