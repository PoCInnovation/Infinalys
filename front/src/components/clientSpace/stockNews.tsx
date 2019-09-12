import React from 'react';
import shortid from 'shortid';
import Entry from '../../types/Rss';

interface Props {
    feed: Array<Entry>
}

const StockNews = (props: Props): JSX.Element => (
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