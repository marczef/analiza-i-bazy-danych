# Laboratorium 6 - Exploratory Data Analysis

Original data wojewodztwo.csv is available in /OriginalData folder.

The whole script is in /CommandFiles/lab6.ipynb

Files present in directory “original_data”
wojewodztwo.csv files – each file represents data concerning vacuum cleaner purchases collected in 16
    different voivodeships in Poland. During the course only one of the files was used later. In this case
    file "0_DOLNOSLASKIE".csv“ was analysed further. Every file contains several columns listed below:
- “Dni od zakupu”- describes how many days passed before the customer gave a rating to
    purchased product.
- “Marka” – brand of vacuum cleaner.
- “Wiek kupującego” – gives information about customer’s age.
- “Płeć kupującego” – gives information about customer’s gender.
- “Ocena” – customer’s rating of purchased product.

Data after analysis is available in:
- "age.csv” – extracted Pandas data frame containing information about customers’ age. 
    Later used to generate plot “age.jpg” in “Documents” directory.
- "time_of_having.csv” – extracted Pandas data frame containing information about how
    many days after purchase the customer has rated the product. Later used to generate plot
    time_of_having.jpg” in “Documents” directory.
- “gender.csv” – extracted Pandas data frame containing information about gender of
    customers’. Later used to genserate plot “gender.jpg” in “Documents” directory.
- “brand.csv” – extracted Pandas data frame containing information about
    purchase rates of each brand . Later used to generate plot “brand.jpg” in
    “Documents” directory
- "rate.csv” – extracted Pandas data frame containing information about all product rates
    given by customers. Later used to generate plot review.jpg” in “Documents” directory.   