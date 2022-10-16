package distribution

import "errors"

type UniformDistribution struct {
	A, B float64
}

func CreateUniformDistribution(A, B float64) (error, *UniformDistribution) {
	switch {
	case A > B || (A == B && A == 0):
		return errors.New("bad bounds"), nil
	default:
		return nil, &UniformDistribution{A: A, B: B}
	}
}

func (ud *UniformDistribution) ProbabilityDensityInPoint(x float64) (result float64) {
	if x >= ud.A && x <= ud.B {
		result = 1 / (ud.B - ud.A)
	} else {
		result = 0
	}
	return result
}

func (ud *UniformDistribution) DistributionFunctionInPoint(x float64) (result float64) {
	switch {
	case x < ud.A:
		result = 0
	case x > ud.B:
		result = 1
	default:
		result = (x - ud.A) / (ud.B - ud.A)
	}
	return result
}

func (ud *UniformDistribution) ProbabilityDensity(A, B float64) []float64 {
	result := make([]float64, EMPTY)
	for i := A; i < B; i += DELTA {
		result = append(result, ud.ProbabilityDensityInPoint(i))
	}
	return result
}

func (ud *UniformDistribution) DistributionFunction(A, B float64) []float64 {
	result := make([]float64, EMPTY)
	for i := A; i < B; i += DELTA {
		result = append(result, ud.DistributionFunctionInPoint(i))
	}
	return result
}

func (ud *UniformDistribution) GetParams() (A, B float64) {
	return ud.A, ud.B
}
