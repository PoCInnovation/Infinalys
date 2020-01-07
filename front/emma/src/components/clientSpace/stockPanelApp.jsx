import React, { useState, useEffect } from 'react';
import StockNews from './stockNews';
import StockGlobalInfo from './stockGlobalInfo';
import StockViewer from './stockViewer';

import axios from 'axios';


const StockPanel = (props) => {
    const [stockInfos, setStockInfos] = useState(undefined);
    const [error, setError] = useState(undefined);

    useEffect(() => {
        axios({
            method: 'get',
            url: `http://localhost:4000/api/stocks/${props.stockName}`,
        }).then((res) => {
            console.log(res);
            setStockInfos({
                stockInfo: res.data.stockInfo,
                feed: res.data.feed,
                predictions: res.data.predictions,
                stock: res.data.stocks,
            });
        }).catch((err) => {
            setError(err);
        });
    }, [props]);

    if (error) {
        return <p>{error}</p>
    }
    if (!stockInfos) {
        return <p className="text-center">Loading</p>;
    }
    return (
        <div>
            <StockGlobalInfo stockInfo={stockInfos.stockInfo} />
            <StockViewer stock={stockInfos.stock} predictions={stockInfos.predictions} />
            <StockNews feed={stockInfos.feed} />
        </div>
    );
};

export default StockPanel;
