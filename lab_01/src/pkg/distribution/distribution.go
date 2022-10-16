package distribution

type Distribution interface {
	ProbabilityDensityInPoint(x float64) (result float64)
	DistributionFunctionInPoint(x float64) (result float64)
	ProbabilityDensity(A, B float64) []float64
	DistributionFunction(A, B float64) []float64
	GetParams() (A, B float64)
}
