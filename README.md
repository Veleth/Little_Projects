# My little projects
This is a repository of my small programs, that may be kind of useful to someone, but don't deserve their own repository due to the amount of code and their size.
I may or may not expand the list in the future.
## Index
1. [Webchecker](#WEBCHECKER)
2. [BP reading converter](#BPCONVERTER)
3. [Election Tracker](#ELECTION)
4. [EKW Checker](#EKWCHECKER)

<a name="WEBCHECKER"><h3>Webchecker (2019-01-17)</h3></a>
This program reads the list of URLs (by default from websites.txt) and constantly checks whether there has been an update to any of them. Upon update it notifies the user.
Libraries used: `bs4`, `smtplib`, and `requests`. It also requires `lxml` to be present in order to parse the data.

<a name="BPCONVERTER"><h3>Blood Pressure Reading Converter (2021-04-12)</h3></a>
This Jupyter script reads a CSV export from Apple Health data and converts the records to a more doctor-friendly format. Instead of an array of readings, you get an array of dates with a morning/evening column split.
Sample data included to better showcase what kind of data I was dealing with and what the intended result was.

<a name="ELECTION"><h3>2023 Parliamentary Election Tracker (2023-10-16)</h3></a>
This was a 1-day quick project that aimed to collect real-time polling data for the <a href="https://en.wikipedia.org/wiki/2023_Polish_parliamentary_election">2023 Polish parliamentary election</a>. The script fetched the data from the official <a href="https://wybory.gov.pl/sejmsenat2023/pl/sejm/wynik/pl">Electoral Commission website</a> as the votes were being counted and results published. The goal was to estimate the Parliament seat distribution with increasing accuracy as the data kept flowing in.

<a name="EKWCHECKER"><h3>EKW Checker</h3></a>
KW (Księgi Wieczyste), also called Land Registers, are official public records concerning the ownership and other parameters of real estate properties. I assume this part does not need to be explained further.
EKW is an online system that allows people to browse these records, but it doesn't provide a REST API to access them. There are some 3rd party APIs, but they cost way too much for any non-professional needs.
As it happened, I became interested in one of these registries, and got very impatient waiting for one of the records to be entered - this usually takes the Land Registry Court (eyeballing the name here, not sure what the official name in English is) months, and I am a very impatient man. After months of randomly checking the EKW website, I decided that it is better to spend several hours programming rather than several minutes checking the registry every week or so.
This project is loosely based on my trusty old [Webchecker](#WEBCHECKER), but is written a little bit better IMO, and relies on Pushover for notifications rather than SMTP.
Side note - figuring out the notifications took like 80% of the development time. I mostly spent that time reading and being frustrated with Gmail, IFTTT, Sendmail, and others.
