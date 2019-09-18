import React from 'react';
import Plot from 'react-plotly.js';

import Predictions from '../../types/Predictions';
import StockValues from '../../types/StockValues';

interface Props {
    stock:StockValues,
    predictions: Predictions,
}

const StockViewer = (props: Props): JSX.Element => (
    <div className="text-center">
        <Plot
            data={[
              {
                x: props.stock.Date,
                close: props.stock.Close,
                decreasing: {line: {color: '#7F7F7F'}},
                high: props.stock.High,
                increasing: {line: {color: '#17BECF'}},
                line: {color: 'rgba(31,119,180,1)'},
                low: props.stock.Low,
                open: props.stock.Open,
                type:'candlestick' as 'candlestick',
                xaxis:'x',
                yaxis:'y',
                layout:{
                    dragmode:'zoom',
                    margin:{
                      r: 10,
                      t: 25,
                      b: 40,
                      l: 60,
                }},
            },
            ]}
            layout={ {width: 1300, height: 700,}}
        />
    </div>
);

export default StockViewer;