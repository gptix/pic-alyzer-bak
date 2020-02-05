# pic-alyzer
Simple app to deploy on Heroku to test two endpoints.

## Team git repo
[Chris Huskey's](https://github.com/chrishuskey/DS10_picmetric2/)

[https://github.com/Build-week-picmetric2](https://github.com/Build-week-picmetric2)


## Team Tools
[Trello](https://trello.com/b/nBlbUZ5M/pic-metric-2)

[Notion](https://www.notion.so/6e719d512134435f8a89ca2862f8d3e7?v=6c8d3bd7bbcb44539f8659fc96caa906)

[Product Vision](https://docs.google.com/document/d/1ojPvd1FSEH8yWSFAFJezzLcXCEf7V1Lw4M7XT1sywzI/edit)

[Airtable](https://airtable.com/shrSnyzmYWdDO7c0G/tbl3bjvcax7pelQ2F/viwmaXfKAPEQyB01S/recWrKyK6b9FArml9?blocks=hide)

[Team (DS) Repo](https://github.com/picmetric/data-science)

## Other Tools

[Test PEP8 onlne](http://pep8online.com/)

[Receiving Images in Flask](http://www.patricksoftwareblog.com/receiving-files-with-a-flask-rest-api/)

[Test POST requests](https://docs.postman-echo.com/?version=latest)

[Markdown Live Preview](https://markdownlivepreview.com/)

[Flask Heroku Hello World](https://hidenobu-tokuda.com/how-to-build-a-hello-world-web-application-using-flask-and-deploy-it-to-heroku/)

[Discusion of YOLO3 and output](https://www.aiproblog.com/index.php/2019/05/26/how-to-perform-object-detection-with-yolov3-in-keras/)



## Rubrics
[Overall](https://www.notion.so/Build-Week-Project-Rubrics-c0783f6d9b7e435f9ce47e8cd2d0ee3b)

[DS Unit 3](https://www.notion.so/Data-Science-Unit-3-3289d37e99924262bca2a1f7d0292f51)

### Software Engineering and Reproducible Research

- [ ] Student contributed idiomatic and stylistically correct code to the project. 

[Code here](https://github.com/gptix/pic-alyzer/)

Idiomatic: tested with PEP8

- [ ] Problem they had to accomplish on their own: 

To proceed with testing of API vs. Michelangelo's layer, I created a Heroku instance, and successfully tested with Michelangelo.

Show code (above)

Break down their participation in the project.

- Created and tested (on Heroku) endpoints that interacted correctly with Michelangelo's work.

- Communicated with Chris, who developed similar code on AWS.

- Identified critical need for desctription of return value from classifier.

### SQL and Databases

- [ ] Student used and was able to implement and talk technically about their understanding over the database/data-pipeline used for the project. They also may have participated in helping design the schema.

I discussed with Michelangelo and team storage alternatives (Bucket, NoSQL, SQL) for different types of data.

- Images received from user - bucket
- User, transaction data - Postgres
- Results from classifier - Postgres, string field

I participated in designing model, by proposing storage of pre-processed image, by discussing which data is needed by the endpoint layer, and other points.

### Productization and Cloud

- [ ] Student participated in and contributed to the routes/API relevant for Data Science functionality. 

I did this by implementing the required endpoints in a python script hosted on Heroku, Functionality was tested by Michelangelo.

- [ ] Ensure here that student can speak technically to the frameworks/languages/tools used to create the API and ensure that the data flowed smoothly across the project back-end.

- Framework - Flask was a natural choice because it is easy to use, and ue of it and Heroku are a known quantity. For testing, this accepts GET requests.  In production, only POST requests will be needed.

- Languages - I only used Python (and JSON).

- Tools - I used Heroku as infratructure. I attempted to get an AWS account, but could not get my card validated. I am pursuing this.

- Smooth flow of data - as of Tuesday afternoon, Michelangelo was happy with data flow between his servers and the endpoints. Connection to the model built by DS9 is incomplete, but identified as a requirement.

### Teamwork - MVP

- [ ] demonstrates that all MVP features were built

Two endpoints reqired (`/summary` and `/batch_img_summary`) are defined and worked as of Tuesday afternoon.

Features: 

- `/summary` recieves image URL in JSON via POST request, returns JSON containing classification.

- `/batch_img_summary` receives JSON with multiple copies of data as for `/summary`, and returns JSOn containing multiples of return for `'/summary`

### Teamwork - Communications

- [ ] Student successfully collaborated with colleagues, "translated" DS topics for non-DS peers, and handled any problems or friction appropriately.

I think so.  I cooperated successfully with Michelangelo and Chris, and got a commitment to a data format to be returned from the model from Marilyn and Todd. This allowed Michelangelo to continue with work on storage of result instances.

I had some friction with one team member. Not a show stopper (yet), but cooperation regarding updates to git repo could be smoother.


## Team Members

Team Lead: Nicholas Gallucci

My **Awesome** TL - Jordan Ireland (Leader of Sharks)

DS (Unit 3) Chris Huskey (Laser Shark)

Michelangelo Markus

DS (Unit 4) Marilyn Esko 

DS (Unit 4) Todd Gonzalez
