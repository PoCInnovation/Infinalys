import React, { useState } from 'react';
import StockPanel from './clientSpace/stockPanelApp';

const ClientPanel = (): JSX.Element => {
    const [search, setSearch] = useState<string>('');
    const [click, setClick] = useState<boolean>(false);
    if (click) {
        return (
            <StockPanel stockName={search}/>
        );
    }
    return (
        <div className="text-center search">
            <h2>Search a Stock Name</h2>
            <input
                placeholder="stock name"
                value={search}
                onChange={(e) => { setSearch(e.target.value); }}
            />
            <button className="btn btn-primary" onClick={() => { setClick(true); }}>Search</button>
        </div>
    );
};

export default ClientPanel;