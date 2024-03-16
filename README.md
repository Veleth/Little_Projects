# My little projects
This is a repository of my small programs, that may be kind of useful to someone, but don't deserve their own repository due to the amount of code and their size.
I may or may not expand the list in the future.
## Index
1. [Webchecker](#WEBCHECKER)
2. [BP reading converter](#BPCONVERTER)
3. [Election Tracker](#ELECTION)

<a name="WEBCHECKER"><h3>Webchecker (2019-01-17)</h3></a>
This program reads the list of URLs (by default from websites.txt) and constantly checks whether there has been an update to any of them. Upon update it notifies the user.
Libraries used: `bs4`, `smtplib`, and `requests`. It also requires `lxml` to be present in order to parse the data.

<a name="BPCONVERTER"><h3>Blood Pressure Reading Converter (2021-04-12)</h3></a>
This Jupyter script reads a CSV export from Apple Health data and converts the records to a more doctor-friendly format. Instead of an array of readings, you get an array of dates with a morning/evening column split.
Sample data included to better showcase what kind of data I was dealing with and what the intended result was.

<a name="ELECTION"><h3>2023 Parliamentary Election Tracker (2023-10-16)</h3></a>
This was a 1-day quick project that aimed to collect real-time polling data for the <a href="https://en.wikipedia.org/wiki/2023_Polish_parliamentary_election">2023 Polish parliamentary election</a>. The script fetched the data from the official <a href="https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/pl">Electoral Commission website</a> as the votes were being counted and results published. The goal was to estimate the Parliament seat distribution with increasing accuracy as the data kept flowing in.