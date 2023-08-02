import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';

const FibonacciNumbers = () => {
  // State to store the value of 'n'
  const [n, setN] = useState(null);
  // State to store the Fibonacci numbers
  const [fibonacciData, setFibonacciData] = useState([]);
  // State to store any potential error messages
  const [error, setError] = useState(null);
  // Access the history object for programmatic navigation
  const history = useHistory();

  // Get the value of 'n' from the URL query string
  const getQueryVariable = (variable) => {
    const query = window.location.search.substring(1);
    const vars = query.split('&');
    for (let i = 0; i < vars.length; i++) {
      const pair = vars[i].split('=');
      if (decodeURIComponent(pair[0]) === variable) {
        return parseInt(decodeURIComponent(pair[1]));
      }
    }
    return null;
  };

  // Fetch the Fibonacci numbers when the component mounts
  useEffect(() => {
    
    // Get the value of 'n' from the URL query string
    const nValue = getQueryVariable('n');
    
    if (!isNaN(nValue) && nValue >= 1) {

      // Update the 'n' state with the extracted value
      setN(nValue);

      // Fetch Fibonacci series from the backend API with the query string 'n'
      fetch(`http://127.0.0.1:5000/home?n=${nValue}`)
        .then((response) => response.json())
        .then((fibonacciData) => {
          // Assuming the backend returns the Fibonacci numbers as a Python list in JSON format
          if (Array.isArray(fibonacciData)) {
            // Update the 'fibonacciData' state with the fetched data
            setFibonacciData(fibonacciData);
          } else {
            // If the data format is incorrect, display an error message
            setError("Error fetching data from the server.");
          }
        })
        .catch((error) => {
          // If there's an error in the fetch, display an error message
          setError("Error: " + error.message);
        });
    } else {
      // If 'n' is not a valid positive integer, display an error message
      setError("Invalid input! Please go back and enter a valid positive integer.");
    }
  }, []);

  return (
    <div>
      <h1>Fibonacci Numbers</h1>
      {n !== null && <p>First {n} Fibonacci numbers:</p>}
      {error ? (
        // Display error message if there's an error
        <p>{error}</p>
      ) : (
        // Display the list of Fibonacci numbers and the "Go Back" button
        <div>
          <p id="fibonacciList">{fibonacciData.join(", ")}</p>
          <button onClick={() => history.goBack()}>Go Back</button>
        </div>
      )}
    </div>
  );
};

export default FibonacciNumbers;
