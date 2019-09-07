import React, { useState, useEffect } from 'react';
import { Redirect } from 'react-router';

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
        </div>
    );
};

export default Header;