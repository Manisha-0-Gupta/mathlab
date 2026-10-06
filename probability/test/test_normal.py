from probability.normal import NormalDistribution
import math


def test_valid_parameters():
      NormalDistribution(0, 1)
      NormalDistribution(170, 10)
      NormalDistribution(-5, 2.5)


def test_invalid_sigma():
      for value in [0, -1, -0.5]:
            try:
                  NormalDistribution(0, value)
                  assert False
            except ValueError:
                  pass


def test_pdf():
      d = NormalDistribution(0, 1)

      # Standard normal PDF at 0
      assert math.isclose(
            d.pdf(0),
            1 / math.sqrt(2 * math.pi),
            rel_tol=1e-9
            )

      # Symmetry
      assert math.isclose(d.pdf(-1), d.pdf(1))

      # Density decreases away from the mean
      assert d.pdf(0) > d.pdf(1) > d.pdf(2)

def test_pdf_symmetry_around_mean():
      d = NormalDistribution(170, 10)

      assert math.isclose(d.pdf(160), d.pdf(180))
      assert math.isclose(d.pdf(150), d.pdf(190)) 

def test_cdf():
      d = NormalDistribution(0, 1)

      assert math.isclose(d.cdf(0), 0.5, rel_tol=1e-5)

      assert math.isclose(
            d.cdf(1),
            0.8413447,
            rel_tol=1e-5
            )

      assert math.isclose(
            d.cdf(2),
            0.9772499,
            rel_tol=1e-5
            )


def test_cdf_symmetry():
      d = NormalDistribution(0, 1)

      assert math.isclose(
            d.cdf(-1),
            1 - d.cdf(1),
            rel_tol=1e-5
            )


def test_cdf_boundaries():
      d = NormalDistribution(0, 1)

      assert d.cdf(-10) == 0
      assert d.cdf(10) == 1


def test_statistics():
      d = NormalDistribution(170, 10)

      assert math.isclose(d.expected_value(), 170)
      assert math.isclose(d.variance(), 100)
      assert math.isclose(d.standard_deviation(), 10)


