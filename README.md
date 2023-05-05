# World Top Universities 2023

## Goal

Combine leading university rankings using Python and JupyterLab.

## Data Sources

### Computer Science 2023

* QS: [World University Ranking 2023 — Computer Science & IT](https://www.topuniversities.com/university-rankings/university-subject-rankings/2023/computer-science-information-systems)
* Times Higher Education: [World University Ranking 2023 — Computer Science](https://www.timeshighereducation.com/world-university-rankings/2023/subject-ranking/computer-science)
* Shanghai Ranking: [Academic Ranking of World Universities 2022 — Computer Science & Engineering](https://www.shanghairanking.com/rankings/gras/2022/RS0210)

### Mathematics 2023

* QS: [World University Ranking 2023 — Mathematics](https://www.topuniversities.com/university-rankings/university-subject-rankings/2023/mathematics)
* Times Higher Education: [World University Ranking 2023 — Physical Sciences](https://www.timeshighereducation.com/world-university-rankings/2023/subject-ranking/physical-sciences)
* Shanghai Ranking: [Academic Ranking of World Universities 2022 — Mathematics](https://www.shanghairanking.com/rankings/gras/2022/RS0101)

## Usage

1. Add the ranking links in `./scraper/scraper/settings.py`.
2. Run the commands below, with the appropriate filenames and arguments.

```
$ cd top-universities/scraper
$ scrapy crawl qs -O data_scraped/qs_cs_2023.jsonl -a subject=cs -a year=2023
$ scrapy crawl the -O data_scraped/the_cs_2023.jsonl -a subject=cs -a year=2023
$ scrapy crawl arwu -O data_scraped/arwu_cs_2023.jsonl -a subject=cs -a year=2023
```

3. Open the Jupyter Notebook, edit the settings and run it.
4. Update `normalize.py` as needed to fix the university names.

## Articles

* [900 Free Computer Science Courses from World’s Top Universities](https://www.classcentral.com/report/cs-online-courses/)
* [150 Math Courses from the World’s Top Universities](https://www.classcentral.com/report/mathematics-statistics-free-online-courses/)