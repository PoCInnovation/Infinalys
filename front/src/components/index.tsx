import React from 'react';
import MainStocksOverview from './header/mainStocksOverview';
import LandingLayout from './body/landingLayout/landingLayout';

const Index = (): JSX.Element => (
    <div className="App">
        <div className="body">
            <LandingLayout/>
        </div>
    </div>
);

export default Index;