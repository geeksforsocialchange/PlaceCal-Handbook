Facebook Events
===============

Adding Facebook listings is now a bit harder than it used to be due to
the company over-reacting to the GDPR legislation. Hopefully in the
future, this becomes simpler but we have worked out this workaround for
now. It takes up to ten minutes to set it up.

*Please note this currently only works for Page events and not Group
events!*

You will need a PlaceCal user account to follow this guide. Get in touch
with a PlaceCal admin if you don’t have one.

.. NOTE:: Jan 2020: We’ve had reports that Facebook has added additional
          verification steps for new accounts registering Developer
          accounts and you may have to upload a scan of your
          identification to create an app as described below. We’re
          seeing if there’s anything we can do about this.

Create a Facebook App
---------------------

First, we’re going to create a Facebook App. This should be done by a
**Page Owner** or **Page Admin**.

-  Go to https://developers.facebook.com/
-  In the upper right hand corner, click on **My Apps**
-  Select **Add New App**

.. figure:: /assets/facebook/01.png
   :alt: Add new app

   Add new app

-  Fill in a name that’ll help you remember what it is and a contact
   email
-  Click **Create App ID**

.. figure:: /assets/facebook/02.png
   :alt: Add contact info

   Add contact info

Set up the app
--------------

-  Once your app has been created you will be taken to the **Add a
   Product** screen.
-  Select **Facebook Login**

.. figure:: /assets/facebook/03.png
   :alt: Facebook login

   Facebook login

-  Click on the **“www”** bubble.

.. figure:: /assets/facebook/04.png
   :alt: www button

   www button

-  Fill in **Site URL** with **placecal.org**
-  Click **Save**

.. figure:: /assets/facebook/05.png
   :alt: Set URL

   Set URL

-  Under **Facebook Login** in the left menu, click on **Settings**.
-  Set **Valid OAuth Redirect URIs** to
   https://admin.placecal.org/users/auth/facebook/callback
-  Enable **Use Strict Mode for Redirect URIs** and **Enforce HTTPs** if
   they are not automatically set to that already.
-  Click **Save Changes** at the bottom of the screen.

.. figure:: /assets/facebook/06.png
   :alt: App settings

   App settings

-  Under **Settings** in the left menu, click on **Basic**
-  Fill in **App Domain** with **placecal.org**
-  Fill in **Privacy Policy URL** with https://placecal.org/privacy
-  Click **Save Changes**

.. figure:: /assets/facebook/07.png
   :alt: Set URL

   Set URL

-  Click **Show** in the **App Secret** field. You may have to enter
   your password.
-  Keep the tab open! You’re all done.

Add the calendar to PlaceCal
----------------------------

-  Log in to your account at https://admin.placecal.org
-  Go to your profile https://admin.placecal.org/profile
-  Copy the **App ID** and **App Secret** from Facebook.
-  Click **Add New Calendar From Facebook**

.. figure:: /assets/facebook/07.png
   :alt: Add new calendar from Facebook

   Add new calendar from Facebook

-  Follow the prompts to add your calendar.
-  You’re done! Your events should start to import in the next ten
   minutes.
