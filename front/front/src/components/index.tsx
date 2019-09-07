import React from 'react';
import MainStocksOverview from './header/mainStocksOverview';
import LandingLayout from './body/landingLayout/index';

const Index = (): JSX.Element => (
    <div className="App">
        <div className="header">
            <MainStocksOverview/>
        </div>
        <div className="body">
            <LandingLayout/>
        </div>
    </div>
);

export default Index;