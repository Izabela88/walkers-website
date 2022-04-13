[![Build Status](https://app.travis-ci.com/Izabela88/walkers-website.svg?branch=main)](https://app.travis-ci.com/Izabela88/walkers-website)


# **WALKERS WEBSITE**

## **INTRODUCTION** 

![mockup](/documents/responsive.png)

Walkers -  a platform and website for people who are both looking for dog carers and for people providing such services in the whole UK.

Using the principles of UX design, this fully responsive and interactive website was developed using HTML, CSS, JavaScript and Python as well as Django as a framework.

View live project here [link to deployed link](https://walkers88.herokuapp.com/)


## **CHECK SEARCH FORM FUNCTIONALITY** 

The platform is to operate in the UK, and addresses from the Wolverhampton area were entered into the database.

To check the search form functionality please:

  - visit this page [Random Addresses Generator](https://www.doogal.co.uk/RandomAddresses.php)
  - to 'Number of addresses required' input enter '1'
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
    - [Databases platform and cloud storage](#databases-platform-and-cloud-storage)
    - [Libraries and frameworks](#libraries-and-frameworks)
    - [Other technologies](#other-technologies)  
  - [Testing](#testing)
    - [Introduction](#introduction)
    - [Code validation](#code-validation)
    - [Testing User stories](#testing-user-stories)
    - [Automated testing](#automated-testing)
    - [Testing accessibility and performance](#testing-accessibility-and-performance)
    - [Interesting issues and known bugs](#interesting-issues-and-known-bugs)
  - [Deployment](#deployment)
    - [Deployment of the page](#deployment-of-the-page)
    - [How to run the code locally](#how-to-run-the-code-locally)
   - [Credits](#credits)
     - [Code](#code)
     - [Media and content](#media-and-content)



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

      - All projects was created in Adobe XD:

      - [Home page, search section, join us section](/documents/home-page-project.png)
      - [Login, register page](/documents/login-register-project.png)
      - [Pet sitter profile](/documents/petsitter-profile-project.png)
      - [Search results](/documents/search-results-project.png)


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
    - [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/): Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

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
    - [Travis CI](https://www.travis-ci.com/): to sync with my GitHub for testing code before pulls and merge
    - [Doogal](https://www.doogal.co.uk/RandomAddresses.php): random addresses generator   
    - [Visual Studio Code](https://code.visualstudio.com/): was used to create and store code
    - [GitHub](https://github.com/): used to store the code of the project
    - [Adobe XD](https://www.adobe.com/products/xd/pricing/free-trial.html): for website projects
    - [Compress](https://compressgif.com/): for compress images
    - [Realfavicongenerator](https://realfavicongenerator.net/): for favicon


## **TESTING**

  - ### **Introduction**

    - The website was tested as it was developed with the implementation of new features, using:

      - console.log() and google developer tools
      - breakpoint() function and terminal for backend functionalities by printing expected outcome
      - manual testing
      - automated testing
      - Travis CI for testing code before pull and merge on GitHub:

        ![travis](/documents/travis-ci-merge-check.png)
        ![travis](/documents/travis-ci-merge-complete.png)
      

  - ### **Testing User Stories**
  
    - Testing User Stories can be found in [this document](/documents/features/test_user_stories.md).


  - ### **Automated testing**

    - The developer implemented automated testing all apps.
    - For measuring code coverage developer used Coverage.py tool.

    Coverage.py report can be found in [this document]()
    

- ### **Code validation**

    - #### **W3C HTML Code Validator**
      Each page for the website was run through the [W3C Markup Validation Service](https://validator.w3.org/) and returned no errors. 
      As all web pages are rendered dynamically using Django template, each page and scenario had to be validated by direct input by copying and pasting the source code for the page.

    - #### **W3C CSS Jigsaw Validator**
      Each CSS file was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors

    - #### **JSHint validator**
      All JavaScripts files were tested with [JSHint](https://jshint.com/) and returned no errors.


    - #### **Python 8**
      Each python file was run through [PEP8 online](http://pep8online.com/) and returned no errors.


  - ### **Responsiveness and compatibility**

    The Website was tested on Google Chrome, Mozilla Firefox, Opera and Safari browsers.
    The Safari browser doesn't support 'smooth' behavior parameter in window.scroll() method.
    The website was viewed on a variety of devices such as Desktop, Laptop (Macbook Pro 16 inch), Mobiles( Huawei P20 Mate, Huawei P30, Samsung S21 ultra).
    A large amount of testing was done to ensure that all pages were linking correctly.
    Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
    
  - ### **Testing accessibility and performance**

    I confirmed that the colors and fonts chosen are easy to read and accessible by running it through Lighthouse in Chrome extension.

      - Accessibility for desktop
      - Accessibility for mobiles


## **DEPLOYMENT**

 
  - ### **How to run the code locally**

    - ### **Forking the GitHub Repository**

    By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

    1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Izabela88/walkers-website)
    2. At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
    3. You should now have a copy of the original repository in your GitHub account.

    - ### **Making a Local Clone**

    1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Izabela88/walkers-website)
    2. Under the repository name, click "Clone or download".
    3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
    4. Open Git Bash
    5. Change the current working directory to the location where you want the cloned directory to be made.
    6. Type `git clone`, and then paste the URL you copied in Step 3.

    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    ```

    7. Press Enter. Your local clone will be created.

    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    > Cloning into `CI-Clone`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

    Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.


## **CREDITS**

  - ### **Code**

    - While coding for some problems and inspirations with JavaScript code, I looked for answers on websites:

    - [W3School](https://www.w3schools.com/)
    - [Stack Overflow](https://stackoverflow.com/)
    - [JavaScript Tutorial](https://www.javascripttutorial.net/)
    - [MDN Web Docs](https://developer.mozilla.org/en-US/)

    
  - ### **Media and content**

    - All content was written by the developer.
    - [Unsplash](https://unsplash.com/): for images
    - [Lottiefiles](https://lottiefiles.com/): for used animations
    - [Pixlr](https://pixlr.com/pl/): was used to process used photos
    - [CSS Scan](https://getcssscan.com/css-box-shadow-examples): for box shadow example
    - [Free Frontend](https://freefrontend.com/): for CSS and JavaScript inspirations


