const express = require('express');
const app = express();
const cors = require('cors');
app.use(cors());
const validate = require('validate.js');
const fs = require('fs');
const axios = require('axios');

const constraints = {
    stock_name: {
        presence: true,
        length: {
            min: 1,
            message: "stock name is empty"
        },
        format: {
            pattern: /^[A-Z]+(.[A-Z])*$/,
            message: '%{value} is not in a valid format.'
        }
    }
}

/**
 * wrapper for axios requests
 * @returns data collected
 */
function fetch_data(url) {
    return axios({
        method: 'get',
        url: url
    }).then(res => {
        return res.data;
    }).catch(err => {
        console.log(err);
        return null;
    });
}

const IRMA_API = 'http://localhost:3000/api';
const JEANPIERRE_API = 'http://localhost:5000/api';

/**
 * wrapper for calls to irma and jean-pierre api
 * @param {*} stock_name 
 * @returns a json object {infos: {jean-pierre json}, predictions: {irma-json}}
 */
async function get_stock(stock_name) {
    let json = await fetch_data(JEANPIERRE_API + '/news/' + stock_name);
    const predictions = await fetch_data(IRMA_API + '/predictions/' + stock_name);

    for (let key in predictions)
        json[key] = predictions[key];
    return json;
}

app.get('/api/stocks/:stock_name', async function (req, res, next) {
    const errors = validate(req.params, constraints);
    if (errors)
        return next(errors.message);
    const response_content = await get_stock(req.params.stock_name);
    res.status(200).send(response_content);
})

const PORT = 4000;

app.listen(PORT, function () {
    console.log('[*] Listening on port', String(PORT));
})
