# Key Considerations
Producing a clean, hourly-aligned UK–France day-ahead electricity price dataset was a critical and non-trivial stage of this case study. The majority of complexity lay in sourcing, aligning, and validating data from different systems before modelling could begin.

1. Multiple Data Sources
• France: Retrieved via the ENTSO-E Transparency Platform API, which returns XML in monthly chunks and requires careful parsing.
• UK: Sourced from a separate file (simulated for this study due to limited free UK market data post-Brexit), in a different format and unit of measure.
• Required harmonisation of currency, units, and timestamps.

2. Data Availability Gaps
• UK day-ahead prices are not directly accessible on ENTSO-E for the relevant period, requiring an alternative data source (simulated dataset for uk day ahead prices)
• Simulated UK data still needed exact hourly alignment with the France dataset.

3. ENTSO-E API 
• Month-by-month calls: API limits meant looping over months between start and end dates.
• Exclusive end times: periodEnd is exclusive — failing to add the correct buffer can omit the last day’s data.
• Daylight savings time (DST): Spring DST change reduces some days to 23 hours, breaking naïve 24×day assumptions.
• Timestamp parsing: Correct timestamps require reading the <timeInterval> start from XML, not assuming sequential hours from a fixed start date.

4. Merging Complexities
• Both datasets required:
• Hourly resolution with no missing hours in the overlap period.
• Consistent timezone handling and flooring to the hour.
• Currency alignment (GBP to EUR where applicable).
• Even small mismatches in datetime formats or rounding could result in large row losses after merging.

Outcome:
A validated, currency-consistent, hourly UK–France dataset covering Jan–Jul 2025, ready for spread construction, exploratory data analysis, and option pricing models.