#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `brewerwall` package."""


import unittest
from click.testing import CliRunner

from brewerwall import brewerwall
from brewerwall import cli


class TestBrewerwall(unittest.TestCase):
    """Tests for `brewerwall` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def testABV(self):
        """Test Alcohol by Volume calculation."""
        self.assertEqual(7.319479429051208, abv(1.055, 1))
        self.assertEqual(None, abv(1, 1.055))
    
    def testABW(self):
        """Test Alochol by Weight calculation."""
        self.assertEqual(5.782388748950455, abw(1.055, 1))
        self.assertEqual(None, abw(1, 1.055))
    
    def testMCU(self):
        """Test Malt Color Unit calculation."""
        self.assertEqual(None, mcu(1, 1, 0))
        self.assertEqual(5, mcu(5, 5, 5))
        self.assertEqual(5.5, mcu(5.5, 5.5, 5.5))
    
    def testSRM(self):
        """Test Standard Reference Method calculation."""
        self.assertEqual(None, srm(7, 5, 0))
        self.assertEqual(5.668651803424155, srm(7, 5, 5))
        self.assertEqual(5.943353419684101, srm(7.5, 5.5, 5.5))
    
    def testAAU(self):
        """
        Test Alpha Acid Units.

        Based off Palmer's Calculation
        """
        self.assertEqual(9.600000000000001, aau(1.5, 6.4))
        self.assertEqual(4.6, aau(1, 4.6))
    
    def testUtilization(self):
        """Test hop utilization calculation."""
        self.assertEqual(0.08363227080582435, utilization(10, 1.050))
        self.assertEqual(0.30113013986478654, utilization(120, 1.030))
        self.assertEqual(0.0, utilization(0, 1.070))
        self.assertEqual(0.14780486892282785, utilization(45, 1.090))
    
    def testIBU(self):
        """
        Test International Bittering Units calculation.
        
        Based off Palmer's Calculation
        """
        self.assertEqual(25.365869680614512, ibu(6.4, 1.5, 60, 1.080, 5))
        self.assertEqual(6.03108750923272, ibu(4.6, 1, 15, 1.080, 5))
    
    def testPlato(self):
        """Test conversion from specific gravity to plato."""
        self.assertEqual(17.055185000000108, convertToPlato(1.070))
    
    def testRealExtract(self):
        """Test Reat Extract calculations."""
        self.assertEqual(6.216277095999994, realExtract(1.070, 1.015))
        self.assertEqual(None, realExtract(1.015, 1.070))
    
    def testCalories(self):
        """
        Test calories per 12 oz. serving calculation.
        
        Based on http://hbd.org/ensmingr/
        """
        self.assertEqual(234.97692128247783, calories(1.070, 1.015))
        self.assertEqual(None, calories(1.015, 1.070))
    
    def testAttenuation(self):
        """Test attenuation calculation."""
        self.assertEqual(0.7777777777777778, attenuation(1.054, 1.012))
        self.assertEqual(None, attenuation(1, 1.055))
    
    def testGravityCorrection(self):
        """Test gravity correction calculation."""
        self.assertEqual(1.0562227410997, gravityCorrection(100.4, 1.050, 60))
    
    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'brewerwall.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
