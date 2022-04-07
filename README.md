[![Build Status](https://app.travis-ci.com/Izabela88/walkers-website.svg?branch=main)](https://app.travis-ci.com/Izabela88/walkers-website)


# **WALKERS WEBSITE**

## **INTRODUCTION** 

![mockup]()

Walkers -  a platform and website for people who are both looking for dog carers and for people providing such services in the whole UK.

Using the principles of UX design, this fully responsive and interactive website was developed using HTML, CSS, JavaScript and Python as well as Django as a framework.

View live project here [link to deployed link](https://walkers88.herokuapp.com/)


## **Search for pet sitter** 

The platform is to operate in the UK, and addresses from the Wolverhampton area were entered into the database.

To check the search form functionality please:

  - visit this page [doogal](https://www.doogal.co.uk/RandomAddresses.php)
  - From 'Generate addresses in this area' option please choose 'WV'
  - Click 'Create random addresses' button

You can use the generated post code for the search form as your own.


## **TABLE OF CONTENT** 

  - [UX Design](#ux-design)
    - [Strategy](#Strategy)
    - [User stories](#User-stories)
    - [Scope](#Scope)
    - [Structure](#Structure)
    - [Skeleton](#Skeleton)
    - [Design](#Design)
  - [Features](#features)
    - [Existing features](#existing-features)
    - [Features left to implement](#features-left-to-implement)
  - [CRUD operations and defensive design](#crud-operations-and-defensive-design)    
    - [CRUD operations](#crud-operations)
    - [Defensive design](#defensive-design)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Databases platform and cloud storage](#database-platform-and-cloud-storage)
    - [Libraries and frameworks](#libraries-and-frameworks)
    - [Other technologies](#other-technologies)  
  - [Testing](#testing)
    - [Introduction](#introduction)
    - [Code validation](#code-validation)
    - [Testing User stories](#testing-user-stories)
    - [Automated testing](#automated-testing)
    - [Responsiveness and compatibility](#responsiveness-and-compatibility)
    - [Testing performance](#testing-performance)
    - [Testing accessibility](#testing-accessibility)
    - [Interesting issues and known bugs](#interesting-issues-and-known-bugs)
  - [Deployment](#deployment)
    - [Deployment of the page](#deployment-of-the-page)
    - [How to run the code locally](#how-to-run-the-code-locally)
   - [Credits](#credits)
     - [Code](#code)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgment](#acknowledgments)



## **UX DESIGN**

 - ### **Strategy**  

   More and more people own dogs. Although dogs are wonderful and undoubtedly important members of our families,
   owners often struggle with the problem of what to do in case they have to leave, 
   and they cannot take the dog with them or they work a lot and the dog is struggling at home alone. 
   This was the inspiration for creating the Walkers app which will help with find the best solution.

   The website gather users who:
    - are looking for people who provide services in care of the dog
    - provides services for the care of dogs
   
   - #### **Site owner goal**
     - To provide an platform where users can easy find proven pet sitters/ dog walkers
     - To provide an platform that allows users to advertise their services to a large number of recipients
     - To create a viable product that can be further developed with additional features

   - #### **User goals** 
     - To access a user-friendly website across multiple devices 
     - To find and contact a professional dog carer
     - To find as many customers as possible

 - ### **User stories** 

    1. **Navigation and website experience:**

        - As a site user, I want a responsive website so that I can access it on different devices
        - As a site user, I want to easily navigate across the site so that I can find the information I need
        - As a site user, I want to be able to return quickly to the home page so I can navigate the website easily
        - As a site user, I want to know when I am unauthorized to see some content so I can return to the home page and register.
        - As a site user, I want to see messages after logging in, logging out, or register so I will know what is happening
        

    2. **As a new user:**

        - I want to easily understand the main purpose of the website.
        - I want to know how to join the walkers' community
        - I want to find a section describing the company to find out when it was founded and the rest of the pertinent information about this company.
        - I want to locate social media links to find opinions about the company and check how trusted and known they are.
        - I want to be able to find a dog walker or pet sitter in my area
        - I want to be able to log in with social media so I can access my account quickly
        - I want to be sure that my email is correct so I can verify it.

        
    3. **As a returning user:**

        - I want to log in and logout so that I can access my profile safely
        - I want to be able to delete my profile so my personal information is removed from the website
        - I want to be able to add my image to my profile so I can be more trustworthy for others users.
        - I want to register for an account so  I can view a profile of dog walkers or pet sitters.
        - I want to be able to see dog walker or pet sitter profile to check more information about this person
        - I want to be able to write comments about dog walkers or pet sitters so I can help others users with choosing the best one person
        - I want to be able to delete or edit my reviews so I can manage them on my profile.
        

    4. **As a frequent user:** 

        - I want to be able to create my profile so I can advertise my services as dog walker/pet sitter.
        - I want to have the ability to change my password so I can keep my account safe.
        - I want to edit my profile so that I can update my personal information.
        - I want to be able to contact the platform owner so I can report any problems or ask questions.
        - I want to verify forgotten password so I can confirm my request on the recovery link
        - I want to sign up for the Newsletter to email any major updates and/or changes to the website or organization.


 - ### **Scope**
  
     - #### **Feature trade-off**

        ![Attachments_feature trade off]()

        A pdf version of the feature trade-off can been see [here]()

        This website will be developed as a minimal viable product with room for future improvements and releases, incorporating additional features.

     - #### **Functional requirements**
        - To be able to register using email address and secure password
        - To be able to login and logout
        - To be able to add/view/edit/delete profile information as pet sitter seeker
        - To be able to add/view/edit/delete profile information as pet sitter 
        - To be able to reset password
        - To be able to change password
        - To be able to add/view/edit/delete an ad
        - To be able to add/view/edit/delete reviews
        - To be able to search pet sitter according to area and set of criteria
        - To be able to display search results
        - To be able to store and retrieve avatar image 
        - To be able to contact the site owner 
        - To handle errors: page 404 not found, page 500 Internal Server Error and page 403 access denied

	  - #### **Non functional requirements**
          - Display pet sitter profile and information about him/her in engaging way
          - Intuitive navigation and structure

     - #### **Content requirements**
          - Clear and concise information on how to use the website
          - Details for the pet sitter
          - Forms where user input is required
          - Engaging text and headings throughout to introduce main sections of the website
          - Icons for interactive and visual elements
          - Background images to provide visually appealing and engaging interface

     - #### **Constraints**
    
          - Technical skills: Developer is still learning Python and is new to Django Framework which may impact on the successful implementation of the planned features. 
          - Time: Implementing features using new technical skills will require time and careful planning.

 - ### **Structure**

     - #### **Organization of functionality and content**

        - Header: Logo and a collapsible menu with navigational links
        - Homepage: Question indicating the purpose of the page, button which directs to the search form
        - Join Us: Information on how to start advertising as a pet sitter
        - About: Information about the site owner
        - Contact: The form that allows users to send an inquiry to the owner of the website
        - Profile page: to display all the relevant information about a user  
        - Footer: Links to social media, newsletter and site links

     - #### **Interaction design**

        - Collapsible menu
        - Buttons, icons and links with hovering effect
        - Pop up modal forms

     - #### **Database structure**

        The diagram below illustrates the database structure used in this project, first managed using SQLite during the development process, then Postgres in production with Heroku.

        ![Attach db structure](documents/db%20structure.png)

        - **User**
          - The default User model is replaced by custom AbstractUser because:
            - During authentication, application using an email address to uniquely identify
            - The model has been extended with additional custom columns: 'is_petsitter', 'avatar', 'phone_number'
          - Information from the User Model is used to create the UserProfile upon signing up

        - **AddressDetails model**
          - Site users' detailed address information
          - Address using one-to-one relationship with the user model
          - This model is used to generate address form in user profile

        - **ServiceDetails model**
          - Stores all service details (dog size, amount for services) which pet sitter can offer
          - This model is used to generate pet sitter profile form in user profile

        - **ServiceTypes model**
          - Stores detailed information about services types which are :
            - walking in the neighborhood
            - boarding ate the pet sitter home
            - day care at the client home
          - Related one-to-many  with service details model 
        
        - **PetsitterDetails model**
          - Stores pet sitter description about him/herself
          - Used to generate 'about description' in the pet sitter profile
          - Related one-to-one with user model and one-to-many with service details model

        - **Review model**
          - Stores review details about the pet sitters such as stars rating, comments etc
          - Related to user model to verify wether the user is leaving a review for the pet sitter
          - Related to pet sitter profile to easily retrieved information to be displayed in reviews
          - Reviews cannot be displayed and visible until approved by the admin

- ### **Skeleton**
    
    - ### **Wireframes**


- ### **Surface / Design** 

     The website feature a simple, modern and engaging design, with bright colors to arouse positive emotions among users.

    - #### **Imagery**

      - Hero image is designed to catch the user's attention. It also has a modern, energetic aesthetic.
      - The photos in the all sections are very positive and are meant to inspire the trust of the users.

    - #### **Colour scheme**
 
       The website will use the following color palette:

       ![color palette](documents/color%20palette.png)       

     - #### **Typography**
        The website will use the following fonts from Google:
        - [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter?query=Architects+Daughter) for headings
        - [Hubballi](https://fonts.google.com/specimen/Hubballi?query=Hubballi) for the rest text

     - #### **Icons**
       Icons by font-awesome used throughout the website to allow users to quickly access functionalities.

     - #### **Styling**
        - Horizontal lines to structure and make the content of the website easy to read.
        - Rounded edge borders and buttons for a more user friendly and inviting interface.
        - Some light shadows to add further dimension and depth to the website.


## **FEATURES**

  - ### **Existing features**
  
    Implemented features can be found in [this document](documents/features/features.md).
 
  - ### **Features left to implement**
  	- Pagination on pet sitters when displaying all people
    - Checkout and payment system
    - Chat with pet sitters

## **CRUD operations and defensive design**

  - ### **CRUD operations**
    Operations | all users | auth. user | superuser |
    --- | --- | --- | --- 
    View homepage | Yes | Yes | Yes |
    View about page | Yes | Yes | Yes |
    View contact page | Yes | Yes | Yes |
    View newsletter page | Yes | Yes | Yes |
    Add/edit/delete profile | No | Yes | Yes |
    View pet sitter profile | No | Yes | Yes |
    View pet sitters (search results)| Yes | Yes | Yes |
    Add/edit/delete ad | No | Yes | Yes |
    Login | No | Yes | Yes |
    Register | Yes | No | No |
    View/edit/delete my reviews | No | Yes | Yes |
    View all reviews | No | Yes | Yes |
    Add/edit/delete a review | No | Yes | Yes |


  - ### **Defensive design**

    - #### **Delete operations**
      - Users first need to confirm that they are sure that they want to delete the profile, review, avatar

    - #### **Review status**
      - Reviews can be written only by the pet sitter seekers
      - If review is not approved by admin:
        - Review will not be displayed in pet sitter profile page
        - In 'my reviews' section in review box will display information: 
          - 'waiting for approval by admin'
        

    - #### **Is active ad**
      - When user is register as pet sitter he/she can complete his/her profile to display his/her ad
      - There is  an option to display ad 
      - If pet sitter will set option to 'ON' information will be displayed 
      - If pet sitter will set option to 'OFF' information won't be displayed but it won't be delete in case of future mind changing
      - If pet sitter will off all options the 'check price' button will be disabled in his/her profile

    - #### **Status information**
      - If any of the fields is left blank, informative texts appear in their place.
      - The short texts describe what is missing in a given place.


## **TECHNOLOGIES USED**

  - ### **Languages**
    - [HTML](https://html.spec.whatwg.org/multipage/)
    - [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - [Python](https://www.python.org/)

  - ### **Databases platform and cloud storage**
    - [SQlite](https://www.sqlite.org/index.html): SQL database engine provided by default as part of Django and used during development
    - [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql): SQL database service provided directly by Heroku for storing data
    - [Cloudinary](https://cloudinary.com/): to store images and static files in production
    - [Heroku](https://www.heroku.com/): to deploy and run the application in production

  - ### **Libraries and frameworks**
    - [Django](https://www.djangoproject.com/): Python web framework for rapid development and clean, pragmatic design
    - [Django Phonenumber Field](https://pypi.org/project/django-phonenumber-field/0.2a3/): uk phone numbers validation
    - [Pillow](https://pillow.readthedocs.io/en/stable/): This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
    - [Jquery](https://jquery.com/): to DOM manipulation and event handling
    - [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html): using for registration, and social account authentication.
    - [Django_case_insensitive_field](https://pypi.org/project/django-case-insensitive-field/): to allow case insensitive comparison for unique fields.
    - [Django cleanup](https://pypi.org/project/django-cleanup/): to automatically delete images / files when an ImagField is removed / updated or deleted
    - [Flake8](https://pypi.org/project/flake8-django/): A flake8 plugin to detect bad practices on Django projects

  - ### **Other technologies**
    - [Google font](https://fonts.google.com/): used for body and headings font
    - [Font Awesome](https://fontawesome.com/): used for icons throughout the website
    - [Postcodes Io](https://api.postcodes.io/): Postcodes & Geolocation API for the UK.
    - [Mailchimp](https://mailchimp.com/): Marketing platform used for newsletter.
    - [Dbdiagram.io](https://dbdiagram.io/home): to design schema of relational database
    - [W3C Markup Validation Service](https://validator.w3.org/): to check there's not error in HTML
    - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This tool was used to check there's no error in the CSS code.
    - [PEP8 online](http://pep8online.com/): to validate python syntax
    - [JSHint](https://jshint.com/): to validate jquery/javascript syntax
    - [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Google inspect was used to test and fix code and page responsiveness.
    - [Google lighthouse](https://developers.google.com/web/tools/lighthouse): Google lighthouse was used to assess performance of the site
    - [Lottiefiles](https://lottiefiles.com/): for used animations
    - [Travis CI](https://www.travis-ci.com/): to sync with my GitHub for testing my code
    - [Doogal](https://www.doogal.co.uk/RandomAddresses.php): random addresses generator
    - [Unsplash](https://unsplash.com/): for images
    - [Pixlr](https://pixlr.com/pl/):  was used to process used photos
    - [Visual Studio Code](https://code.visualstudio.com/): was used to create and store code
    - [GitHub](https://github.com/): used to store the code of the project



## **TESTING**

  - ### **Testing User Stories**
  
    Testing User Stories can be found in [this document](/documents/features/test_user_stories.md).