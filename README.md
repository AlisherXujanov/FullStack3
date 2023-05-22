### This project is testing project of Alisher-Company for his classes

---

### Explanation of usage

- For using this project you need to install git on your computer
- Then you need to clone the repository through HTTPS
- Then you need to open the folder in your terminal
- Then you need to use _git status_ to see the status of the project
- Then you need to use _git add ._ to add all the changes into staging area
- Then you need to use _git commit -m "your message"_ to commit the changes
- Then you need to use _git push_ to push the changes into the repository
- ## Then you need to use _git pull_ to pull the changes from the repository

### INSTALL

- git clone .... => clones repository
- cd ... => change directory to that folder
- npm install => install all dependencies
- npm start => start the project

  ***

### Installing routers
1. **npm i react-router-dom@latest**
> - installs the library
2. **import { BrowserRouter } from 'react-router-dom'**  
> - this should be located in the main JS / JSX file of the project
3. **import { Routes, Route, Link, Outlet } from 'react-router-dom'**
> - This helps to create routes and links
> - Outlet should be after all links that we created for navigtion
    

### Installing formik
1. **npm install formik --save**
> - installs the library
2. **import { Formik, Form, Field, ErrorMessage } from 'formik';**
> - this should be located in the main JS / JSX file of the project

> - The Form component wraps all the form fields and provides essential context for using Formik's tools. This includes managing the form's state, handling validation, and submitting the form.
> - Field is a component provided by Formik that represents a form field. We can use this component to render an input, select, or other form elements. It automatically handles the state of the field, such as its value and validation.
> - ErrorMessage is a component provided by Formik that renders an error message for a specific field. We can use this component to display validation errors for a field. This is especially helpful for displaying form errors in a user-friendly way.


### Installing EmailJS
1. **npm install @emailjs/browser**
2. REGISTER ON emailjs.com TO GET YOUR OWN SERVICE_ID, TEMPLATE_ID, PUBLIC_KEY
<!-- 
  import emailjs from '@emailjs/browser';
  emailjs.sendForm('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', form.current, 'YOUR_PUBLIC_KEY')
     .then((result) => {
         //* show the user a success message
     }, (error) => {
         //* show the user an error
     });
-->


1. Chakra UI
> Альтернатива Bootstrap
https://chakra-ui.com/

2. Formik
> Формы
https://formik.org/

3. EmailJS
> Отправка писем (Gmail || Email  ...)
https://www.emailjs.com/

4. React Toastify
> Оповещения (уведомления похожие на alert())
https://www.npmjs.com/package/react-toastify