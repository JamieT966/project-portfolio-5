<h1 align="center">Chem-eShop</h1>

[View the live project here](https://chem-eshop.herokuapp.com/)

At the beginning of the pandemic, as sellers of PPE, Chemstore Group set up an online ecommerce store on the Shopify platform. While the Shopify platform is great it has its limitations and costs.

My project features a full ecommerce store that allows users to view chemical safety products. Users are able to fiter them by category, sort by price, name, category, and then add to their bag and checkout securely.

Users can also leave reviews on products, sign up to our newsletter and contact us regarding a product.

![Am I responsive](documentation/images/am-i%20-responsive.png)


## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## User Experience (UX)

### User stories :

- All user stories can be seen here [Chem-eShop Issues](https://github.com/JamieT966/project-portfolio-5/issues)

  <details>
    <summary>Site User Stories</summary>

    - As a **site user** I want to be able to **register for an account** so that I can **have a personal account with my delivery details saved**

    - As a **site user** I want to be able to **login and logout** so that I can **access my profile info**

    - As a **site user** I want to be able to **receive an email confirmation after sign up** so that I can **verify my account registration was successful**

    - As a **site user** I want to be able to **have a personalised user profile** so that I can **view my order history and delivery information**

    - As a **site user** I want to be able to **leave a product review** so that I can **advise potential customers with my advise**

    - As a **site user** I want to be able to **sign up to a newsletter** so that I can **get the latest news and offers**

    - As a **site user ** I want to be able to **unsubscribe for the newsletter ** so that I can **stop receiving emails**

    - As a **site user** I can **return to Home after http 404 or 500 response** so that **I feel I am still working within the website and can navigate easily**

  </details>

  <details>
    <summary>Shopper User Stories</summary>

    - As a **Shopper** I want to be able to **view a list of products** so that I can **select a product to purchase**

    - As a **shopper** I want to be able to **view individual products** so that I can **check price, description, images and sizes**

    - As a **shopper** I want to be able to **view my total cost** so that I can **I don't spend too much**

    - As a **shopper** I want to be able to **sort any list of products** so that I can **easily sort by price, best rated, etc**

    - As a **shopper** I want to be able to **sort products into categories** so that I can **split products into categories to make it easier to find what I want**

    - As a **shopper** I want to be able to **search a product by name** so that I can **easily find the product I am searching for**

    - As a **shopper** I want to be able to **select a specific size** so that I can **I can make sure the product will suit my needs**

    - As a **shopper** I want to be able to **view the items in my bag** so that I can **check out my bag contents and know exactly what I am buying**

    - As a **shopper** I want to be able to **adjust the quantity of items in my bag** so that I can **easily make changes**

    - As a **shopper** I want to be able to **enter my card details** so that I can **make a purchase**

    - As a **shopper** I want to be able to **view my order after I complete a purchase** so that I can **verify I have not made any mistakes**

    - As a **shopper** I want to be able to **receive an email confirmation after making a purchase** so that I can **keep the confirmation for any future needs**

    - As a **shopper** I want to be able to **contact Chemstore** so that I can **get in touch regarding a product/ issue, etc**

  </details>

 <details>
    <summary>Admin Stories</summary>

    - As an **admin** I want to be able to **add a product** so that I can **I can add new products my store**

    - As an **admin** I want to be able to **edit a product** so that I can **make changes to any product**

    - As an **admin** I want to be able to **delete a product** so that I can **remove an item that is no longer for sale**

    - As an **admin** I want to be able to **view all messages from the contact form** so that I can **communicate with customers in a timely manner**

    - As an **admin** I want to be able to **view all messages from the contact form** so that I can **communicate with customers in a timely manner**

    - As an **admin** I want to be able to **view a list of subscribers in my admin** so that I can **see the amount of subscribers we have**

    - As an **admin** I want to be able to **export a CSV list of my subscribers** so that I can **can use them in marketing campaigns using tools like Mail Chimp**

  </details>    


## Features

### Existing Features

#### - Header

The header features the Chemstore logo, navigation for products in the centre and three icons to the right, a search icon, an account icon and a bag icon.

![Header](documentation/images/header.png)


#### - Search Icon and Overlay

The search icon when clicked brings up a search input below, this can be used to search the site for all products. An autofocus was added so when the search icon is clicked the user's type is on the search input.

![Search Icon and Overlay](documentation/images/search-overlay.png)


#### Account Dropdown

When clicked the account icon will display a dropdown list. Depending on the logged in status of the site user you will see different links. When the user is logged out they will see 'Register', 'Login' and 'Contact'. If the user is logged in they will see 'My Profile', 'Logout' and 'Contact'. Finally, if an admin user is logged in they will see 'Product Managment', 'My Profile', 'Logout' and 'Contact'.

![Account Dropdown](documentation/images/account-dropdown.png)


#### Bag Notification

If the user currently has nothing in their bag they will just see a bag icon. If the user adds a product or products to their bag a green circle/ bubble will appear with the number of items in their bag.

![Bag Notification](documentation/images/header-bag.png)


#### Hero Section

The hero section is quite simple featuring an illustration of an ecommerce style image to the right and an a site intro on the left. The hero section also features a button to 'Shop Now' that takes the user to the all products page.

![Hero Section](documentation/images/hero-section.png)


#### Product Categories

Below the hero section is a Product Categories section. This section features five cards with an image. Each card will grow on hover and when clicked will take the user to that product category.

![Product Categories](documentation/images/product-categories.png)


#### About Us Section

Next we have the about us section. Again, another simple section featuring a small word on the company on the right and an image of a chemical safety worker on the right.

![About Us Section](documentation/images/about-us.png)


#### Our Client Carousel

At the bottom of the homepage is a carousel style section featuring some of Chemstore's previous clients. This has been animated to automatically scroll across the screen.

![Our Client Carousel](documentation/images/our-clients.png)


#### Footer

Finally the homepage features a footer. This footer is split into four sections. Firstly, the address section, then the products and account links. The fourth part of the footer features the Chemstore logo, a link to sign up to the newsletter below that and then social links.

There is also a link to the privacy policy at the bottom.

![Footer](documentation/images/footer.png)


#### All Products Page

The all products page displays every product on the store as cards in rows of max 3. This page has a sort by field that allows a user to sort by price, name, rating and category. The produuct cards display the product image, title, price, rating and category below it.

The rating shown is an average of all user ratings for that product.

If the user is an admin they will see two icon buttons to edit and delete a product.

![All Products Page](documentation/images/product-page.png)


#### Edit Product

This feature is only available to admin users, when the edit button is clicked whether from the products page or product detail page it will take you to the edit product page.

An alert displays to notify the admin that they are currently editing a product. The edit product page features a rich text editor thanks to django-ckeditor.

![Edit Product](documentation/images/edit-product.png)


#### Delete Product

When the delete button is clicked the admin user will have a modal appear to confirm if the admin wants to delete the product.

![Delete Product](documentation/images/delete-product.png)


#### Product Detail Page

The product detail page features an image to the left and then on the right there is the product title, price, rating, description, the quantity and then two buttons 'Keep Shopping', that will take the user back to the products page. The 'Add to Bag' button will add the product to the user's bag.

The rating shown is an average of all user ratings for that product.

If the user is an admin they will again see two icon buttons to edit and delete a product.

![Product Detail Page](documentation/images/product-page.png)

User Added to Bag:

![User Added to Bag](documentation/images/add-to-bag.png)

If the product has sizes a sizes option will also appear on the product detail page.

![Product Sizes](documentation/images/product-with-sizes.png)


#### Product Reviews

Below the product container on the product detail page is the reviews section. When a user is signed in a product review form will show on the left side. The user reviews are then displayed on the right. These reviews have the review title, body, the user it was left by and the rating they gave.

Only the user that made the review or an admin has the ability to edit or delete it.

![Product Reviews](documentation/images/product-reviews.png)


#### Edit Review Page

When the user clicks the edit button they are taken to a page with the edit form prefilled with their previous details. At the bottom there is two buttons. The first is to 'Delete Review', this will again take the user to a modal again to confirm delete. Then there is an 'Update Review' button that updates the review.

![Edit Review Page](documentation/images/edit-review.png)


#### Add Product

As well as admin users having the ability to add products in the django admin they can also add them in the front end site. This page also features a rich text editor. 

![Add Product](documentation/images/add-product.png)


#### Bag Page

When the user is ready to progress on to the bag page they can either click the 'Go to Secure Checkout' button on the pop up that appears after adding an item to the bag or by clicking the bag icon.

The bag page features each product as displayed as a line item. The user can edit quantites or remove items from their bag with the buttons displayed.

![Bag Page](documentation/images/bag.png)


#### Checkout Page

The checkout page has a form to fill out the user's delivery details and card details. On the right is an order summary with the total cost.

![Checkout Page](documentation/images/checkout.png)


#### Checkout Success

Following a successful checkout process the user will be taken to a success screen. There is an alert with the confirmation number and email the confirmation was sent to. This page displays a summary of the order info, details, delivery details and the amount they were charged.

![Checkout Success](documentation/images/checkout-success.png)


#### Profile Page

On the my profile page the logged in user can see their saved delivery details to the left and their order history on the right. Clicking the green highlighted order number will take the user to the order confirmation history with an alert that they are viewing an old order history.

![Profile Page](documentation/images/profile-page.png)


#### Contact Page

The contact page has an embedded Google Map on the left of the location of Chemstore. Next to it is a contact form with the option to select a product if their query relates to a particular product.

![Contact Page](documentation/images/contact-page.png)


#### Newsletter Page

The newsletter sign up page features a simple input field for users to type their email address and be signed up. When submitted the user will get an alert saying that they are now signed up and receive a confirmation email.

![Newsletter Page](documentation/images/newsletter.png)


#### Unsubscribe Page

Near identical to the sign up page, the unsubscribe page has a single input field to delete their email address from our database. When submitted the user will get an alert saying that they are now unsubsribed and receive a confirmation email.

![Unsubscribe Page](documentation/images/unsubscribe.png)


#### Newsletter Admin Page

When an admin user navigates to the user page he will also see an export button. When clicked a CSV file of all newsletter sign ups will be exported for use on Chemstore's email marketing service, Campaign Monitor.

![Newsletter Admin Page](documentation/images/newsletter-admin.png)


#### Custom 404 Page

Finally, I have set up a custom 404 error page (as well as 403, 405 and 500). This presents the user with a relevant image and a link to take them back to the homepage.

![Custom 404 Page](documentation/images/404.png)


### Features which could be implemented in the future

Below are some of the features that I will be working on over the next few weeks.

- __Draft Orders__

Due to the nature of what Chemstore sell many of their customers do not know exactly what product they need. Often times customers contact them about this. On Shopify the sales person can make create a draft order that is then sent to the customer directly to pay.

- __Order Collection__

A few Chemstore customers would prefer to collect their products from the Chemstore factory, this a feature Chemstore can offer on Shopify that I would like to implement in the future.

- __Stock/ Inventory Management__

Another feature that I would like to implement in the future is an option to import an inventory file for product management.

- __Product Gallery__

Next I would like to have a product gallery on the product detail page. 

- __Shipping Costs__

With the products that Chemstore offer varying so much in size and weight I would like to have a feature that an admin can set a product's shipping cost.

- __Featured Product__

Another feature I will be implementing will be the ability to have a featured product in any given category like in my wirefreames.


## Design

### Wireframes

Below are all the wireframes that I created for this project:

<details>
    <summary>Home Page</summary>

![Home Page Wireframe](documentation/images/wireframe-home.png)


  </details>


<details>
    <summary>Products Page</summary>

![Produts Wireframe](documentation/images/wireframe-products.png)


  </details>


<details>
    <summary>Product Detail Page</summary>

![Product Detail Wireframe](documentation/images/wireframe-product-detail.png)



  </details>

<details>
    <summary>Mobile Views</summary>

![Mobile Views Wireframe](documentation/images/wireframe-mobile.png)



  </details>


### Entity-Relationship diagram for DBMS

Below is an image of my entity-relationship diagrams:


INSERT DIAGRAMS

## Planning

For this project I used Github Projects as an agile tool. I created user stories and moved them along the progression boards as I was at different stages.

Link can be found here: [Chem-eShop Github Project](https://github.com/users/JamieT966/projects/1)

## Technologies Used

### Languages Used

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks, Libraries & Programs Used  

-   [Google Fonts](https://fonts.google.com/) used for the Poppins and Open Sans fonts.
-   [Font Awesome](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.
-   [Git](https://git-scm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
-   [GitHub](https://github.com/) is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
-   [Django](https://www.djangoproject.com/) was used as the framework to support rapid and secure development of the application.
-   [Bootstrap](https://getbootstrap.com/) was used to build responsive web pages.
-   [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) used for account registration and authentication (version 0.41.0 installed because of project dependencies).
-   [Pillow](https://pillow.readthedocs.io/en/stable/index.html) - Python Imaging Library used for image handling.
-   [Django ckeditor](https://pypi.org/project/django-ckeditor/) - Renders rich text editor for various forms.
-   [jquery library](https://code.jquery.com/jquery-3.4.1.min.js) - for various pieces of functionality including adding and removing items from the shopping cart and handling the increment and decrement of the quantity control.
-   [Django crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to simplify form rendering.
-   [Django import export](https://django-import-export.readthedocs.io/en/latest/) used to export list of newsletter subscribers.
-   [Stripe](https://js.stripe.com/v3/) used for secure payments (referenced in base.html).
-   [Stripe install library](https://pypi.org/project/stripe/) used for secure payments.
-   [Django Countries](https://pypi.org/project/django-countries/) used on checkout page to pass valid country code to Stripe.
-   [Gunicorn](https://gunicorn.org/) was used as the Web Server to run Django on Heroku.
-   [dj_database_url](https://pypi.org/project/dj-database-url/) library used to allow database urls to connect to the postgres db.
-   [psycopg2](https://pypi.org/project/psycopg2/) database adapter used to support the connection to the postgres db.
-   [Amazon S3](https://aws.amazon.com/s3/) used to store static files and images.
-   [Boto3](https://pypi.org/project/boto3/) the Amazon Web Services (AWS) Software Development Kit (SDK) for Python.
-   [django_storages](https://django-storages.readthedocs.io/en/latest/) used to connect django to S3.
-   [Heroku](https://www.heroku.com) - used to host the deployed application.
-   [Heroku Postgres](https://www.heroku.com/postgres) - SQL database service provided by Heroku used to store models and data.
-   [Balsamiq](https://balsamiq.com/) was used to create the wireframes during the design process.
-   [Grammarly](https://app.grammarly.com/) was used to proof the content of my project and README.
-   [Beautifier.io](https://beautifier.io/) was used to beautify html and css.
-   [W3 HTML Validator](https://validator.w3.org/nu/) was used to validate HTML.
-   [W3 CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
-   __Adobe Photoshop__ was used to create the images for category products.


## Testing

### Validator Testing 

[W3 HTML Validator](https://validator.w3.org/nu/) found a few issues that I am going to classify as bugs.

1. Products page found an error Duplicate ID exampleModalLabel. 
- This is due to me having a modal to confirm that the user wants to delete a product or review. The modal has to be in my for loop for it to work.

2. Edit product page found multiple errors.
- These errors are being caused by a django installation, ckeditor and not due to my code.

3. Product detail page found multiple errors.
- These are again being caused by django-ckeditor.

__Pages Checked__

- Home Page
- Products Page
- Product Detail Page
- Add Product Page
- Edit Product Page
- Edit Review Page
- Profile Page
- Sign Up Page
- Unsubscribe Page
- Contact Page
- Bag Page
- Checkout Page
- Checkout Success Page
- Sign Up Page
- Login Page
- Logout Page
- 404 Page

[W3 CSS Validator](https://jigsaw.w3.org/css-validator/) found no issues.

All code has been beautified with [Beautifier.io](https://beautifier.io/)

All code has been made PEP8 compliant.

### Manual Testing Test Cases and Results 

### Known bugs

I had a an issue with my webhooks not working and confirmation emails subsequently not being sent. To fix this issue I had to copy over the entirety of Boutique Ado's checkout code. I then could not migrate these model changes to Heroku. This was eventually fixed but I thought that I should make note of it just in case.

## Deployment

<details>
    <summary>Cloning Git Repository</summary>

- Go here: https://github.com/JamieT966/project-portfolio-5/
- Click the 'Code' button to the right of the screen and click HTTPS and copy the link.
- Open a Git Bash terminal and go to the directory where you want the clone.
- Type 'git clone' then paste in the copied url, hit enter and the cloning should start.
- Type ' pip install -r requirements.txt'.
- Set DEBUG=True in the settings.py file.
- Any changes made to your local clone can be pushed by 'git add .' then 'git commit -m "message" and finally 'git push'.

  </details>


<details>
    <summary>Create App on Heroku</summary>

- Login to [Heroku](https://www.heroku.com/) or create an account.
- On Heroku dashboard, click 'Create New App', enter a name and choose your region. Click 'Create App'
- Click the 'Resources' tab.
- In the Add-ons search bar enter 'Postgres' and select 'Heroku Postgres' from the list, click the 'Submit Order Form' button on the pop-up dialog.
- Then go to 'Settings', scroll down to 'Reveal Config Vars'.
- Add a confif var DISABLE_COLLECTSTATIC, value: 1.
- Add SECRET_KEY, value: any random line of charaters and numbers.
- Go back to Gitpod, settings.py and add:
- if 'DATABASE_URL' in os.environ:

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

SECRET_KEY = os.environ.get('SECRET_KEY')
- In your Gitpod terminal type, 'python3 manage.py migrate'.
- Then 'python3 manage.py createsuperuser'.
- Set DEBUG to False in settings.py.
- Commit and push to Github.
- Add SECRET_KEY and DATABASE_URL in env.py. 

  </details>


<details>
    <summary>Connecting Heroku to Github</summary>

- Go to Heroku and go to the 'Deploy' tab.
- Select Github, login to Github and find repo.
- Scroll down and choose 'Enable Automatic Deployment'

  </details>


<details>
    <summary>Set up Amazon AWS S3 Bucket</summary>

- Create AWS account.
- On dashboard, go to S3 services.
- Create a new bucket, use a similar name to your project.
- Go to properties tab and enable static hosting, enter default values for index and error document settings.
- Go to permissions tab and change these bucket settings:

1. Add this to your Cross-origin resource sharing (CORS):
  [
  {
  "AllowedHeaders": [
  "Authorization"
  ],
  "AllowedMethods": [
  "GET"
  ],
  "AllowedOrigins": [
  "*"
  ],
  "ExposeHeaders": []
  }
  ]
  
2. Access Control List
  - Go to the Access Control List area
  - Set the list objects permission for everyone under the Public Access section and check the box to confirm you want this permission setting.

3. Generate Policy
  - Go to the bucket policy area, click on Edit and click on policy generator.  
  - Choose S3 bucket policy from drop-down.
  - Put * in Principal field.
  - Select get object from Actions drop-down.
  - Copy ARN and paste into ARN box on the policy generator page.
  - Click Add Statement.
  - Click Generate Policy then copy the policy into the policy editor window.
  - Add /* to the end of the Resource key.
  - Save.

4. Identify and Access Management (IAM)
  - Create group
  - Create policy, don't bother adding tags.
  - Attach Policy, To attach the policy, on the sidebar click 'User Groups'. Select your group, go to the permissions tab, open the 'Add permissions' dropdown, and click 'Attach policies'. Select the policy and click 'Add permissions' at the bottom.
  - Download and save the generated csv which contains the users access and secret access key.

- Go to your settings.py file in Gitpod and enter this: 

if 'USE_AWS' in os.environ:

    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = "chem-eshop"
    AWS_S3_REGION_NAME = "eu-west-1"
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

  - Go to the S3 dashboard and create a folder called media in the new bucket.  Specify grant public-read access on the folder and tick the checkbox to confirm.
  - Add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY config vars to heroku using the values from the downloaded cvs.
  - Add USE_AWS = True to the Heroku config vars.
  - Remove DISABLE_COLLECTSTATIC from config vars.

  </details>


  <details>

    <summary>Add Stripe Config Vars and Webhooks</summary>

- Create Stripe account.
- Add STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to the Heroku config vars, you'll find these on your Stripe developer dashboard.
- Go to Stripe dashboard go to the Developers, Webhooks, click add endpoint, use the url of your Heroku application with '/checkout/wh/' added to the end of the url string.  Select all events.
- When the endpoint is set up get your signing secret from the webhook add this value as a Heroku config var called STRIPE_WH_SECRET.

  </details>


## Credits 

### Code 

- I created the bulk of this project following the 'Boutique Ado' walkthrough project and had to copy the entire checkout section, which is documented in my bug errors.
- A lot of my newsletter code came from here:
[Newsletter Code 1](https://www.youtube.com/watch?v=UtV1u0pejKs&ab_channel=MasterCodeOnline) |
[Newsletter Code 2](https://www.youtube.com/watch?v=_QPuX-HD8wA&ab_channel=CodingIsThinking)
- A lot of the import/ export came from here:
[Export Code](https://python.plainenglish.io/the-easy-way-to-import-export-data-from-django-admin-fe17ecd012fb) |
[Review Stars Code](https://www.youtube.com/watch?v=gDtsAWMA3Jo&ab_channel=RathanKumar)
- The icon carousel came from tiktok user @tomisloading

### Content 

- Much of the content for products came from [Chem-eShop](https://chem-eshop.ie/). Which I used as my base idea but with the idea of improving as I went.
- The about us content came directly from [Chemstore Ireland](https://www.chemstore.ie/)
- My hero image and many of the error page illustrations came from [Many Pixels](https://www.manypixels.co/)
- 

### Acknowledgments

- Thank you to my mentor Brain Macharia for his help and feedback throughout this project.
- Thanks to the Code Institute tutors that also helped me in this project.