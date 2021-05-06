In order to make a more convenient data set out of these, I wrote a script that can clean any of the main files in this dataset.

There are a few minor issues that I ran into when importing the data set to a few different programs. The first is that the data begins with the most recent date as the first row, which if one wished to do something such as a regression model would make for an unintuitive model that goes backwards, so the data frames rows are inverted, starting with the first recorded date.

Due to the way the dates are structured, some programs may not read them as a date. To solve this, the code changes to a Y-M-D format in numerical data, and creates separate columns for the year, month and day in addition if someone may want them.

The format of the numerical columns which might be read as strings rather than numbers due to the commas.

Tthe Volume column which is the most significant change, as it is currently not written in a numeric format. The code simply allows for Volume to be numeric now.

The column names are edited to be shorter and all lower case for more convenient use in coding.

The program then exports these changes to a new CSV file.

Original data sets: https://www.kaggle.com/kaushiksuresh147/top-10-cryptocurrencies-historical-dataset
