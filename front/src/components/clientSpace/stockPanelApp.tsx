import React, { useState, useEffect } from 'react';
import StockNews from './stockNews';
import StockInfo from '../../types/StockInfo';
import StockGlobalInfo from './stockGlobalInfo';
import StockViewer from './stockViewer';

import axios from 'axios';
import Entry from '../../types/Rss';
import Predictions from '../../types/Predictions';
import StockValues from '../../types/StockValues';

interface Props {
    stockName: string,
};

interface Stock {
    stockInfo: StockInfo,
    feed: Array<Entry>,
    stock: StockValues,
    predictions: Predictions,
};

const StockPanel = (props: Props): JSX.Element => {
    const [stockInfos, setStockInfos] = useState<Stock | undefined>(undefined);
    const [error, setError] = useState<string | undefined>(undefined);

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