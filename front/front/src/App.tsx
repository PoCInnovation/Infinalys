import React from 'react';
import { Router, Route } from 'react-router';
import Index from './components/index';
import { createBrowserHistory } from 'history';
import Login from './components/login';
import StockPrediction from './components/stockPrediction';
import Header from './components/header/header';
import './App.css';


const history = createBrowserHistory();

const App: React.FC = (): JSX.Element => (
    <Router history={history} >
        <Route path='/' component={Header}/>
        <Route exact path='/' component={Index}/>
        <Route exact path='/login' component={Login}/>
        <Route exact path='/app' component={StockPrediction}/>
    </Router>
);

export default App;
