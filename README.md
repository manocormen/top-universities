# World Top Universities 2023

## Goal

Combine leading university rankings using Python and JupyterLab.

## Articles

* [900 Free Computer Science Courses from World’s Top Universities](https://www.classcentral.com/report/cs-online-courses/)
* [100+ Math Courses from the World’s Top Universities](https://www.classcentral.com/report/mathematics-statistics-free-online-courses/)

## Data Sources

### Computer Science 2023

* QS: [World University Ranking 2023 — Computer Science & IT](https://www.topuniversities.com/university-rankings/university-subject-rankings/2023/computer-science-information-systems)
* Times Higher Education: [World University Ranking 2023 — Computer Science](https://www.timeshighereducation.com/world-university-rankings/2023/subject-ranking/computer-science)
* Shanghai Ranking: [Academic Ranking of World Universities 2022 — Computer Science & Engineering](https://www.shanghairanking.com/rankings/gras/2022/RS0210)

## Usage

```
$ cd top-universities/scraper
$ scrapy crawl qs -O data_scraped/qs.jsonl -a subject=cs -a year=2023
$ scrapy crawl the -O data_scraped/the.jsonl -a subject=cs -a year=2023
$ scrapy crawl arwu -O data_scraped/arwu.jsonl -a subject=cs -a year=2023
```
