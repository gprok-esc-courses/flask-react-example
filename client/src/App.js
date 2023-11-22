import { BrowserRouter, Link, Route, Routes } from "react-router-dom"
import './App.css';
import Contacts from './components/Contacts';
import AddContact from './components/AddContact';
import Home from './components/Home';
import { useEffect, useState } from 'react';

function App() {

  const [contacts, setContacts] = useState([])


  function getContacts() {
    fetch('http://127.0.0.1:5000/api/v1.0/contacts')
    .then(response => response.json())
    .then(data => {
      console.log(data)
      setContacts(data['contacts'])
    }) 
  }

  return (
    <BrowserRouter>
      <div>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/contacts">Contacts</Link></li>
          <li><Link to="/add/contact">Add Contact</Link></li>
        </ul>
        <button onClick={getContacts}>Get Contacts</button>
      </div>
      <Routes>
        <Route path="/contacts" element={<Contacts contacts={contacts} />} />
        <Route path="/add/contact" element={<AddContact />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
