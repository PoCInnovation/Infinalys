import React from 'react';
import Plot from 'react-plotly.js';

import Predictions from '../../types/Predictions';
import StockValues from '../../types/StockValues';
import { array } from 'prop-types';

interface Props {
    stock:StockValues,
    predictions: Predictions,
}

/**
 * @param size size of the array to generate
 * @returns an array containing all ids between 0 and size parameter
 */
const getIndexArray = (start: number, size: number): Array<number> => {
    const array = [];
    for (let i = start; i < size + start; i += 1) {
        array.push(i);
    }
    return array;
}

const LOOKBACK = 100;

const StockViewer = (props: Props): JSX.Element => (
    <div className="text-center">
        <h3>{`Stock movements over the previous ${LOOKBACK} days`}</h3>
        <Plot
            data={[
              {
                x: props.stock.Date.slice(props.stock.Date.length - LOOKBACK, props.stock.Date.length + 1),
                close: props.stock.Close.slice(props.stock.Close.length - LOOKBACK, props.stock.Close.length + 1),
                decreasing: {line: {color: '#7F7F7F'}},
                high: props.stock.High.slice(props.stock.High.length - LOOKBACK, props.stock.High.length + 1),
                increasing: {line: {color: '#17BECF'}},
                line: {color: 'rgba(31,119,180,1)'},
                low: props.stock.Low.slice(props.stock.Low.length - LOOKBACK, props.stock.Low.length + 1),
                open: props.stock.Open.slice(props.stock.Open.length - LOOKBACK, props.stock.Open.length + 1),
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
            layout={ {width: 1000, height: 700,}}
        />
        <h3>{`Tendency predictions for the next ${props.predictions.Mean.length} days`}</h3>
        <Plot
            data={[
                {
                    type: 'scatter',
                    x: getIndexArray(1, props.predictions.Mean.length),
                    y: props.predictions.Mean,
                }
            ]}
            layout={ {width: 600, height: 400,}}
        />
        <h3>{`Volume predictions for the next ${props.predictions.Mean.length} days`}</h3>
        <Plot
            data={[
                {
                    type: 'scatter',
                    x: getIndexArray(1, props.predictions.Volume.length),
                    y: props.predictions.Volume,
                }
            ]}
            layout={ {width: 600, height: 400,}}
        />
    </div>
);

export default StockViewer;