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
        <div>
            <input
                className="search"
                placeholder="stock name"
                value={search}
                onChange={(e) => { setSearch(e.target.value); }}
            />
            <button onClick={() => { setClick(true); }}>Search</button>
        </div>
    );
};

export default ClientPanel;