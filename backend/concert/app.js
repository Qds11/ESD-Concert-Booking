import express from "express";
import {RECOMMENDATION_MICROSERVICE_URL} from './config.js'
//import function from models.js
import { getConcertById, getAllConcertData, getConcertByGenre } from "./model.js";
import bodyParser from "body-parser";
import cors from "cors";
import axios from 'axios';
const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//get all concerts
app.get("/", async (req, res) => {
  const concerts = await getAllConcertData();
  // const userId = req.query.userid;
   const userId=null
  if (userId) {
    const recommended = await axios.get(`http://localhost:5005/reco/${userId}`);
    return res.json({ concerts: concerts, recommended: recommended.data });
  }
  return res.json({concerts:concerts,recommended:null})
});

//get concert by id
app.get("/concert/:id", async (req, res) => {
  const id = req.params.id;
  const concert = await getConcertById(id);
  res.json(concert);
});

//get concert by genre (for recommendation)
app.get("/concert/:genre", async (req, res) => {
  const genre = req.params.genre;
  const concert = await getConcertByGenre(genre);
  res.json(concert);
});

//call recommendation microservice
app.get("/reco/:id", async (req, res) => {
  try {
    console.lof("HELLP")
    const userId = req.params.id;
    const url = `${RECOMMENDATION_MICROSERVICE_URL}/${userId}`;
    const response = await axios.get(url);
    const genre = response.data.message
    const concert = await getConcertByGenre(genre);

    // Send the response back to the frontend
    res.send(concert)
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
