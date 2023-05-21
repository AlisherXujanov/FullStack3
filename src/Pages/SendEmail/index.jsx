import "./sendEmail.scss";
import { useRef } from 'react';
import emailjs from '@emailjs/browser';



function SendEmail(props) {
    const form = useRef(); // reference to the form element


    const submit = (e) => {
        e.preventDefault(); // prevents the page from reloading when you hit “Send”

        emailjs.sendForm('SERVICE_ID', 'TEMPLATE_ID', form.current, 'PUBLIC_KEY')
            .then((result) => {
                alert('Message Sent', result.text);
                // show the user a success message
            }, (error) => {
                alert('An error occurred, Please try again', error.text);
                // show the user an error
            });

        e.target.reset(); // resets the form after submission
    }

    return (
        <div className="email-form">
            <h1>Send Email</h1>

            <form ref={form} onSubmit={(e) => submit(e)}>
                <label htmlFor="exampleInputEmail1">Email address</label>
                <input
                    type="email"
                    id="exampleInputEmail1"
                    placeholder="Reciever email address"
                    name='user_email'
                />
                <small id="email-help">
                    We'll never share your email with anyone else.
                </small>

                <label htmlFor="exampleFormControlTextarea1">Message</label>
                <textarea
                    id="exampleFormControlTextarea1"
                    rows="3"
                    placeholder="Enter your message here..."
                    name="message"
                ></textarea>
                <small id="message-help">
                    Text area for your message.
                </small>

                <button type="submit">
                    Submit
                </button>
            </form>
        </div>
    );
}

export default SendEmail;