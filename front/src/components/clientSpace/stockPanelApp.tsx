import React, { useState, useEffect } from 'react';
import StockNews from './stockNews';
import StockInfo from '../../types/StockInfo';
import StockGlobalInfo from './stockGlobalInfo';

import axios from 'axios';
import Entry from '../../types/Rss';

interface Props {
    stockName: string,
};

interface StockInfos {
    stockInfo: StockInfo,
    feed: Array<Entry>,
}

const StockPanel = (props: Props): JSX.Element => {
    const [stockInfos, setStockInfos] = useState<StockInfos | undefined>(undefined);
    const [error, setError] = useState<string | undefined>(undefined);

    useEffect(() => {
        axios({
            method: 'get',
            url: `http://localhost:4000/api/stocks/${props.stockName}`,
        }).then((res) => {
            setStockInfos({
                stockInfo: res.data.stockInfo,
                feed: res.data.feed,
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
            <StockNews feed={stockInfos.feed} />
        </div>
    );
};

export default StockPanel;