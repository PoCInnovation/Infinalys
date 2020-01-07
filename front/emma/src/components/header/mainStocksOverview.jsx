import React, { useState, useEffect } from 'react';
import StockOverview from './stockOverview';
import shortid from 'shortid';

// const URL = '/api/stocks/overview';

/**
 * Displays a bar with stock overviews
 * The stocks values are fetched from the defined URL variable
 */
const MainStocksOverview = () => {
    const [loading, setLoading] = useState(true);
    const [stocks, setStocks] = useState([]);

    useEffect(() => {
        setStocks([
            {name: "AAPL",    trend: "down", trendPercentage: 0.5},
            {name: "DAX",     trend: "up", trendPercentage: 0.5},
            {name: "KER",     trend: "down", trendPercentage: 0.5},
            {name: "EUR-USD", trend: "up", trendPercentage: 0.5},
            {name: "GOLD",    trend: "down", trendPercentage: 0.5},
        ]);
        setLoading(false);
    }, []);

    return (
        <div className="box">
            <div className="stocks-overview">
                {
                    loading || !stocks.length ?
                        null
                    :
                        stocks.map((stock) => (
                            <StockOverview key={shortid.generate()} stock={stock}/>
                        ))
                }
            </div>
        </div>
    );
}

export default MainStocksOverview;