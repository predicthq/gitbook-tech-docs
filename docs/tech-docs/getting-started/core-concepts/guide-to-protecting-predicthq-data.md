---
description: It's important to protect PredictHQ data from unauthorized access and usage.
---

# Guide to protecting PredictHQ data

This guide provides ideas on how to protect PredictHQ’s data from unauthorized usage due to what is known as web scraping or screen scraping, specifically when being used in public facing websites.

Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites, which automated tools or bots typically perform. Our terms require customers to protect against unauthorized use of our data including by these techniques so carefully consider how you're exposing PredictHQ data and what protections you have in-place to protect it.

## Technical deterrents and protection

You must use any reasonable endeavors to prevent unauthorized access to, or use of PredictHQ Data and, in the event of any such unauthorized access or use, promptly notify PredictHQ. Reasonable endeavors to prevent web scraping may include any of the following (**but are not limited to**):

### Require authentication to view data

Users must log in, or be approved before using the application. This may help detect legitimate users from automated scripts. It also allows more effective monitoring for (and the ability to take action against) any unwanted activity.

### Application design

Effective application design can make it difficult to scrape information or easier to detect scraping. This includes techniques such as limiting the amount of data returned per search, restricting the area of the search, or requiring pagination of results.

### IP address monitoring, limiting, or blocking

Ability to monitor, alert, and report on website activity by IP address allows for the detection of sudden increases in traffic, outliers, or bad actors. Tracking of an IP address allows for the ability to use a blocklist if needed.

### Use of commercial software to protect public-facing content from bots

Many companies offer fully featured solutions to prevent scraping by bots or automated scripts. The major cloud providers (AWS, Azure, and GCP) offer Web Application Firewall (WAF) solutions. In addition to this there are several stand alone solutions, for example Cloudflare or Fastly. These solutions all provide services that include regularly updated blocklists, automatic bot detection, and bot prevention.

### Traffic monitoring

Monitoring of website traffic through capture and analysis of access logs or similar allows for trend monitoring, the configuration of alerts, and early detection of suspicious activity such as increased traffic volumes.

### Use of captcha challenge-response tests, in particular reCaptcha

Captcha or reCaptcha solutions that attempt to identify legitimate human users can help prevent bot usage. Together with IP tracking, the use of a captcha can be triggered only after certain thresholds are met, or for repeated infringements.&#x20;

### Correct use of the Robots Exclusion Standards (robots.txt file)&#x20;

Websites can declare if crawling is allowed or not in the robots.txt file and allow partial access, limit the crawl rate, specify the optimal time to crawl, and more. This can be used to prevent web crawlers from scraping data

### Protect or disable any publicly available APIs

Ensure you implement proper security and access controls for any publicly accessible APIs that your website uses, so that only legitimate usage has access.
