# Developer technology trends

## Source coverage

The IBM course survey contains 65,457 rows and 114 columns. Removing 20 exact duplicate rows leaves 65,437 unique respondent IDs. Country is reported for 58,930 respondents across 185 countries. The job exercise contains 27,005 modified records. The salary exercise contains 10 languages and has no stated survey date or sample size.

## Observed technology preferences

JavaScript has the most current-use mentions: 37,492 respondents (57.3% of all respondents). Python leads future interest: 25,047 respondents (38.3%).

PostgreSQL leads current database use, and PostgreSQL leads desired database use. Complete rankings and percentage-point comparisons are in the derived CSV files. Current use and future interest are answers to different questions in one survey year.

## Compensation and demographics

Positive annual compensation is available for 23,435 respondents. Its median is $65,000 in the supplied converted USD field. 42,002 compensation values are missing. The histogram excludes 978 positive compensation responses outside the IQR display range, while the headline median uses every positive response. Age is categorical and does not support an exact mean age.

## Interpretation

The survey describes people who chose to respond. It does not establish representative global employment demand or a forecast of technology adoption. Future interest can identify topics worth comparing with current use, but country, experience and response coverage should be considered before applying these findings to a particular team.

The course API uses case-sensitive substrings, which can combine distinct technologies such as Java and JavaScript. The job-count CSV preserves those results and adds a case-insensitive comparison with term boundaries. These are counts within a modified teaching dataset. They are not current US city job totals.

The salary exercise has insufficient methodology for comparing career earnings. It is presented only as the result of extracting the supplied HTML table.

## Reproduction

Run `python src/download_data.py`, then `python src/analysis.py` from the repository. The notebook contains the same analysis. Raw respondent data is excluded from this repository. Source links and licensing are in README.md. This analysis was developed with AI assistance.
