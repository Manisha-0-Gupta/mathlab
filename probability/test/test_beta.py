from probability.beta import BetaDistribution
import math

def test_valid_parameters():

      BetaDistribution(1,1)
      BetaDistribution(2,3)
      BetaDistribution(1,9)

def test_invalid_parameters():
      for alpha,beta in [(0,0),(1,0),(0,1),(-1,1),(1,-1)]:

            try:
                  BetaDistribution(alpha,beta)
                  assert False
            except ValueError:
                  pass

def test_pdf_uniform_special_case():
      d = BetaDistribution(1,1)

      assert math.isclose(d.pdf(0.2),1)
      assert math.isclose(d.pdf(0.5),1)
      assert math.isclose(d.pdf(0.8),1)

def test_pdf_boundaries():
      d = BetaDistribution(2,3)

      assert d.pdf(-1) == 0
      assert d.pdf(2) == 0

def test_statistics():
      d = BetaDistribution(2,3)

      assert math.isclose(d.expected_value(),0.4)
      assert math.isclose(d.variance(),0.04)
      assert math.isclose(d.standard_deviation(),0.2)

def test_cdf_uniform_special_case():
      d = BetaDistribution(1,1)

      assert math.isclose(d.cdf(0),0)
      assert math.isclose(d.cdf(0.25),0.25,rel_tol=1e-5)
      assert math.isclose(d.cdf(0.5),0.5,rel_tol=1e-5)
      assert math.isclose(d.cdf(0.75),0.75,rel_tol=1e-5)
      assert math.isclose(d.cdf(1),1)

def test_cdf_boundaries():
      d = BetaDistribution(2,3)

      assert d.cdf(-1) ==0
      assert d.cdf(2) == 1

def test_cdf_non_uniform():
      d = BetaDistribution(2,2)

      assert math.isclose(d.cdf(0.5), 0.5, rel_tol=1e-8)
      assert math.isclose(d.cdf(0.25), 0.15625, rel_tol=1e-8)

def test_cdf_monotonicity():

      d = BetaDistribution(2,3)

      assert d.cdf(0.25) < d.cdf(0.75)