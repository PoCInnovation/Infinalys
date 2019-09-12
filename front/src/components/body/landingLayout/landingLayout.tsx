import React from 'react';
import { Link } from 'react-router-dom';

const LandingLayout = (): JSX.Element => (
    <div className="landing-layout">
        <img src='http://pngimg.com/uploads/money/money_PNG3547.png' alt="infinalys"/>
        <div className="typewriter">
            <p className="typewriter-text">Artifical Intelligence as Financial Advisor</p>
            <br/>
            <Link to="/login">
                <button className="btn btn-primary">Login</button>
            </Link>
        </div>
    </div>
);

export default LandingLayout;