---
description: It's important to protect PredictHQ data from unauthorized access and usage.
---

# Guide to Protecting PredictHQ Data

This guide provides ideas on how to protect PredictHQ’s data from unauthorized usage due to what is known as web scraping or screen scraping, specifically when being used in public facing websites.

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites, typically performed by automated tools or bots. Our terms require customers to protect against unauthorized use of our data including by these techniques so please carefully consider how you're exposing PredictHQ data and what protections you have in-place to protect it.

## Technical Deterrents and Protection

Customers must use any reasonable endeavors to prevent unauthorized access to, or use of PredictHQ Data and, in the event of any such unauthorized access or use, promptly notify PredictHQ. Reasonable endeavors to prevent web scraping may include any of the following (**but are not limited to**):

### Require Authentication to View Data

Users must login, or be approved before using the application. This may help detect legitimate users from automated scripts. It also allows more effective monitoring for (and the ability to take action against) any unwanted activity.

### Application Design

Effective application design can make it difficult to scrape information or easier to detect scraping. This includes techniques such as limiting the amount of data returned per search, restricting the area of the search, or requiring pagination of results.

### IP Address Monitoring, Limiting or Blocking

Ability to monitor, alert and report on website activity by IP address allows for the detection of sudden increases in traffic, outliers or bad actors. Tracking of an IP address allows for the ability to use a blocklist if needed.

### Use of Commercial Software to Protect Public-Facing Content from Bots

Many companies offer fully featured solutions to prevent scraping by bots or automated scripts. Web Application Firewalls (WAF) solutions are offered by the major cloud providers (AWS, Azure and GCP). In addition to this there are several stand alone solutions, for example Cloudflare or Fastly. These solutions all provide services that include regularly updated blocklists, automatic bot detection and bot prevention.

### Traffic Monitoring

Monitoring of website traffic through capture and analysis of access logs or similar allows for trend monitoring, the configuration of alerts and early detection of suspicious activity such as increased traffic volumes.

### Use of Captcha Challenge-Response Tests, in Particular reCaptcha

Captcha or reCaptcha solutions that attempt to identify legitimate human users can help prevent bot usage. Together with IP tracking, the use of a captcha can be triggered only after certain thresholds are met, or for repeated infringements.&#x20;

### Correct use of the Robots Exclusion Standards (robots.txt file)&#x20;

Websites can declare if crawling is allowed or not in the robots.txt file and allow partial access, limit the crawl rate, specify the optimal time to crawl and more. This can be used to prevent web crawlers from scraping data

### Protecting or Disabling any Publicly Available APIs

Ensuring proper security or access controls are implemented for any publicly accessible APIs that your website uses to ensure access is restricted for legitimate usages.
