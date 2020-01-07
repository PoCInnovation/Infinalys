import React from 'react';
import shortid from 'shortid';

const StockNews = (props) => (
    <div className="card">
    <h2>News</h2>
    {
        props.feed.map((entry) => (
            <a key={shortid.generate()} rel="noopener noreferrer" href={entry.link[0]} target="_blank">
                <p>{entry.title[0]}</p>
            </a>
        ))
    }
    </div>
);

export default StockNews;