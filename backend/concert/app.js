import express from "express";
import RECOMMENDATION_MICROSERVICE_URL from './config.js'
//import function from models.js
import { getConcertById, getAllConcertData } from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";
import request from 'request';

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//get all spending data
app.get("/", async (req, res) => {
  const concerts = await getAllConcertData();
  return res.json(concerts);
});

// //get spending data filtered by date range
app.get("/concert/:id", async (req, res) => {

  const id = req.params.id;
  const concert = await getConcertById(id);
  res.json(concert);
});


const options = {
  url: RECOMMENDATION_MICROSERVICE_URL,
  method: "POST",
  json: { key: "value" }, // This is the data you want to send to the Flask microservice
};

request(options, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(body);
  }
});
//PORT
app.listen(5005, () => {
  console.log("Server is running on port 5000");
});
