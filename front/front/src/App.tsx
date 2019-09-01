import React from 'react';
import { Router, Route } from 'react-router';
import Index from './components/index';
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();

const App: React.FC = (): JSX.Element => (
    <Router history={history} >
        <Route exact path='/' component={Index}/>
    </Router>
);

export default App;
