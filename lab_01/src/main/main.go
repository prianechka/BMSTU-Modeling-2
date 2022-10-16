package main

import (
	"fmt"
	"lab_01/pkg/distribution"
	"lab_01/pkg/plots"
)

const (
	ERLAND  = "распределения Эрланга (K, θ)"
	UNIFORM = "равномерного распределения (A, B)"
	DENSITY = "плотности"
	FUNC    = "функции"
)

func main() {
	var X1, X2 float64 = -2, 4
	var A, B float64 = 0, 3
	err, uniformDistribution := distribution.CreateUniformDistribution(A, B)
	//err, erlangDistribution := distribution.CreateErlangDistribution(2, 3)
	if err == nil {
		err = plots.PlotFunction(uniformDistribution, FUNC, UNIFORM, X1, X2)
	}

	if err != nil {
		fmt.Printf("%v", err)
	}
}
