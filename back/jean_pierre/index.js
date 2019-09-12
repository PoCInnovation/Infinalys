const express = require('express');

const app = express();

const validate = require('validate.js');

const axios = require('axios');

const fs = require('fs');

const { parseString } = require('xml2js');

const { stockNameValidator } = require('./schemas');


/**
 * convert a rss string to a JSON object
 * @param rssString all rss feed as string
 * @returns a JSON object of the feed
 */
const sendRssAsJson = (responseCallback, rssString, info) => {
  parseString(rssString, (err, result) => {
    if (err) {
      throw err;
    }
    if (info) {
        return responseCallback.status(200).send({
          stockInfo: info,
          feed: result.rss.channel[0].item,
       }); 
    }
    return responseCallback.status(200).send({
      feed: result.rss.channel[0].item,
    });
  });
};

/**
 * wrapper for axios requests
 * @returns data collected
 */
const fetchData = (url) => axios({
  method: 'get',
  url,
}).then((res) => res.data).catch((err) => err);


/**
 * @returns all top news of the moment
 */
app.get('/api/news', async (req, res) => {
  const feed = await fetchData('https://news.google.com/news/rss');
  sendRssAsJson(res, feed, null);
});


/**
 * Gets name, stockName and industry of the company corresponding to the given stockName
 * @param {*} stockName
 */
const getCompanyInfos = (stockName) => {
  const content = String(
    fs.readFileSync('../../assets/top_500_sp.csv')
  ).split('\n');
  let tmp = [];
  for (let line = 0; line < content.length; line += 1) {
    tmp = content[line].split(',');
    if (tmp[0] === stockName) {
      return {companyName: tmp[1], stockName: tmp[0], industry: tmp[2]};
    }
  }
  return null;
};


/**
 * @param stockName name of a stock in the stock market
 * @return all the news related to this stock
 */
app.get('/api/news/:stockName', async (req, res, next) => {
  const errors = validate(req.params, stockNameValidator);
  if (errors) {
    return next(errors.message);
  }
  const companyInfos = getCompanyInfos(req.params.stockName);
  if (companyInfos === null) {
    return res.status(400).send({
      error: 'invalid stock name',
    });
  }
  const feed = await fetchData(
    `https://news.google.com/rss/search?q=${companyInfos.companyName}`,
  );
  sendRssAsJson(res, feed, companyInfos);
});


const PORT = 5000;


app.listen(PORT, () => {
  console.log('[*] Listening on port', PORT);
});
