# Uploading Your Demand Data to Beam

The dataset is a time series where each record consists of a date and its corresponding value. The supported file format is CSV, with column names specified in the first row and each column separated by a comma.

See also [Upload Demand Data](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam/analyses/upload-demand-data) in the Beam API documentation for more details on the upload format.

### Data Format and Specifications <a href="#data-format-and-specifications" id="data-format-and-specifications"></a>

* The CSV file must contain two columns – `date` and `demand`. The column headings must be in the first row of the file as `date,demand`
* The date format required is ISO date format in the `YYYY-MM-DD` format. That is year, month, and day. For example 2017-03-29 for 29 March 2017. The file should contain one row per date.
* Data can be daily or weekly. Daily data should have consecutive dates, while weekly data should have one entry per week.
* Demand can be any integer or decimal value. In general, we recommend using the same value that is used in your demand forecasting.
* For **daily** demand, the minimum amount of data required is **6 months**, or 180 data points. Beam can impute up to 20% of missing values, provided that the minimum data requirements are satisfied and there are no more than 7 consecutive days missing.
* For **weekly** demand, the minimum amount of data required is **2 years**, or 104 data points. Beam can impute up to 10% of missing values, provided that the minimum data requirements are satisfied and there are no more than 5 consecutive weeks missing. All weekly data points must align with the **start of the week** and occur on the same weekday.
* Data should start no earlier than 1 January 2017 (2017-01-01) and end no later than one year into the future.

### File Format <a href="#file-format" id="file-format"></a>

Here are examples of the correct file format for Beam:

#### Daily Data <a href="#daily-data" id="daily-data"></a>

Below is an example of what the file should look like for daily demand data. The column headers must be `date` and `demand` only and the date format `YYYY-MM-DD` to avoid receiving errors.

| date       | demand |
| ---------- | ------ |
| 2018-01-01 | 3278   |
| 2018-01-08 | 4494   |
| 2018-01-15 | 3712   |
| 2018-01-22 | 3900   |
| 2018-01-29 | 5067   |
| 2018-02-05 | 4692   |
| 2018-02-12 | 5161   |

* [Daily example demand file for Beam](https://www.predicthq.com/files/beam-example-demand-file.csv)

#### Weekly Data <a href="#weekly-data" id="weekly-data"></a>

Weekly demand data looks the same but each row is a week apart. See below:

| date       | demand |
| ---------- | ------ |
| 2018-01-01 | 3278   |
| 2018-01-08 | 4494   |
| 2018-01-15 | 3712   |
| 2018-01-22 | 3900   |
| 2018-01-29 | 5067   |
| 2018-02-05 | 4692   |
| 2018-02-12 | 5161   |

* [Weekly example demand file for Beam](https://www.predicthq.com/files/example-beam-weekly-demand-data.csv)

#### Additional Notes <a href="#additional-notes" id="additional-notes"></a>

Each date in the uploaded file should correspond to exactly one row to ensure data integrity. If multiple entries for the same date are found, the upload automatically retains the latest entry and ignores earlier values.

If you have any problems please [talk to us](https://www.predicthq.com/contact/sales) and we can help.

### What type of data should I include? <a href="#what-type-of-data-should-i-include" id="what-type-of-data-should-i-include"></a>

We recommend selecting a unit of measure that reflects your specific business activities, such as the unit used in your demand forecasting. This ensures that the data is directly relevant to your analytical needs. For example:

* **Hotels:** The total number of rooms booked per day.
* **Restaurants**: The number of staff rostered per day if you’re forecasting labor needs.
* **Consumer Packaged Goods (CPG) Companies**: Daily inventory numbers.
* **Parking Facilities**: The number of bookings for each parking location per day.

You may upload any unit that best represents your demand. Whether it's sales per day, the number of trips for a rideshare service, or any other metric, ensure it aligns with what you aim to analyze using Beam.

### Granularity and missing data <a href="#granularity-and-missing-data" id="granularity-and-missing-data"></a>

It is important that the data is aggregated on a daily level for daily demand or a weekly level for weekly demand. For example, a business might record a demand of 1000 on March 29, 2017, and 800 on the following day.

The `demand` column should represent a non-negative quantity, with values greater than or equal to 0. Every date in the dataset should correspond to a non-blank, non-null demand value, and every demand entry must have an associated date. While it may be tempting to fill in missing values with zero, this should only be done if zero accurately represents 'no demand' for that period.

If missing data occurs because the system was down or no record was available for a particular day, we suggest leaving that row out of the dataset to maintain accuracy in the results.

### Bulk uploading Beam analyses <a href="#bulk-uploading-beam-analyses" id="bulk-uploading-beam-analyses"></a>

If you want to upload a large amount of Beam analyses we recommend using the [Beam API](https://app.gitbook.com/s/kEFs8urDbSJqBmXUI3Lv/beam).
