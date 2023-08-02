import React, { useState } from 'react';

const FibonacciGenerator = () => {
  // State to store the input value for 'n'
  const [inputN, setInputN] = useState('');

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    if (!isNaN(inputN) && inputN >= 1) {
      // Redirect to the second page with the value of 'n'
      // in the URL query string
      window.location.href = `/fibonacci?n=${inputN}`;
    } else {
      // Display an alert if 'n' is not a valid positive integer
      alert("Please enter a valid positive integer.");
    }
  };

  return (
    <div>
      <h1>Fibonacci Generator</h1>
      <form onSubmit={handleSubmit}>
        {/* Label and input field for the user to enter 'n' */}
        <label htmlFor="inputN">Enter a positive integer (n):</label>
        <input
          type="number"
          id="inputN"
          min="1"
          value={inputN}
          onChange={(e) => setInputN(e.target.value)}
          required
        />
        <p></p>
        {/* Submit button to generate Fibonacci numbers */}
        <button type="submit">Generate Fibonacci Numbers</button>
      </form>
    </div>
  );
};

export default FibonacciGenerator;
