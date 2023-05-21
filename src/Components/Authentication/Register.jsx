import React from "react";
import registrationSchema from "./registrationSchema.scss";
import { Formik, Form, Field, ErrorMessage } from "formik";
function App() {
  return (
    <div style={registrationSchema}>
      <center>
        <h1>Register a new account</h1>
        <Formik
          initialValues={{ fullname: "", email: "", password: "" }}
          validate={(values) => {
            const errors = {};
            if (!values.fullname) {
              errors.fullname = "Required";
            }

            if (!values.email) {
              errors.email = "Required";
            } else if (
              !/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)
            ) {
              errors.email = "Invalid email address";
            }
            if (!values.password) {
              errors.password = "Required";
            }
            return errors;
          }}
          onSubmit={(values, { setSubmitting }) => {
            setTimeout(() => {
              alert(JSON.stringify(values, null, 2));
              setSubmitting(false);
            }, 400);
          }}
        >
          {({ isSubmitting }) => (
            <Form>
              <Field
                type="text"
                name="fullname"
                placeholder="Enter your fullname"
              />
              <ErrorMessage className="error" name="fullname" component="div" />

              <Field
                type="email"
                name="email"
                placeholder="Enter email address"
              />
              <ErrorMessage className="error" name="email" component="div" />

              <Field 
                type="password" 
                name="password" 
                placeholder="Enter password"
              />
              <ErrorMessage className="error" name="password" component="div" />

              <button type="submit" disabled={isSubmitting}>
                Submit
              </button>
            </Form>
          )}
        </Formik>
      </center>
    </div>
  );
}
export default App;