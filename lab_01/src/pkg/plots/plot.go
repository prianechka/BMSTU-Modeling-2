package plots

import (
	"errors"
	"fmt"
	"gonum.org/v1/plot"
	"gonum.org/v1/plot/plotter"
	"gonum.org/v1/plot/vg"
	"image/color"
	"lab_01/pkg/distribution"
)

type MyDistribution struct {
	dist distribution.Distribution
	A, B float64
	X, Y []float64
}

func findMinAndMax(a []float64) (min float64, max float64) {
	min = a[0]
	max = a[0]
	for _, value := range a {
		if value < min {
			min = value
		}
		if value > max {
			max = value
		}
	}
	return min, max
}

type MyTick struct{}

func (mt MyTick) Ticks(min, max float64) (result []plot.Tick) {
	delta := (max - min) / 6
	for i := min; i <= max; i += delta {
		result = append(result, plot.Tick{
			Value: i,
			Label: fmt.Sprintf("%.2f", i),
		})
	}
	return result
}

func InitMyDistribution(dist distribution.Distribution, FuncName string, X1, X2 float64) MyDistribution {
	var Y []float64
	switch FuncName {
	case DENS:
		Y = dist.ProbabilityDensity(X1, X2)
	case FUNC:
		Y = dist.DistributionFunction(X1, X2)
	default:
		Y = nil
	}
	return MyDistribution{
		dist: dist,
		A:    X1,
		B:    X2,
		X:    MakeXCoords(X1, X2),
		Y:    Y,
	}
}

func MakeXCoords(A, B float64) []float64 {
	X := make([]float64, EMPTY)
	for i := A; i <= B; i += DELTA {
		X = append(X, i)
	}
	return X
}

func (myDist MyDistribution) Len() int {
	return len(myDist.X)
}

func (myDist MyDistribution) XY(index int) (x, y float64) {
	return myDist.X[index], myDist.Y[index]
}

func PlotFunction(dist distribution.Distribution, FuncName, DistName string, A, B float64) error {
	var distribute = InitMyDistribution(dist, FuncName, A, B)
	return Plot(distribute, FuncName, DistName)
}

func Plot(distribute MyDistribution, FuncName, DistName string) error {
	p := plot.New()

	P1, P2 := distribute.dist.GetParams()

	p.Title.Text = fmt.Sprintf("График %s %s с параметрами (%.2f, %.2f)", FuncName, DistName, P1, P2)
	p.Add(plotter.NewGrid())
	p.X.Label.TextStyle.Font.Size = FONTSIZE
	p.Y.Label.TextStyle.Font.Size = FONTSIZE
	p.X.Tick.Label.Font.Size = FONTSIZE - 2
	p.Y.Tick.Label.Font.Size = FONTSIZE
	p.Title.TextStyle.Font.Size = FONTSIZE
	p.X.Label.Text = XLABEL
	p.Y.Label.Text = YLABEL
	YMin, YMax := findMinAndMax(distribute.Y)
	p.Y.Max = YMax
	p.Y.Min = YMin
	p.X.Tick.Marker = MyTick{}
	p.Y.Tick.Marker = MyTick{}

	l, err := plotter.NewLine(plotter.XYer(distribute))
	l.LineStyle.Width = vg.Points(1)
	l.LineStyle.Color = color.RGBA{B: 255, A: 255}
	p.Legend.Add("График "+FUNC, l)
	p.Legend.TextStyle.Font.Size = FONTSIZE
	p.Legend.XOffs = -20
	p.Legend.YOffs = 400
	p.Add(l)

	if err == nil {
		if err := p.Save(WIDTH, HEIGHT, "points.png"); err != nil {
			err = errors.New("bad saving")
		}
	}
	return err
}
