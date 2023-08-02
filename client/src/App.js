import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import FibonacciGenerator from './FibonacciGenerator';
import FibonacciNumbers from './FibonacciNumbers';

const App = () => {
  return (
    <Router>
      <Switch>
        {/* Route for the first page (FibonacciGenerator) */}
        <Route exact path="/" component={FibonacciGenerator} />
        
        {/* Route for the second page (FibonacciNumbers) */}
        <Route path="/fibonacci" component={FibonacciNumbers} />
      </Switch>
    </Router>
  );
};

export default App;
