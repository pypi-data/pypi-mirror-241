#!/usr/bin/env python
""" generated source for module ChiSquareTerm """
# 
#  * Java Statistics.  A java library providing power/sample size estimation for 
#  * the general linear model.
#  * 
#  * Copyright (C) 2010 Regents of the University of Colorado.  
#  *
#  * This program is free software; you can redistribute it and/or
#  * modify it under the terms of the GNU General Public License
#  * as published by the Free Software Foundation; either version 2
#  * of the License, or (at your option) any later version.
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#  
# package: edu.cudenver.bios.distribution
# 
#  * Pojo describing a chi-square term for use with calculating the
#  * distribution of a sum of weighted non-central chi-squares 
#  * 
#  * @see WeightedSumOfNoncentralChiSquaresDistribution
#  * @author Sarah Kreidler
#  *
#  
class ChiSquareTerm(object):
    """ generated source for class ChiSquareTerm """
    #  weight 
    lambda_ = float()

    #  non-centrality parameter
    noncentrality = float()

    #  degrees of freedom
    df = float()

    # 
    # 		 * Constructor
    # 		 * @param lambda weight value
    # 		 * @param df degrees of freedom
    # 		 * @param noncentrality non-centrality parameter
    # 		 
    def __init__(self, lambda_, df, noncentrality):
        """ generated source for method __init__ """
        self.lambda_ = lambda_
        self.noncentrality = noncentrality
        self.df = df

    # 
    # 		 * Get the weight for this chi-square term
    # 		 * @return weight
    # 		 
    def getLambda(self):
        """ generated source for method getLambda """
        return self.lambda_

    # 
    # 		 * Get the non-centrality parameter for this chi-square term
    # 		 * @return non-centrality parameter
    # 		 
    def getNoncentrality(self):
        """ generated source for method getNoncentrality """
        return self.noncentrality

    # 
    # 		 * Get the degrees of freedom for this chi-square term
    # 		 * @return degrees of freedom
    # 		 
    def getDegreesOfFreedom(self):
        """ generated source for method getDegreesOfFreedom """
        return self.df

