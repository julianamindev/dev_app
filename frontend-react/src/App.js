import logo from './logo.svg';
import './App.css';

import { useEffect, useState } from 'react'

function App() {
  const [user, setUser] = useState([])
  useEffect(() => {
    fetch('http://localhost:4567/')
      .then(res => res.json())
      .then(data => setUser(data.user))
      .catch(error => console.error('Error fetching user:', error));
  }, [])

  return (
    // <div className="App">
    //   <header className="App-header">
    //     <h1>User</h1>
    //     {user && <div>{user}</div>} {/* Display the user string directly */}
    //   </header>
    // </div>
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Welcome user {user && <div>{user}</div>}
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          React Frontend
        </a>
      </header>
    </div>
  );
}

export default App;

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           React Frontend
//         </a>
//       </header>
//     </div>
//   );
// }
