import { useState } from "react";

const AddContact = () => {

    const [name, setName] = useState('')
    const [email, setEmail] = useState('')
    const [message, setMessage] = useState('')

    function addContact() {
        fetch('http://127.0.0.1:5000/api/v1.0/contact', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({name: name, email: email})
        })
        .then(response => response.json())
        .then(data => {
            setMessage(data['result'])
        })
    }

    return (
        <div>
            <h1>Add Contact</h1>

            <div>{message}</div>

            <input type="text" placeholder="Name" onChange={(e) => setName(e.target.value)} />
            <input type="text" placeholder="Email" onChange={(e) => setEmail(e.target.value)}/>
            <button onClick={addContact}>Add</button>

        </div>
    )
}

export default AddContact;