// 2. Create a Node.js Express Google Search Autocomplete API application to fetch
// data & download it in CSV file.


const express = require('express');
const axios = require('axios');
const { Parser } = require('json2csv');

const app = express();

app.get('/autocomplete', async (req, res) => {
    try {
        const q = req.query.q || 'python';

        const response = await axios.get(
            'https://suggestqueries.google.com/complete/search',
            {
                params: { client: 'firefox', q: q }
            }
        );

        const data = response.data[1].map(item => ({
            search_query: item
        }));

        res.json(data);
    } catch (error) {
        res.status(500).send('Error fetching data');
    }
});

app.get('/download', async (req, res) => {
    try {
        const q = req.query.q || 'python';

        const response = await axios.get(
            'https://suggestqueries.google.com/complete/search',
            {
                params: { client: 'firefox', q: q }
            }
        );

        const data = response.data[1].map(item => ({
            search_query: item
        }));

        const csv = new Parser().parse(data);

        res.header('Content-Type', 'text/csv');
        res.attachment('suggestions.csv');
        res.send(csv);
    } catch (error) {
        res.status(500).send('Error downloading CSV');
    }
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});
