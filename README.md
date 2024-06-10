# Ferrari_Emvironmental_Indicator_Analysis
This repository assesses Ferrari’s sustainability using a custom EPI. It uses three GHG indices to reflect Ferrari’s carbon reduction efforts. Findings show significant steps in reducing emissions. The EPI Index aids in evaluating the company's environmental impact.


# Introduction

There are various ways to measure sustainability. A common method is
through multi-criteria assessment using indicators. Indicators are
useful because they can provide information over a period, organize and
group data (index), and assess data against a threshold or a baseline.
For sustainability assessment to be useful, socio-economic and
environmental indicators must target shareholder needs.

Data can be an effective and efficient enabler of ESG initiatives, but
only if information is conveyed clearly to decision makers and
stakeholders. To facilitate data-driven policy-making, we have decided
to develop an indicator on the base of the Environmental Performance
Index (EPI). The EPI transforms complex environmental datasets into
simple metrics that gauge sustainability progress. These metrics, or
indicators, give each country a score, with 0 denoting worst performance
and 100 denoting best performance.

The EPI is a tool created to evaluate a country's affords towards
sustainability. Similarly, our indicator aims to evaluate some of
Ferrari's initiatives and ESG goals. We have identified the efforts
toward which the company has concentrated high levels of resources:
mainly in reducing the carbon and greenhouse gas (GHG) footprint. For
this reason we have chosen to use three GHG indices in compiling the
indicator:

-   GHP: Greenhouse gas emissions per capita

-   CDA: Adjusted emissions growth rate for carbon dioxide

-   GHN: Projected GHG emissions in 2050

# Calculating Indicator Scores

The indicator follows the formula: $$EPI = (X - W) / (B - W) / 100$$
Where X is the company score, W is the weight, and B is the panel score.
We have used the weights provided in the original EPI index and only
adapted the distribution to allow for accuracy and readability.

The first index we selected is Greenhouse gas emissions per capita
(GHP), where capita refers to the number of vehicles produced in a given
period of time. To calculate the GHP we used the 2022 Ferrari group
average carbon footprint (*598000*) and divided it by the number of
Ferraris produced in the same period (*13221*). We have compared the
company score to the average carbon footprint of a manufacturing plant
in Italy. The data for CO2 emissions in the manufacturing sector of
Italy was gained through \"Climate Watch\" *29480000*. We divided the
the total CO2 emission by the number of manufacturing companies register
in Italy *548565*.

We calculated the adjusted emissions growth rate for carbon dioxide
(CDA) using the formula: $$\frac{N_1}{N_n}^\frac{1}{n}-1$$

The values for N here are *93243 & 78059*, the CO2 emission of Ferrari
during $N_1$ (2016) and $N_n$ 2022. For the panel data we used the
historic data of CO2 emissions of Italy in the last 30 years *4030000 &
29480000*. There is a notable difference within the time period chosen,
because through a longer data set we aim for the panel value to be more
taxing when evaluating the company's performance.

Projected GHG emissions in 2040(GHN) captures whether Ferrari is on
track to reach zero emissions by 2040. It is calculated using an
exponential fit function to project GHG emissions to the end of the
period. $$a * \exp{(-b * x)} + c$$ The function takes in *x* as the
independent variable, *a* which describes the coefficient of the
exponential term, *b* shows the rate of decay or growth, and *c* is the
coefficient of of the constant term. We fit the function to historical
data and then use it to predict future emissions. To normalize the score
value to match the format of the indicator we use the same formula as
the adjusted growth rate. The first input is the GHG emissions of
Ferrari in 2016. The last input is the predict emission 24 steps in the
future, from now (2024) until 2040. We adjust the rate over the entire
period to get the final score. Below you can see the results of the
linear regression.
![CO2_Predicted_2040](https://github.com/NikolaKirilov/Ferrari_Emvironmental_Indicator_Analysis/assets/96425721/cec327d9-9d92-41e3-9c1c-b85810efea3b)
 

# Conclusion

In conclusion, our sustainability assessment through the custom EPI
Index provides an understanding of Ferrari's environmental impact and
progress towards ESG goals. We successfully established a robust
framework to evaluate and compare Ferrari's performance against industry
standards and national averages.

Our analysis reveals that Ferrari is making significant strides in
reducing its carbon footprint and greenhouse gas emissions, aligning
with global sustainability efforts. The calculated indicators reflect
the company's dedication to resource optimization and environmental
responsibility.

This indicator highlights the importance of data-driven decision-making
in steering corporate strategies towards a greener future. As we
continue to refine our assessment tools and methodologies, we anticipate
that such indicators will become integral to monitoring and promoting
sustainable practices.
