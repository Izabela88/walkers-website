[![Build Status](https://app.travis-ci.com/Izabela88/walkers-website.svg?branch=main)](https://app.travis-ci.com/Izabela88/walkers-website)

# **WALKERS WEBSITE**

## **INTRODUCTION**

![mockup](/documents/responsive.png)

Walkers - a platform for people who are both: looking for dog carers and for people providing such services in the whole Great Britain.

Using the principles of UX design, this fully responsive and interactive website was developed using HTML, CSS, JavaScript and Python as well as Django as a framework.

View live project here [link to deployed link](https://walkers88.herokuapp.com/)

## **CHECKING THE SEARCH FORM FUNCTIONALITY**

The platform is to operate in the UK, and only UK addresses may be entered in all address forms.
The database contains addresses from the Wolverhampton area only. Wolverhampton belong to West Midlands county.

To check the search form functionality please:

- Visit this page [Random Addresses Generator](https://www.doogal.co.uk/RandomAddresses.php).
- In the "Number of Addresses Required" field, enter the number of random addresses you want to print.
- Check the "Include a randomly generated phone number" option if you also want to generate a randomly generated phone number.
- From 'Generate addresses in this area' option please choose 'WV'.
- Click 'Create random addresses' button.

You can use the generated post code for the search form as your own.

The created address can also be used to fill in the address form on the user profile page.

## **WALKER PROFILE SERVICE TYPES**

In case of trying run code locally for the first time it is necessary to enter the data from image below manually into the database in the section: "walker_profile_servicetypes".
The first two columns must be exact the same as in the photo and the date may be present.

![service types](/documents/db-data.png)

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
- [Data validation](#data-validation)
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
  - [Deployment on heroku](#deployment-on-heroku)
  - [How to run the code locally](#how-to-run-the-code-locally)
- [Credits](#credits)
  - [Code](#code)
  - [Media and content](#media-and-content)

## **UX DESIGN**

- ### **Strategy**

  More and more people own dogs. Although dogs are wonderful and undoubtedly important members of our families,
  owners often struggle with the problem of what to do in case they have to leave,
  and they cannot take the dog with them or they work a lot and the dog is struggling at home alone.
  This was the inspiration for creating the Walkers platform which will help with find the best solution for all dogs owners.

  The website gathers users who:

  - are looking for people who provide services in the care of the dogs.
  - provides dog care services and who wants to advertise their own services.

  - #### **Site owner goal**

    - To provide an platform where users can easy find proven pet sitters/ dog walkers.
    - To provide an platform that allows users to advertise their services to a large number of recipients.
    - To create a viable product that can be further developed with additional features.

  - #### **User goals**
    - To access a user-friendly website across multiple devices.
    - To find and contact a professional dog carer.
    - To find as many customers as possible.

- ### **User stories**

  1. **Navigation and website experience:**

     - As a site user, I want a responsive website so that I can access it on different devices.
     - As a site user, I want to easily navigate across the site so that I can find the information I need.
     - As a site user, I want to be able to return quickly to the home page so I can navigate the website easily.
     - As a site user, I want to know when I am unauthorized to see some content so I can return to the home page and register.
     - As a site user, I want to see messages after logging in, logging out, or register so I will know what is happening.

  2. **As a new user:**

     - I want to easily understand the main purpose of the website.
     - I want to know how to join the walkers' community.
     - I want to find a section describing the company to find out when it was founded and the rest of the pertinent information about this company.
     - I want to locate social media links to find opinions about the company and check how trusted and known they are.
     - I want to be able to find a dog walker or pet sitter in my area.
     - I want to be able to log in with social media so I can access my account quickly.
     - I want to be sure that my email is correct so I can verify it.

  3. **As a returning user:**

     - I want to log in and logout so that I can access my profile safely.
     - I want to be able to delete my profile so my personal information is removed from the website.
     - I want to be able to add my image to my profile so I can be more trustworthy for others users.
     - I want to register for an account so I can view a profile of dog walkers or pet sitters.
     - I want to be able to see dog walker or pet sitter profile to check more information about this person.
     - I want to be able to write comments about dog walkers or pet sitters so I can help others users with choosing the best one person.
     - I want to be able to delete or edit my reviews so I can manage them on my profile.

  4. **As a frequent user:**

     - I want to be able to create my profile so I can advertise my services as dog walker/pet sitter.
     - I want to have the ability to change my password so I can keep my account safe.
     - I want to edit my profile so that I can update my personal information.
     - I want to be able to contact the platform owner so I can report any problems or ask questions.
     - I want to verify forgotten password so I can confirm my request on the recovery link.
     - I want to sign up for the Newsletter to email any major updates and/or changes to the website or organization.

- ### **Scope**

  - #### **Functional requirements**

    - To be able to register using email address and secure password.
    - To be able to login and logout.
    - To be able to add/view/edit/delete profile information as pet sitter seeker.
    - To be able to add/view/edit/delete profile information as pet sitter.
    - To be able to reset password.
    - To be able to subscribe to the newsletter.
    - To be able to change password.
    - To be able to add/view/edit/delete an ad.
    - To be able to add/view/edit/delete reviews.
    - To be able to search pet sitter according to area and set of criteria.
    - To be able to display search results.
    - To be able to store and retrieve avatar image.
    - To be able to contact the site owner.
    - To handle errors: page 404 not found, page 500 Internal Server Error and page 403 access denied, 401 Unauthorized.

  - #### **Non functional requirements**

    - Display pet sitter profile and information in an interesting way.
    - Intuitive navigation and structure.

  - #### **Content requirements**

    - Clear and concise information on how to use the website.
    - Details for the pet sitter.
    - Forms where user input is required.
    - Engaging text and headings throughout to introduce main sections of the website.
    - Icons for interactive and visual elements.
    - Background images to provide visually appealing and engaging interface.

  - #### **Constraints**
    - Technical skills: The developer is still learning Python and is new to Django Framework, which may impact the successful implementation of the planned features.
    - Time: Implementing features using new technical skills will require time and careful planning.

- ### **Structure**

  - #### **Organization of functionality and content**

    - Header: Logo and a collapsible menu with navigational links.
    - Homepage: Question indicating the page's purpose, the button which directs to the search form.
    - Find Petsitter: contains a form that should be used to search for a pet sitter.
    - Join Us: Information on how to start advertising as a pet sitter.
    - About: Information about the site owner.
    - Contact: The form allows users to send an inquiry to the owner of the website.
    - Profile page: to display all the relevant information about a user.
    - Register: This contains the form for registering an account.
    - Login: This contains the form for logging in to the account.
    - Footer: Links to social media, newsletter and site links.

  - #### **Interaction design**

    - Collapsible menu.
    - Buttons, icons and links with hovering effect.
    - Pop up modal forms.

  - #### **Database structure**

    The diagram below illustrates the database structure used in this project, first managed using SQLite during the development process, then Postgres in production with Heroku.

    ![Attach db structure](/documents/db%20structure.png)

    - **Walkeruser**

      - The Django default User model is replaced by the custom AbstractUser because:
        - During authentication, the application uses an email address to identify uniquely.
        - The model has been extended with additional custom columns: 'is_petsitter', 'avatar', 'phone_number'.
      - Information from the User Model is used to create the UserProfile upon signing up.

    - **AddressDetails model**

      - Stores site users' detailed address information.
      - Address using a one-to-one relationship with the user model.
      - This model is used to generate an address form in the user profile.

    - **ServiceDetails model**

      - Stores all service details (dog size, amount for provide services) which pet sitter can offer.
      - This model is used to generate a pet sitter profile form in the user profile.

    - **ServiceTypes model**

      - Stores detailed information about services types which are :
        - walking in the neighbourhood.
        - boarding ate the pet sitter home.
        - daycare at the client's home.
      - Related one-to-many with service details model.

    - **PetsitterDetails model**

      - Stores pet sitter description about themselves.
      - Used to generate 'About' in the pet sitter profile.
      - Related one-to-one with the user model.

    - **Petsitterreview model**

      - Stores review details about the pet sitters such as stars rating and review description.
      - Related to the user model to verify whether the user is leaving a review for the pet sitter.
      - Related to pet sitter profile to easily retrieve information displayed in reviews.
      - Reviews cannot be displayed and visible until approved by the admin.

    - **Newsletteruser model**
      - Stores users subscribed to the newsletter.
      - Connected via webhook with "Mailchimp" service.
      - If the user resigns from receiving the newsletter, "Mailchimp" creates a request to the webhook, and the endpoint changes subscription status in the database.

- ### **Skeleton**

  - ### **Wireframes**

    - All projects was created in Adobe XD:

    - [Home page, search section, join us section](/documents/home-page-project.png)
    - [Login, register page](/documents/login-register-project.png)
    - [Pet sitter profile](/documents/petsitter-profile-project.png)
    - [Search results](/documents/search-results-project.png)

- ### **Surface / Design**

  The website feature a simple, modern and engaging design, with bright colors to arouse positive emotions among users.
  All parts of this website are custom made from the scratch.

  - #### **Imagery**

    - Hero image is designed to catch the user's attention. It also has a modern, energetic aesthetic.
    - The photos in the all sections are very positive and are meant to inspire the trust of the users.

  - #### **Colour scheme**

    The website will use the following color palette:

    ![color palette](documents/color%20palette.png)

  - #### **Typography**

    The website will use the following fonts from Google:

    - [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter?query=Architects+Daughter) for headings.
    - [Hubballi](https://fonts.google.com/specimen/Hubballi?query=Hubballi) for the rest text.

  - #### **Icons**

    Icons by font-awesome used throughout the website to allow users to quickly access functionalities.

  - #### **Styling**
    - Horizontal lines to structure and make the website's content easy to read.
    - Rounded edge borders and buttons for a more user-friendly and inviting interface.
    - Some light shadows to add further dimension and depth to the website.
    - Custom created forms.

## **FEATURES**

- ### **Existing features**

  Implemented features can be found [here](documents/features/features.md).

- ### **Features left to implement**
  - Pagination on search results.
  - Checkout and payment system.
  - Pet sitter profile extension: add a calendar, the possibility to chat with the pet sitter, and add the ability to upload documents confirming the petsitter's experience.
  - Complete automated testing in 100%.

## **DATA VALIDATION**

- #### **Search form**

  - Postcode input only accepts UK postcodes.
  - Validation is performed using the [postcodes](https://api.postcodes.io/) API, max length: 8.
  - If the postcode is invalid on the screen, an error message appears.
  - All fields are required.

  ![invalid post code](/documents/wrong-postcode.png)

- #### **Personal information form**

  - Phone number input validation is performed using [Django Phonenumber Field](https://pypi.org/project/django-phonenumber-field/0.2a3/) library, required.

  - Email: required, max length: 254, validate with built-in validator from Django.
  - First and last name : required, max_length: 100, custom Regex validator which allows only letters (also special French, German, Polish, Italian, Spanish, Swedish, Norvegian,
    Danish, Russian, Ukrainian, Serbian, Bulgarian, Belarusian letters).

  ![invalid form](/documents/personal-info-validation.png)

- #### **Address form**

  - Post Code validation is performed using the [postcodes](https://api.postcodes.io/) API, max_length=8.
  - Address 1: max length: 50, required.
  - Address 2: max length: 100, required.
  - Town: max length: 85, required.
  - County: max length: 100, required.

  ![invalid form](/documents/address-errors.png)

- #### **Upload photo**

  - Avatar: required, size validation: max size is 0.4MB.

  ![invalid image](/documents/image-validation.png)

- #### **Newsletter**

  - Email: required, max length: 254, validate with built-in validator from Django.

  ![invalid email](/documents/newsletter-error.png)

- #### **Contact form**

  - Full Name: required, max_length: 100, custom Regex validator which allows only letters and spaces,
    (also special French, German, Polish, Italian, Spanish, Swedish, Norvegian,
    Danish, Russian, Ukrainian, Serbian, Bulgarian, Belarusian letters).
  - Email: required, max length: 254, validate with built-in validator from Django.
  - Message: required, max length: 1500.

  ![contact form](/documents/contact-form-errors.png)

- #### **Reviews**

  - Stars: required
  - Description: max length: 1500.
  - The user can't write more than one review for the same pet sitter.

  ![stars](/documents/stars-validation.png)
  ![stars](/documents/double-rev-error.png)
- #### **Pet Sitter Profile Form**

  - Display add: at least one dog size must be checked to make ad visible.
  - Price inputs: at least one of two fields must be filled to continue, max price is 99.

  ![ad](/documents/displayad-error.png)
  ![prices](/documents/prices-errors.png)

## **CRUD operations and defensive design**

- ### **CRUD operations**

  | Operations                        | all users | auth. user | superuser |
  | --------------------------------- | --------- | ---------- | --------- |
  | View homepage                     | Yes       | Yes        | Yes       |
  | View about page                   | Yes       | Yes        | Yes       |
  | View contact page                 | Yes       | Yes        | Yes       |
  | View newsletter page              | Yes       | Yes        | Yes       |
  | Add/edit/delete profile           | No        | Yes        | Yes       |
  | View pet sitter profile           | No        | Yes        | Yes       |
  | View pet sitters (search results) | Yes       | Yes        | Yes       |
  | Add/edit/delete ad                | No        | Yes        | Yes       |
  | Login                             | No        | Yes        | Yes       |
  | Register                          | Yes       | No         | No        |
  | View/edit/delete my reviews       | No        | Yes        | Yes       |
  | View all reviews                  | No        | Yes        | Yes       |
  | Add/edit/delete a review          | No        | Yes        | Yes       |

- ### **Defensive design**

  - #### **Delete operations**

    - Users first need to confirm that they are sure that they want to delete:
    - The user account.
    - The review.

  - #### **Review status**

    - Reviews can be written only by the pet sitter seekers.
    - If the admin does not approve the review:
      - Review will not be displayed on the pet sitter profile page.
      - In the 'my reviews' section in the review box will display information:
        - 'waiting for approval by admin.'
    - If the admin approve the review:
      - In the 'my reviews' section in the review box will display information:
        - 'approved and visible.'
          ![admin review](/documents/reviews-list.png)

  - #### **Is active ad**

    - When the users are registered as pet sitters, they can complete their profile to display their ad.
    - There is an option to display an ad.
    - If the pet sitter sets the option to 'ON', information will be displayed.
      If the pet sitter sets the option to 'OFF', the information won't be displayed but won't be deleted in case of future mind changes.
    - Inputs, where the pet sitter can enter the price, are only active when the user first selects the size of the dog he can care for.

    ![active ad](/documents/active-ad.png)

  - #### **Status information**
    - If any of the fields are left blank, informative texts appear in their place or toast message on the top of the site.
    - The short texts describe what is missing in a given place.

## **TECHNOLOGIES USED**

- ### **Languages**

  - [HTML](https://html.spec.whatwg.org/multipage/)
  - [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
  - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [Python](https://www.python.org/)

- ### **Databases platform and cloud storage**

  - [SQlite](https://www.sqlite.org/index.html): SQL database engine provided by default as part of Django and used during development.
  - [Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql): SQL database service provided directly by Heroku for storing data.
  - [Cloudinary](https://cloudinary.com/): to store images and static files in production.
  - [Heroku](https://www.heroku.com/): to deploy and run the application in production.

- ### **Libraries and frameworks**

  - [Django](https://www.djangoproject.com/): Python web framework for rapid development and clean, pragmatic design.
  - [Django Phonenumber Field](https://pypi.org/project/django-phonenumber-field/0.2a3/): uk phone numbers validation.
  - [Pillow](https://pillow.readthedocs.io/en/stable/): This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities.
  - [Jquery](https://jquery.com/): to DOM manipulation and event handling.
  - [Django Allauth](https://django-allauth.readthedocs.io/en/latest/index.html): using for registration, and social account authentication.
  - [Django cleanup](https://pypi.org/project/django-cleanup/): to automatically delete images / files when an ImagField is removed / updated or deleted.
  - [Flake8](https://pypi.org/project/flake8-django/): A plugin to detect bad practices on Django projects.
  - [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/): Coverage.py is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes. the source to identify code that could have been executed but was not.
  - [Black](https://pypi.org/project/black/): for the uncompromising Python code formatter.
  - [Django REST](https://www.django-rest-framework.org/): for Mailchimp webhook

- ### **Other technologies**

  - [Google font](https://fonts.google.com/): used for body and headings font.
  - [Font Awesome](https://fontawesome.com/): used for icons throughout the website.
  - [Postcodes Io](https://api.postcodes.io/): Postcodes & Geolocation API for the UK.
  - [Mailchimp](https://mailchimp.com/): Marketing platform used for newsletter.
  - [Dbdiagram.io](https://dbdiagram.io/home): to design schema of relational database.
  - [W3C Markup Validation Service](https://validator.w3.org/): to check there's not error in HTML.
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This tool was used to check there's no error in the CSS code.
  - [PEP8 online](http://pep8online.com/): to validate python syntax.
  - [JSHint](https://jshint.com/): to validate jquery/javascript syntax.
  - [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Google inspect was used to test and fix code and page responsiveness.
  - [Google lighthouse](https://developers.google.com/web/tools/lighthouse): Google lighthouse was used to assess performance of the site.
  - [Travis CI](https://www.travis-ci.com/): to sync with my GitHub for testing code before pulls and merges.
  - [Doogal](https://www.doogal.co.uk/RandomAddresses.php): random UK addresses generator.
  - [Visual Studio Code](https://code.visualstudio.com/): was used to create and store code.
  - [GitHub](https://github.com/): used to store the code of the project.
  - [Adobe XD](https://www.adobe.com/products/xd/pricing/free-trial.html): for website projects.
  - [Compress](https://compressgif.com/): for compress images.
  - [Realfavicongenerator](https://realfavicongenerator.net/): for favicon.
  - [TablePlus](https://tableplus.com/): for database management.
  - [TempMail](https://temp-mail.org/en/): generates temporary emails for registering an account.

## **TESTING**

- ### **Introduction**

  - The website was tested as it was developed with the implementation of new features, using:

    - console.log() and google developer tools
    - terminal for backend functionalities by printing expected outcome
    - manual testing
    - automated testing
    - Travis CI for testing code before pull and merge on GitHub:

      ![travis](/documents/travis-ci-merge-check.png)
      ![travis](/documents/travis-ci-merge-complete.png)

- ### **Testing User Stories**

  - Testing User Stories can be found [here](/documents/features/test_user_stories.md).

- ### **Automated testing**

  - I implemented 81 automated testings.
  - For measuring code coverage I used the Coverage.py tool.
  - To check coverage in the HTML format run in the terminal:
    - "coverage run --source='.' manage.py test
    - "coverage html"
    - Open the link that appeared in the terminal.
    - Display the HTML code in the browser with the Live Server.

  ![coverage tests](/documents/coverage-tests.png)

  - ### **Testing accessibility and performance**

  - Testing through Lighthouse in Chrome extension:

    - For desktop:

    | Section        | Performance | Accessibility | Best Practices | SEO |
    | -------------- | ----------- | ------------- | -------------- | --- |
    | Home           | 95          | 92            | 92             | 90  |
    | About          | 97          | 97            | 100            | 90  |
    | Contact        | 93          | 98            | 100            | 90  |
    | Find Petsitter | 96          | 87            | 100            | 90  |
    | Join Us        | 97          | 87            | 100            | 90  |
    | Register       | 91          | 98            | 100            | 90  |
    | Log In         | 93          | 98            | 100            | 90  |
    | Error pages    | 95          | 100           | 100            | 90  |

    - For mobiles:

    | Section        | Performance | Accessibility | Best Practices | SEO |
    | -------------- | ----------- | ------------- | -------------- | --- |
    | Home           | 84          | 92            | 100            | 92  |
    | About          | 81          | 100           | 100            | 92  |
    | Contact        | 85          | 100           | 100            | 92  |
    | Find Petsitter | 82          | 89            | 100            | 92  |
    | Join Us        | 84          | 89            | 100            | 92  |
    | Register       | 83          | 98            | 100            | 92  |
    | Log In         | 80          | 98            | 100            | 92  |
    | Error pages    | 76          | 100           | 100            | 92  |

  - ### **Interesting issues and known bugs**

    1. Thanks to the "Allauth" library, I added the ability to register or log in using social media: Facebook and Google. While testing, I discovered a bug in my application.

       - How I discovered the bug:

         - I registered with the Goggle.
         - Again, I tried to register to the same email address but using Facebook.
         - The same error occurred when I tried to register to an email address that already existed in the database.
         - This error is displayed on the screen:

         ![social media bug](/documents/socialaccount-bug.png)

       - The steps I have taken to solve the problem:

         - I deleted my account.
         - I tried to register in reverse order.
         - I was looking for this bug on the internet.

       - Solution:

         - Override the Allauth SocialAccountAdapter class in the adapter.py file.
         - Method "pre_social_login" checks if the provided e-mail address already exists in the database:
           - If yes, it will connect the accounts with the Allauth template.
           - If no, it will create the account.

    2. I used the newsletter form in base.html because I wanted it to be available on every page.

       - How I discovered the bug:

         - I created a form in the newsletter app and tried to display it in base.html, but the form didn't display.

       - The steps I have taken to solve the problem:

         - I was looking for this bug on the internet.

       - Solution:

         - Create a context_processors.py file in the walker's app.
         - Create a global_variable function which returns context which can display globally.

    3. To register via social media, I had to enter information in the admin panel.

       - How I discovered the bug:

         - I'm not sure what I did. Probably I accidentally deleted a sample domain of the site in the admin panel and created another one.
         - This error is displayed on the screen:

       ![social media bug](/documents/siteid.png)

       - The steps I have taken to solve the problem:

         - I was looking for this bug on the internet.

       - Solution:

         - Change SITE_ID in the settings.py from 1 to 2.

    4. A known bug that I can't fix.

       - How I discovered the bug:

         - I have sent myself a link to my page in the Messenger App.
         - I tried to register via Google.
         - This error is displayed on the screen:

         ![social media bug](/documents//403error.png)

         - When I tried to register or log in via Facebook, there wasn't any bug, but I couldn't continue registering as well.

       - The steps I have taken to solve the problem:

         - I was looking for this bug on the internet.
         - Tried changing settings in my Google Platform account and Facebook for developers account and settings.py file.

       - Solution:

         - The error: "disallowed_useragent" will occur because the app makes a login request that Google and Facebook reject.
           The most common reason for this rejection is an unauthorized browser agent (the app uses a deprecated browser agent that Google no longer accepts).
         - This error did not appear when I tried to register or log in using a secure browser for example Google Chrome.

- ### **Code validation**

  - #### **W3C HTML Code Validator**

    Each page for the website was run through the [W3C Markup Validation Service](https://validator.w3.org/) and returned no errors.
    As all web pages are rendered dynamically using the Django template, each page and scenario had to be validated by direct input by copying and pasting the source code for the page.

  - #### **W3C CSS Jigsaw Validator**

    Each CSS file was tested with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) via direct input and returned no errors

  - #### **JSHint validator**

    All JavaScripts files were tested with [JSHint](https://jshint.com/) and returned no errors.

  - #### **Python 8**

    Each python file was run through [PEP8 online](http://pep8online.com/) and returned no errors.

  - ### **Responsiveness and compatibility**

    The website was tested on Google Chrome, Mozilla Firefox, Opera and Safari browsers.
    The Safari browser doesn't support the 'smooth' behaviour parameter in the window.scroll() method.
    The website was viewed on a variety of devices such as Desktop, Laptop (Macbook Pro 16 inch), Mobiles( Huawei P20 Mate, Huawei P30, Samsung S21 ultra).
    A large amount of testing was done to ensure that all pages were linking correctly.
    Friends and family members were asked to review the site and documentation to identify bugs and user experience issues.

## **DEPLOYMENT**

- ### **Deployment on Heroku**

  - This project is deployed on Heroku for production, with all static and media files stored on Coudinary. These are steps to deploy on Heroku:

  - Navigate to Heroku.com, create a new account or login if you already have an account. On the dashboard page, click "Create New App" button. Give the app a name. Set the region closest to you, and click "Create App".
  - On the resources tab, provision a new Heroku Postgres database.
  - Configure variables on Heroku by navigating to Settings, and click on Reveal Config Vars. You may not have all the values yet. Add the others as you progress through the steps.  
     Varables | Key |
    ---| ---  
     CLOUDINARY_URL | generated in Cloudinary account  
     DATABASE_URL | your database url  
     EMAIL | your email used for SMTP configuration  
     EMAIL_PASSWORD | your email password used for SMTP configuration  
     ENV | PRODUCTION
    MAILCHIMP_API_KEY | generated in Mailchimp account  
     MAILCHIMP_DATA_CENTER | generated in Mailchimp account  
     MAILCHIMP_EMAIL_LIST_ID | generated in Mailchimp account
    SECRET_KEY | your secret key

  - install dj_database_url and psycopg2.

  ```
  pip3 install dj_database_url
  pip3 install psycopg2-binary
  ```

  - Set up a new database for the site by going to the project's settings.py and importing dj_database_url. Comment out the database's default configuration, and replace the default database with a call to dj_database_url. parse and pass it the database URL from Heroku (you can get it from your config variables in your app setting tab)

  ```
  DATABASES = {
    'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
  }
  ```

  - Run migrations

  ```
  python3 manage.py migrate
  ```

  - Set up a new superuser, fill out the username, email address, and password.

  ```
  python3 manage.py create superuser
  ```

  - Remove the database config from Heroku and uncomment the original config. Add a conditional statement to define that when the app is running on Heroku. we connect to Postgres, and otherwise, we connect to Sqlite.

  ```
  if os.getenv("ENV") == "PRODUCTION":
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
  else:
      DATABASES = {
          "default": {
              "ENGINE": "django.db.backends.sqlite3",
              "NAME": BASE_DIR / "db.sqlite3",
          }
      }
  ```

  - Install gunicorn (if you haven't) which will act as the webserver, and put it on the requirements.txt.

  ```
  pip3 install gunicorn
  pip3 freeze > requirements.txt
  ```

  Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.

  - Create a Procfile, to tell Heroku to create a web dyno, which will run unicorn and serve the Django app.

  Inside the Procfile:

  ```
  release: python manage.py migrate
  web: gunicorn walkers.wsgi
  ```

  - Login to Heroku through CLI, using `heroku login`. Once logged in, disable the collect static temporarily, so that Heroku won't try to collect static files when it deploys.

  ```
  heroku config:set DISABLE_COLLECTSTATIC=1 --app walkers88
  ```

  And add the hostname of the Heroku app to allowed hosts in the project's settings.py, and also add localhost so that Gitpod will still work as well:

  ```
  ALLOWED_HOSTS = ["walkers88.herokuapp.com", "localhost", "127.0.0.1"]
  ```

  - Add, commit, and push to Github and then to Heroku. After pushing to Github as usual, initialize git remote first:

  ```
  heroku git:remote -a walkers88
  ```

  Then push to Heroku:

  ```
  git push heroku main
  ```

  - Go to the app's dashboard on Heroku and go to Deploy. Connect the app to Github by clicking Github and search for the repository. Click connect. Also enable the automatic deploy by clicking Enable Automatic Deploys, so that everytime we push to github, the code will automatically be deployed to Heroku as well.
  - Go back to settings.py and replace the secret key setting with the call to get it from the environment, and use empty string as a default.

  ```
  SECRET_KEY = os.environ.get('SECRET_KEY', '')
  ```

  Set debug to be true only if there's a variable called development in the environment.

  ```
  if os.getenv("ENV") == "PRODUCTION":
    DEBUG = False
    X_FRAME_OPTIONS = "SAMEORIGIN"
  else:
    DEBUG = True
  ```

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

  - Text for reviews, about Walkers and about pet sitter was taken from [Rover](https://www.rover.com/) website.

  - [Unsplash](https://unsplash.com/): for images
  - [Lottiefiles](https://lottiefiles.com/): for used animations
  - [Pixlr](https://pixlr.com/pl/): was used to process used photos
  - [CSS Scan](https://getcssscan.com/css-box-shadow-examples): for box shadow example
  - [Free Frontend](https://freefrontend.com/): for CSS and JavaScript inspirations
  - [Crello](https://create.vista.com/pl/home/): for create the logo
