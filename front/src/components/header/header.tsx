import React, { useState, useEffect } from 'react';
import { Redirect } from 'react-router';
import MainStocksOverview from './mainStocksOverview';

const Header = (): JSX.Element => {
    const [clicked, setClick] = useState<boolean>(false);

    useEffect(() => {
        if (clicked)
            setClick(false);
    }, [clicked]);

    if (clicked) {
        return (
            <Redirect to="/"/>
        )
    }
    return (
        <div className="text-center header" onClick={() => {setClick(true)}}>
            <h1>INFINALYS</h1>
            <MainStocksOverview/>
        </div>
    );
};

export default Header;