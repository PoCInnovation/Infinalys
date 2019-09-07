const express = require('express');
const app = express();
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
        return null
    });
}

app.get('/api/news/:stock_name', async function (req, res, next) {
    const errors = validate(req.params, constraints);
    if (errors)
        return next(errors.message);
    res.status(200).send({"tintin": "milou"});
})

const PORT = 5000;

app.listen(PORT, function () {
    console.log('[*] Listening on port', String(PORT));
})