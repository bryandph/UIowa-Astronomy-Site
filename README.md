# UIowa-Astronomy-Site
An alternative design for the UIowa Astronomy site built as a Flask app. The development of this project was inspired by the want to design a replacement for the University of Iowa's Astronomy Department and the content was taken and based on one of the lab refrence sites of the dept (http://astro.physics.uiowa.edu/ITU/). This project was not comissioned or endorsed by The University of Iowa or any affiliated entity. The Trademarks and content within are used under Fair Use terms for self education.

## Project Goal
This project takes a website with content provided in Markdown and Latex and uses Bootstrap3 to create a static site. It's usecase is comparable with framworks like Jekyll where minimizing code exposure to the end user is of max importance.

## Current Build State
This project is currently under development. At its current build state the site is generated dynamically at the initialization of the app and part of the HTML is stored in memory. The site is still partially generated per request which makes it unsuitable for production given the overhead of each request.

### Future Development
* Generate as much static content as possible on initializtion and store to disk.
* Extend with WSGI to allow provisioning of Apache or Nginx webservers.
* Add a caching mechanism to further speed up request response time.
