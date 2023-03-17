import express from "express";
import {RECOMMENDATION_MICROSERVICE_URL} from './config.js'
//import function from models.js
import { getConcertById, getAllConcertData } from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";
import axios from 'axios';
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


app.get("/reco/:id", async (req, res) => {
  try {
    console.log('hello')
    const userId = req.params.id;
    const url = `${RECOMMENDATION_MICROSERVICE_URL}/${userId}`;
    const response = await axios.get(url);

    // Send the response back to the frontend
    console.log(response);
    // res.send(response.data);
  } catch (error) {
    console.error(error);
    res.sendStatus(500);
  }
});

//PORT
app.listen(5005, () => {
  console.log("Server is running on port 5005");
});
