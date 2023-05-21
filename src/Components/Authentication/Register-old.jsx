import { useState } from "react";
function Register() {

    let [formData, setFormData] = useState({
        username: "",
        password: "",
        password2: "",
        passErr: "",
        nameErr: "",
    })
    const usernamePattern = /^[a-zA-Z]{3,15}$/;
    const passwordPattern = /^[a-zA-Z0-9]{3,15}$/;

    function submit(event) {
        event.preventDefault();
        validateFormData()
        console.log("submit");
        console.log(formData);
    }
    function changeData(event) {
        let name = event.target.name;
        let value = event.target.value;
        setFormData({...formData, [name]: value});
    }
    
    function validateFormData() {
        if (formData.password != formData.password2) {
            let err = "Passwords do not match"
            setFormData({...formData, "passErr": err})
        } 
        else if (!passwordPattern.test(formData.password)) {
            let err = "Password must be 3-15 characters long"
            setFormData({...formData, "passErr": err})
        }
        else {
            setFormData({...formData, "passErr": ''})
        }

        if (!usernamePattern.test(formData.username)) {
            let err = "Username must be 3-15 characters long"
            setFormData({...formData, "nameErr": err})
        }
        else {
            setFormData({...formData, "nameErr": ''})
        }
    }

    // let a = {name: 'a', age: 20}
    // let b = {name: 'b', age2: 30}
    // let merged = {...a, ...b, name:"c"}

    return (
        <>
            <form onSubmit={(e) => submit(e)}>
                <div className="form-control">
                    <b>Username:</b>
                    <input 
                        type="text" 
                        placeholder="Enter Username"
                        value={formData.username}
                        name='username'
                        onChange={(e) => changeData(e)}
                    />
                    <p style={{'color': 'red'}}>
                        <small>
                            <i>{formData.nameErr}</i>
                        </small>
                    </p>
                </div>
                <div className="form-control">
                    <b>Password:</b>
                    <input 
                        type="password" 
                        placeholder="Enter Password"
                        value={formData.password}
                        name='password'
                        onChange={(e) => changeData(e)}
                    />
                    <input 
                        type="password" 
                        placeholder="Confirm Password" 
                        value={formData.password2}
                        name='password2'
                        onChange={(e) => changeData(e)}
                    />

                    <p style={{'color': 'red'}}>
                        <small>
                            <i>{formData.passErr}</i>
                        </small>
                    </p>
                </div>
                <button type="submit">
                    Submit
                </button>
            </form>
        </>
    );
}

export default Register;