# FEATURES

  [Return to main ReadMe](/README.md#features)


- ## **Responsive on all devices:**

    ![responsive]()

- ## **Collapsible and interactive navbar:**

    - The website features a navigation menu on top of the page to allow users to easily navigate throughout the website.
    - The navigation is collapsible on mobile devices for better visibility.
    - The navbar closes automatically after scrolling to a section.
    - Once a user is logged in, the navigation bar will update to functional icons allowing the user to access all the features on the website. If the user has a new notification, a little indicator is displayed with the number of new notifications.

    ![navbar](/documents/navbar-desktop.png)
    ![navbar](/documents/navbar-mobile.png)

- ## **Interactive design:**

    - All interactive elements - including icons, links and buttons - feature hovering effects and all modals.


- ## **Back to top button:**

    - When the page is scrolled down, the button appears in the lower right corner.
    - After pressing the button, the page automatically scrolls to the home page, and the button disappears.

    ![back to top button](/documents/back-to-top-button.png)


- ## **Newsletter window:**

    - In the newsletter window appears after pressing the 'subscribe' button in the footer.
    - After clicking the 'subscribe' button appears a message with thanks for subscribing to the newsletter which disappears by itself after 3 seconds.

    ![newsletter](/documents/newsletter.png)


- ## **Contact form:**

    - The contact form allows the user to contact the owner of the platform.
    - After sending the inquiry, the user will automatically receive an e-mail confirming that Walkers has received the message.

    ![contact form](/documents/contact-form.png)


- ## **Home page:**

    - Depending on whether the user is the pet sitter or not, the website display different home page content.
    
    - ### **Pet sitter/ dog walker:**

        - Home page display text for people who want to advertise their services.

        ![home pet sitter](/documents/home-pet-sitter.png)


    - ### **Pet sitter/ dog walker seeker:**

        - Home page display text for people who looking for dog sitters.

        ![home pet sitter seeker](/documents/home.png)


- ## **Register page:**

    - This page features a form asking the user for their email address and password.
    - The user can choose to register via social media: Google or Facebook.
    - When registering, the user must indicate whether he is a pet sitter or not. For this, there is a query that is highlighted in red and a box that should be checked if the user is a pet sitter.
    - When a user registers via social media, the same query appears. The user must indicate whether he is a pet sitter or not.
    - Once completed the user is redirected to a home page.
    

    ![register page](/documents/register.png)
    ![question](/documents/question.png)


- ## **Log in page:**

    - This page features a form asking the user for their email address and password.
    - The login page also features a link allowing the user to reset their password and remember log in information.
    - The user can choose to log in also via social media: Google or Facebook.

    ![log in](/documents/log-in.png)


- ## **Reset password:**

    - The user will be asked for their email and a reset link with a token will be sent to the email address provided should it exist in the database.
    - Once clicking on the reset link, the user is redirected to a form prompting for a new password and confirmation of that password.
    - Upon the submitting the new password the user is redirected to the log in page.

    ![reset password](/documents/reset-password.png)


- ## **Profile page:**


    - My profile page features the user's personal information, address details, upload photo, account settings . The user is able to update each section as well as changing the password. The page will be updated upon submitting the new information.
    - This page also features the ability for the user to delete their account.
    - The platform supports two types of users: pet sitters/dog walkers and pet sitters/dog walkers seekers, so depending on this two types, the website display extra content after register.

    ![petsitter profile](/documents/petsitter-profile.png)


    - ### **Pet sitter/ dog walker:**
        
        - Profile page contains extra 'Petsitter profile' section which contains forms to be filled in, which then appear in pet sitter profile page.

        ![petsitter profile form](/documents/petsitter-profile-form.png)

    - ### **Pet sitter/ dog walker seeker:**

        - Profile page contains extra 'My reviews' section which directs to  reviews list which was written by user.
        - The user can edit and delete reviews.
        - If the user has not wite any review, the information is displayed.

        ![reviews list](/documents/no-petsitter-profile.png)
        ![reviews list](/documents/reviews-list.png)
        ![edit review](/documents/edit-review.png)
        ![no review](/documents/no-reviews.png)


    - ### **Personal Information:**

        ![personal information](/documents/personal-info.png)


    - ### **Address Details:**

        ![address details](/documents/address-details.png)


    - ### **Edit Account:**

        ![edit account](/documents/edit-account.png)

        - In this section user can change password and delete account

        ![change password](/documents/change-password.png)
        ![delete account](/documents/delete-account.png)


    - ### **Upload Photo:**

        ![upload photo](/documents/upload-photo.png)


- ## **Contact Form:**

    - In the contact section is a form that allows the user to send a message to the company owner.

    ![contact form](/documents/contact-form.png)



- ## **Search Form:**

    - Search form allows users to find pet sitter in their area.
    - The form contains essential information that will allow the user to find the right person for his/her dog.

    ![search form](/documents/search.png)

    - The results are presented in the form of a list of user cards which after click on it leads to pet sitter profile.

    ![results](/documents/success-search.png)

    - If the user cannot find anyone, an appropriate message appears

    ![no pet sitters](/documents/fail-search.png)


- ## **Pet sitter Profile:**

    - 'Pet sitter profile' show all the information about a particular pet sitter:

        - pet sitter image/avatar
        - contact details
        - description
        - star rating
        - reviews carousel
        - 'write review' button
        - 'check prices' button

    - User only can see the pet sitter profile after registration

    ![pet sitter profile](/documents/petsitter-prof.png)

    - ### **Pet sitter image/avatar:**

        - Shows a picture of a pet sitter
        - If the pet sitter hasn't uploaded any photos, there's an icon

        ![no-avatar](/documents/no-avatar.png)


    - ### **Contact Details:**

        - That part contains email and phone no of the pet sitter
        - The seeker may contact the pet sitter in one of the possible ways
        - If the pet sitter did not provide a phone number, an appropriate message appears 

        ![no-phone-no](/documents/no-phone.png)


    - ### **Description:**

        - The description contains information that pet sitter wrote about himself/herself
        - If the pet sitter did not provide a description, an appropriate message appears 

        ![no phone no](/documents/no-description.png)


    - ### **Star Rating:**

        - The star rating represents the average of all ratings a pet sitter has received.
        - If the pet sitter has not received any reviews, the stars remain blank

        ![star rating](/documents/star-rating.png)
        ![no review rating](/documents/no-review.png)


    - ### **Reviews Carousel:**

        - Pet sitter reviews are appear as carousel.
        - Each review includes: the date it was issued, the number of stars the reviewer gave, a photo of the reviewer and a description
        - The next or preview reviews can be seen after pressing the buttons underneath

        ![reviews carousel](/documents/reviews-carousel.png)

        - If the pet sitter has not received any reviews, an appropriate message appears

        ![no review yet](/documents/no-review-yet.png)



    - ### **Write Review Button:**

        - This button lead to new form where user can write a review about the pet sitter

        ![write review](/documents/write-review.png)

        - To give a rating, it is enough to press the appropriate number of stars
        - There is also a textarea under the stars where the user can write opinion

        ![review](/documents/review.png)

        - Review does not appear immediately in the pet sitter profile
        - To be displayed, it must first be approved by the admin

        ![review in pet sitter profile](/documents/review-profile.png)


    - ### **Check Prices Button:**

        - This button which open modal with prices what pet sitter is expecting for his/her services

        ![prices](/documents/prices.png)

        - The next or preview prices can be seen after pressing the buttons underneath


       
