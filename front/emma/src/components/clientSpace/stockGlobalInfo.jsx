import React from 'react';

interface Props {
    stockInfo: StockInfo
}

const StockGlobalInfo = (props: Props): JSX.Element => (
    <div className="card">
        <h2>{props.stockInfo.companyName}</h2>
        <h2>{props.stockInfo.stockName}</h2>
        <h2>{props.stockInfo.industry}</h2>
    </div>

);

export default StockGlobalInfo;
