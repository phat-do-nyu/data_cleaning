
### `ETHICS.md`

```markdown
# Ethical Considerations

## Overview

This project involves gathering data from an API and web scraping a publicly accessible website. Ethical considerations have been carefully evaluated to ensure responsible use of data and compliance with legal standards.

## Data Privacy and Respect for Terms of Service

- **Compliance with API Terms:** The data fetched from the SportMonks API is gathered under the conditions specified in their terms of service. All data collection complies with the usage limitations and privacy policies set by the API provider.
- **Respecting Website Policies:** Transfermarkt is used as a scraping target to gather market values of players. We have ensured that scraping is performed responsibly:
  - **Rate Limiting and Politeness:** The scraper includes random delays between requests to mimic human browsing behavior and reduce the risk of server overload.
  - **User-Agent Spoofing:** Requests are sent with proper headers to identify the requests as coming from a browser, further ensuring that server rules are respected.

## Intellectual Property and Data Use

- **Data Usage Restrictions:** Market value data from Transfermarkt is proprietary, and this project respects that by not redistributing scraped data in any way that violates their terms. This dataset is intended for personal or educational use only and not for commercial distribution.
- **Attribution:** Proper attribution is given to both data sources (SportMonks and Transfermarkt) to acknowledge the ownership of the data.

## Mitigation of Harm

- **Data Integrity:** We ensure that the data is presented accurately without alteration or misrepresentation of player values or statistics. 
- **Transparency:** Users are informed of the data sources and any limitations that come with using this dataset. This ensures users are aware of potential biases or inaccuracies inherent in the data.

## Future Considerations

To further align with ethical standards, users of this dataset are encouraged to review and respect the data policies of both SportMonks and Transfermarkt. Any commercial use of this data should seek explicit permission from the data providers.

## Conclusion

This project prioritizes ethical considerations by adhering to legal standards, respecting data source policies, and promoting responsible data usage. We encourage all users to follow these practices to maintain the integrity and ethical use of this data.
