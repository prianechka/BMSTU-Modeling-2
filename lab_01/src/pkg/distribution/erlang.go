package distribution

import (
	"errors"
	"math"
)

type ErlangDistribution struct {
	K     int
	Alpha float64
}

func CreateErlangDistribution(K int, Alpha float64) (error, *ErlangDistribution) {
	switch {
	case K <= 0 || Alpha <= 0:
		return errors.New("bad params"), nil
	default:
		return nil, &ErlangDistribution{K: K, Alpha: Alpha}
	}
}

func lowGamma(x, a, b float64) (result float64) {
	var t float64 = 0
	for ; t < x; t += DELTA {
		result += math.Exp(-t/b) * math.Pow(t, a-1) * DELTA
	}
	return result
}

func (ed *ErlangDistribution) ProbabilityDensityInPoint(x float64) (result float64) {
	if x < 0 {
		result = 0
	} else {
		result = math.Pow(x, float64(ed.K)-1) * math.Exp(-x/ed.Alpha) /
			(math.Pow(ed.Alpha, float64(ed.K)) * math.Gamma(float64(ed.K)))
	}
	return result
}

func (ed *ErlangDistribution) DistributionFunctionInPoint(x float64) (result float64) {
	if x < 0 {
		result = 0
	} else {
		result = lowGamma(x, float64(ed.K), ed.Alpha) /
			(math.Pow(ed.Alpha, float64(ed.K)) * math.Gamma(float64(ed.K)))
	}
	return result
}

func (ed *ErlangDistribution) ProbabilityDensity(A, B float64) []float64 {
	result := make([]float64, EMPTY)
	for i := A; i < B; i += DELTA {
		result = append(result, ed.ProbabilityDensityInPoint(i))
	}
	return result
}

func (ed *ErlangDistribution) DistributionFunction(A, B float64) []float64 {
	result := make([]float64, EMPTY)
	for i := A; i < B; i += DELTA {
		result = append(result, ed.DistributionFunctionInPoint(i))
	}
	return result
}

func (ed *ErlangDistribution) GetParams() (A, B float64) {
	return float64(ed.K), ed.Alpha
}
