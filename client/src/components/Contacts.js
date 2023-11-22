
const Contacts = ({contacts}) => {
    return (
        <div>
            <h1>Contacts</h1>
            <ul>
                {contacts.map((contact, key) => <li>{contact['name']}</li>)}
            </ul>
        </div>
    )
}

export default Contacts;