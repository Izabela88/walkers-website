# FEATURES

[Return to main README file](/README.md#features)

- ## **Responsive on all devices:**

  ![responsive](/documents/responsive.png)

- ## **Collapsible and interactive navbar:**

  - The website features a navigation menu on top of the page to allow users to easily navigate throughout the website.
  - The navigation is collapsible on mobile devices for better visibility.
  - The navbar closes automatically after scrolling to a section.
  - Once a user is logged in, the navigation bar will update to functional icons allowing the user to access all the features on the website.

  ![navbar](/documents/navbar-desktop.png)
  ![navbar](/documents/navbar-mobile.png)

- ## **Interactive design:**

  - All interactive elements - including icons, links and buttons - feature hovering effects and all modals.

- ## **Back to top button:**

  - When the page is scrolled down, the button appears in the lower right corner.
  - After pressing the button, the page automatically scrolls to the home page, and the button disappears.

  ![back to top button](/documents/back-to-top-button.png)

- ## **Newsletter window:**

  - The newsletter window appears after pressing the 'subscribe' button in the footer.
  - After clicking the 'subscribe' button appears a message with thanks for subscribing to the newsletter which disappears by itself after a while.

  ![newsletter](/documents/newsletter.png)

- ## **Contact form:**

  - The contact form allows the user to contact the platform owner.
  - After sending the inquiry, the user will automatically receive an e-mail confirming that Walkers has received the message.

  ![contact form](/documents/contact-form.png)

- ## **Home page:**

  - Depending on whether the user is the pet sitter or not, the website display different home page content.

  - ### **Pet sitter/ dog walker:**

    - Home page display text for people who want to advertise their services (pet sitters).

    ![home pet sitter](/documents/home-pet-sitter.png)

  - ### **Pet sitter/ dog walker seeker:**

    - Home page display text for people who looking for dog sitters (pet sitter seekers).

    ![home pet sitter seeker](/documents/home.png)

- ## **Register page:**

  - This page features a form asking the user for their email address and password.
  - The user can choose to register via social media: Google or Facebook:

    - For the process to be successful, the link to the Walkers website must be opened in a secure browser.
    - If the user tries to register an account via social media to an email that already exists, he will be redirected to a page stating that both accounts have been linked.
    - The user can add or remove one of the social accounts.
    - After click 'continue' button the user is redirect to home page"
      ![social account connections](/documents/account-connections.png)

  - When registering, the users must indicate whether they are pet sitters or not. For this, a query is highlighted in red and a box that should be checked if the user is a pet sitter.
  - When a users register via social media, the same query appears. The user must indicate whether they are a pet sitter or not.
  - Once completed, the user is redirected to a home page.

  ![register page](/documents/register.png)
  ![question](/documents/question.png)

- ## **Log in page:**

  - This page features a form asking the user for their email address and password.
  - The login page also features a link allowing users to reset their password and remember log in information.
  - The user can choose to log in also via social media: Google or Facebook.
  - For the process to be successful, the link to the Walkers website must be opened in a secure browser.

  ![log in](/documents/log-in.png)

- ## **Reset password:**

  - The users will be asked for their email and a reset link with a token will be sent to the email address provided should it exist in the database.
  - Once clicking on the reset link, the user is redirected to a form prompting for a new password and confirmation of that password.
  - Upon the submitting the new password the user is redirected to the log in page.

  ![reset password](/documents/reset-password.png)

- ## **Profile page:**

  - User can see their profile only after log in.
  - In the navigation bar is icon which, when pressed, takes straight to the user profile page.

  ![profile icon](/documents/profile-icon.png)

  - Profile page features the user's personal information, address details, upload photo, and account settings. The user can update each section. The page will be updated upon submitting the new information.
  - This page also features the ability for the users to delete their accounts.
  - The platform supports two types of users: pet sitters/dog walkers and pet sitters/dog walkers seekers, so depending on these two types, the website display extra profile page content.

  ![pet sitter profile](/documents/petsitter-profile.png)

  - ### **Pet sitter/ dog walker:**

    The Profile page contains an extra 'Petsitter profile' section that includes forms to be filled in, which appear on the pet sitter profile page.

    - The form is divided into four categories:
      - walk
      - boarding at pet sitter home
      - daycare at the client's home
      - description
    - Each category also has a button that should be marked 'ON' or 'OFF' depending on whether the information should be displayed in the ad.
    - Category 'walk', 'boarding at pet sitter home', and 'daycare at client home' are related to the type of care provided by the pet sitter.
    - Pet sitters can point out what size of dog they can look after and the amount they expect for their services.
    - In the 'description' category, the pet sitter can describe themself.

    ![pet sitter profile form](/documents/petsitter-profile-form.png)

  - ### **Pet sitter/ dog walker seeker:**

    - Profile page contains extra 'My reviews' section which directs to reviews list which was written by user.

    ![reviews list](/documents/no-petsitter-profile.png)
    ![reviews list](/documents/reviews-list.png)

    - The user can edit and delete reviews.
    - 'Edit Review' template contains:
      - the star rating that the pet sitter previously received
      - empty stars which can be marked again for re-rating
      - textarea with the previous description, which can be updated
      - bin icon, which allows the user to delete review

    ![edit review](/documents/edit-review.png)

    - Before deleting a review, a modal will appear with the question.

    ![delete review](/documents/delete-rev.png)

    - If the user has not write any review, this information is displayed.

    ![no review](/documents/no-reviews.png)

  - ### **Personal Information:**

    ![personal information](/documents/personal-info.png)

  - ### **Address Details:**

    ![address details](/documents/address-details.png)

  - ### **Edit Account:**

    ![edit account](/documents/edit-account.png)

    - In this section user can change password and delete account.

    ![change password](/documents/change-password.png)
    ![delete account](/documents/delete-account.png)

  - ### **Upload Photo:**

    ![upload photo](/documents/upload-photo.png)

- ## **Contact Form:**

  - In the contact section is a form that allows the user to send a message to the company owner.

  ![contact form](/documents/contact-form.png)

- ## **Search Form:**

  - Search form allows users to find a pet sitter in their area.
  - The form contains essential information that will allow the user to find the right person for their dog.

  ![search form](/documents/search.png)

  - The results are presented in the form of a list of pet sitter cards which after click on it leads to pet sitter profile.

  ![results](/documents/success-search.png)

  - If the user cannot find anyone, an appropriate message appears.

  ![no pet sitters](/documents/fail-search.png)

- ## **Pet sitter card:**

  - Each card includes picture of the pet sitter, name of the pet sitter, the number of reviews and the average rating shows as stars.

  ![pet sitter card](/documents/petsitters-list.png)

- ## **Pet sitter Profile:**

  - 'Pet sitter profile' show all the information about a particular pet sitter:

    - pet sitter image/avatar
    - contact details
    - description
    - star rating
    - reviews carousel
    - 'write review' button
    - 'check prices' button

  - User can see the pet sitter profile only after registration.

  ![pet sitter profile](/documents/petsitter-prof.png)

  - ### **Pet sitter image/avatar:**

    - Shows a picture of a pet sitter.
    - If the pet sitter hasn't uploaded any photos, there's an icon.

    ![no-avatar](/documents/no-avatar.png)

  - ### **Contact Details:**

    - That part contains the email and phone no of the pet sitter.
    - The seeker may contact the pet sitter in one of the possible ways.
    - If the pet sitter did not provide a phone number, an appropriate message appears.

    ![no-phone-no](/documents/no-phone.png)

  - ### **Description:**

    - The description contains information that the pet sitter wrote about themself.
    - If the pet sitter did not provide a description, an appropriate message appears.

    ![no phone no](/documents/no-description.png)

  - ### **Star Rating:**

    - The star rating represents the average of all ratings a pet sitter has received.
    - If the pet sitter has not received any reviews, the stars remain blank.

    ![star rating](/documents/star-rating.png)
    ![no review rating](/documents/no-review.png)

  - ### **Reviews Carousel:**

    - Pet sitter reviews appear as a carousel.
    - Each review includes the date it was issued, the number of stars the reviewer gave, a photo of the reviewer and a description.
    - The following or preview reviews can be seen after pressing the buttons underneath.

    ![reviews carousel](/documents/reviews-carousel.png)

    - If the pet sitter has not received any reviews, an appropriate message appears.

    ![no review yet](/documents/no-review-yet.png)

  - ### **Write Review Button:**

    - This button lead to new form where user can write a review about the pet sitter.

    ![write review](/documents/write-review.png)

    - To give a rating, the user should press the appropriate number of stars.
    - There is also a text area under the stars where users can write their opinions.

    ![review](/documents/review.png)

    - Review does not appear immediately in the pet sitter profile.
    - To be displayed, it must first be approved by the admin.

  - ### **Check Prices Button:**

    - This button opens a modal with prices that pet sitter expects for their services.

    ![prices](/documents/prices.png)

    - The next or preview prices can be seen after pressing the buttons underneath.
    - If the pet sitter doesn't have any active ads, the 'check price' button is disabled.

  - ### **Toast Window:**

    - The toast box has an informative task.
    - It displays in the centre of the page at the top.
    - It contains short texts informing about mistakes made by the user, warnings, errors or actions taken by the system.

    ![prices](/documents/toast.png)

  - ### **Welcome Message:**

    - After logging into the user account, a welcome message appears in the navigation bar.
    - If the user does not enter their first name, only "hello" without a first name will be displayed.

    ![prices](/documents/welcome-msg.png)

  - ### **Admin Panel:**

    - The administration panel allows the owner to manage users who:
      - are signed up for the newsletter
      - given reviews
      - have registered an account

    ![prices](/documents/admin-panel.png)

    - The newsletter:

    ![prices](/documents/admin-newsletter.png)
    ![prices](/documents/admin-newsletter-2.png)

    - The reviews:

    ![reviews](/documents/admin-reviews.png)
    ![reviews](/documents/admin-reviews-2.png)

    - The users:

    ![users](/documents/admin-users.png)
    ![users](/documents/admin-users-2.png)
