# CS50W Capstone

This project is called Reader's Cabin which is a site where people can search for books and make their reading lists. From a long time I wanted a site where I can search for books, create reading lists and keep track of the books I am currently reading and the books which I already read. This site does exactly that.

To build this project I used all the technologies and languages I learned in the course (HTML, CSS, Bootstrap, JavaScript and Python), together with Django. I used Google books API to get information about the books, in the backend.

## Layout-(layout.html)

For the whole website, I designed a navbar using Bootstrap with a navbar brand and title, some navigation buttons and an integrated search bar. I also made sure it was mobile responsive. Also, I included a cover image below it.

## Index page

In the index page, I wrote some content about the Reader's Cabin and buttons to register and login.

## Register/Login/Logout

In the navbar we can find register and login buttons, in which I used a standard authentication system that uses the Django authentication functionalities.

## Top books

Displays a ranking of the books most read by the users of the Reader's Cabin.

## Top readers

Displays a ranking of the top readers of the Reader's Cabin.

## Search functionality

The user can type a book title in the search bar to search for that book in the Google Library. Then all the results are fetched and their covers are shown.

## Book Details Page

The user can click on one of the results to open the book's details page that displays the title, author, rating, categories, cover image, etc and a button to add the book to the user's reading list.

## User Profile

When the user clicks on his/her username in the menu, the user profile page is displayed. In this page, the user can see all the books saved to read, currently reading and finished. The user can see which books are in the reading list and start reading it, by clicking on the "start" button, to keep track of the date he/she started. Then the book is moved from "saved" to "reading". From the reading menu, the user can finish a book  by clicking the "Finish" button. Then the book saves the date and moves to "finished", where the user can see all the books the user finished reading, with the starting and finished dates.

## Project requirements

I think this project is interesting because it satisfies a need that I had, which is to create reading lists and keep track of the books I am currently reading and the books which I already read.
Also, I think it is interesting because I used all the languages we used during the course, as well as the fact that this time I was not provided with any started code and had to do it from scratch.
I used git for source control, html, css, databases, an api, bootstrap, django, python and javascript. During the development of this project I did a lot of research to try to implement details, that I didn't know how to do before and I learned some things that went beyond the course.

## How to run

cd into the project directory

Run "python manage.py runserver" to run the project.

## File Structure

- reading is the app where all the required files are present
- reading/static contains all the CSS, JS, Images of the project.
- reading/template contains all the HTML files of the project.
- reading/views.py contains all the views.
- reading/urls.py contains all the URLS.
- reading/models.py contains all the models created for this project.
